""" These classes define the ORM models to be used by sqlalchemy for the job tracker database """

from sqlalchemy import Column, Integer, Text, ForeignKey, Boolean, Numeric, Index
from sqlalchemy.orm import relationship
from dataactcore.models.baseModel import Base

class FileTypeValidation(Base):
    __tablename__ = "file_type_validation"

    file_id = Column(Integer, primary_key=True)
    name = Column(Text)
    description = Column(Text)
    file_order = Column(Integer, nullable=False, server_default="0")

    TYPE_DICT = None
    TYPE_ID_DICT = None

class FieldType(Base):
    __tablename__ = "field_type"

    field_type_id = Column(Integer, primary_key=True)
    name = Column(Text)
    description = Column(Text)

    TYPE_DICT = None

class FileColumn(Base):
    __tablename__ = "file_columns"

    file_column_id = Column(Integer, primary_key=True)
    file_id = Column(Integer, ForeignKey("file_type_validation.file_id"), nullable=True)
    file = relationship("FileTypeValidation", uselist=False)
    field_types_id = Column(Integer, ForeignKey("field_type.field_type_id"), nullable=True)
    field_type = relationship("FieldType", uselist=False)
    name = Column(Text, nullable=True)
    name_short = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    required = Column(Boolean, nullable=True)
    padded_flag = Column(Boolean, default=False, server_default="False", nullable=False)
    length = Column(Integer)

class RuleSeverity(Base):
    __tablename__ = "rule_severity"

    rule_severity_id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)

    SEVERITY_DICT = None

class RuleSql(Base):
    __tablename__ = "rule_sql"

    rule_sql_id = Column(Integer, primary_key=True)
    rule_sql = Column(Text, nullable=False)
    rule_label = Column(Text)
    rule_description = Column(Text, nullable=False)
    rule_error_message = Column(Text, nullable=False)
    rule_cross_file_flag = Column(Boolean, nullable=False)
    file_id = Column(Integer, ForeignKey("file_type_validation.file_id", name="fk_file"), nullable=True)
    file = relationship("FileTypeValidation", uselist=False, foreign_keys=[file_id])
    rule_severity_id = Column(Integer, ForeignKey("rule_severity.rule_severity_id"), nullable=False)
    rule_severity = relationship("RuleSeverity", uselist=False)
    target_file_id = Column(Integer, ForeignKey("file_type_validation.file_id", name="fk_target_file"), nullable=True)
    target_file = relationship("FileTypeValidation", uselist=False, foreign_keys=[target_file_id])
    query_name = Column(Text)

class AwardFinancialHistory(Base):
    __tablename__ = "award_financial_history"
    award_financial_history_id = Column(Integer, primary_key=True)
    fieldname = Column(Text, nullable=False)
    tas = Column(Text, nullable=False)
    object_class = Column(Text)
    program_activity = Column(Text)
    fiscal_year = Column(Integer)
    quarter = Column(Integer)
    total = Column(Numeric, nullable=False)
    submission_id = Column(Integer, ForeignKey("submission.submission_id", name = "fk_history_submission"), nullable=False)

Index("ix_object_class_history",
  AwardFinancialHistory.fieldname,
  AwardFinancialHistory.tas,
  AwardFinancialHistory.object_class,
  AwardFinancialHistory.fiscal_year,
  AwardFinancialHistory.quarter,
  unique=True)

Index("ix_program_activity_history",
  AwardFinancialHistory.fieldname,
  AwardFinancialHistory.tas,
  AwardFinancialHistory.program_activity,
  AwardFinancialHistory.fiscal_year,
  AwardFinancialHistory.quarter,
  unique=True)