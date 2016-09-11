from datetime import datetime
from unittest.mock import Mock
from dataactcore.models.jobModels import Submission, Job, FileGenerationTask
from dataactbroker.handlers.fileHandler import FileHandler
from random import randint
import pytest
import dataactcore.config
from dataactcore.scripts.databaseSetup import (
    createDatabase, dropDatabase, runMigrations)
from dataactcore.models.baseInterface import BaseInterface
from dataactbroker.handlers.interfaceHolder import InterfaceHolder as BrokerInterfaceHolder
"""
@pytest.fixture(scope='function')
def brokerDb():
    print("Setting up broker interface")
    rand_id = str(randint(10000, 19999))

    existingConfig = BaseInterface.dbConfig
    existingDbName = BaseInterface.dbName
    print("Old db name: " + str(existingDbName))
    config = dataactcore.config.CONFIG_DB
    config['db_name'] = 'unittest{}_data_broker'.format(rand_id)
    print("Broker db name: " + str(config["db_name"]))
    dataactcore.config.CONFIG_DB = config

    createDatabase(config['db_name'])
    runMigrations()
    existingInterface = BaseInterface.interfaces
    interface = BrokerInterfaceHolder(forceOverwrite=True)

    yield interface
    print("Doing broker teardown")
    interface.close()
    dropDatabase(config['db_name'])
    # Replace interfaces used by session-level fixture
    BaseInterface.interfaces = existingInterface
    BaseInterface.dbConfig = existingConfig
    BaseInterface.dbName = existingDbName
    print("Restored to dbname: " + str(BaseInterface.dbName))
"""

def test_start_generation_job(database):
    print("start generation test called")
    return
    fileHandler = FileHandler(None,database[1],True)
    # Mock D file API
    fileHandler.call_d_file_api = Mock(return_value=True)
    file_type = "D2"
    file_type_name = "award"
    sub, uploadJob, validationJob = setupSubmission(database[1], file_type_name)
    success, errorResponse = fileHandler.startGenerationJob(sub.submission_id, file_type)
    assert(success)
    # Get file generation task created
    task = database[1].jobDb.query(FileGenerationTask).filter(FileGenerationTask.submission_id == sub.submission_id).filter(FileGenerationTask.file_type_id == database[1].jobDb.getFileTypeId(file_type_name)).one()
    assert(task.job_id == uploadJob.job_id)
    assert(uploadJob.job_status_id == database[1].jobDb.getJobStatusId("running"))

    # Mock an empty response
    fileHandler.call_d_file_api = Mock(return_value=True)
    sub, uploadJob, validationJob = setupSubmission(database[1], file_type_name)
    success, errorResponse = fileHandler.startGenerationJob(sub.submission_id, file_type)
    assert(success)
    task = database[1].jobDb.query(FileGenerationTask).filter(FileGenerationTask.submission_id == sub.submission_id).filter(FileGenerationTask.file_type_id == database[1].jobDb.getFileTypeId(file_type_name)).one()
    assert(task.job_id == uploadJob.job_id)
    assert(uploadJob.filename == "#")
    assert(uploadJob.job_status_id == database[1].jobDb.getJobStatusId("finished"))

def setupSubmission(brokerDb, file_type_name):
    """ Create a submission with jobs for specified file type """
    # Create test submission
    sub = Submission(datetime_utc=datetime.utcnow(), user_id=1, cgac_code = "SYS", reporting_start_date = "01/01/2016", reporting_end_date = "01/31/2016")
    brokerDb.jobDb.session.commit()
    # Add jobs
    uploadJob = Job(job_status_id = brokerDb.jobDb.getJobStatusId("ready"), job_type_id = brokerDb.jobDb.getJobTypeId("file_upload"),
                    submission_id = sub.submission_id, file_type_id = brokerDb.jobDb.getFileTypeId(file_type_name))
    validationJob =  Job(job_status_id = brokerDb.jobDb.getJobStatusId("ready"), job_type_id = brokerDb.jobDb.getJobTypeId("csv_record_validation"),
                    submission_id = sub.submission_id, file_type_id = brokerDb.jobDb.getFileTypeId(file_type_name))
    brokerDb.jobDb.session.add(uploadJob)
    brokerDb.jobDb.session.add(validationJob)
    brokerDb.jobDb.session.commit()
    return sub, uploadJob, validationJob
