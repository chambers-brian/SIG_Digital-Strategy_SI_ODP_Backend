from dataactvalidator.app import createApp
from dataactcore.interfaces.db import GlobalDB
from dataactcore.models import lookups
from dataactcore.models.validationModels import FileTypeValidation, FieldType, RuleSeverity


def setupValidationDB():
    """Create validation tables from model metadata and do initial inserts."""
    with createApp().app_context():
        sess = GlobalDB.db().session
        insertCodes(sess)
        sess.commit()


def insertCodes(sess):
    """Insert static data."""
<<<<<<< HEAD

    # insert file types
    fileTypeList = [
        (1, 'appropriations', 'appropriations file',1),
        (2, 'program_activity','program activity and object class file',2),
        (3, 'award_financial', 'award_financial file',3),
        (4, 'award', 'award file',4),
        (5, 'award_procurement', 'award procurement file', 5),
        (6, 'derivative', 'derivative file',6),
        (7, 'non_derivative','non derivative file',7)
        ]
    for f in fileTypeList:
        fileType = FileTypeValidation(file_id=f[0], name=f[1], description=f[2], file_order = f[3])
        sess.merge(fileType)
=======
    # insert validation file type
    # todo: combine this table with file_types table
    for f in lookups.FILE_TYPE:
        if f.order is not None:
            fileType = FileTypeValidation(file_id=f.id, name=f.name, description=f.desc, file_order=f.order)
            sess.merge(fileType)
>>>>>>> upstream/master

    # insert field types
    for f in lookups.FIELD_TYPE:
        fieldType = FieldType(field_type_id=f.id, name=f.name, description=f.desc)
        sess.merge(fieldType)

    # insert rule severity
    for s in lookups.RULE_SEVERITY:
        ruleSeverity = RuleSeverity(rule_severity_id=s.id, name=s.name, description=s.desc)
        sess.merge(ruleSeverity)


if __name__ == '__main__':
    setupValidationDB()
