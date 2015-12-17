import unittest
from interfaces.stagingInterface import StagingInterface
from dataactcore.models.jobModels import JobStatus, JobDependency, Status, Type
import requests
from interfaces.jobTrackerInterface import JobTrackerInterface
from interfaces.validationInterface import ValidationInterface
import os
import inspect
from dataactcore.aws.s3UrlHandler import s3UrlHandler
import json
import boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from dataactcore.scripts.databaseSetup import runCommands

class JobTests(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5000"
    JSON_HEADER = {"Content-Type": "application/json"}
    TABLE_POPULATED = False # Gets set to true by the first test to populate the tables
    DROP_TABLES = True # If true, staging tables are dropped after tests are run

    def __init__(self,methodName):
        """ Run scripts to clear the job tables and populate with a defined test set """
        super(JobTests,self).__init__(methodName=methodName)
        # Get staging handler


        if(not self.TABLE_POPULATED):
            # Create staging database
            try:
                runCommands(StagingInterface.getCredDict(),[],"staging")
            except:
                # Staging database already exists, keep going
                pass

            self.stagingDb = StagingInterface()

            # Clear job tables
            import dataactcore.scripts.clearJobs

            # Define user
            user = 1
            # Upload needed files to S3

            s3FileNameValid = self.uploadFile("testValid.csv",user)
            s3FileNamePrereq = self.uploadFile("testPrereq.csv",user)
            s3FileNameBadValues = self.uploadFile("testBadValues.csv",user)
            s3FileNameMixed = self.uploadFile("testMixed.csv",user)
            s3FileNameEmpty = self.uploadFile("testEmpty.csv",user)
            s3FileNameMissingHeader = self.uploadFile("testMissingHeader.csv",user)
            s3FileNameBadHeader = self.uploadFile("testBadHeader.csv",user)
            s3FileNameLongString = self.uploadFile("test.csv",user)

            # Populate with a defined test set
            jobTracker = JobTrackerInterface()
            sqlStatements = ["INSERT INTO submission (submission_id) VALUES (1)",
            "INSERT INTO job_status (job_id, status_id, type_id, submission_id, filename, file_type_id) VALUES (1, " + str(Status.getStatus("ready")) + "," + str(Type.getType("csv_record_validation")) + ",1, '" + s3FileNameValid + "',1)",
            "INSERT INTO job_status (job_id, status_id, type_id, submission_id, file_type_id) VALUES (2, " + str(Status.getStatus("ready")) + "," + str(Type.getType("file_upload")) + ",1,1)",
            "INSERT INTO job_status (job_id, status_id, type_id, submission_id, file_type_id) VALUES (3, " + str(Status.getStatus("ready")) + "," + str(Type.getType("csv_record_validation")) + ",1,1)",
            "INSERT INTO job_dependency (dependency_id, job_id, prerequisite_id) VALUES (1, 3, 2)",
            "INSERT INTO job_status (job_id, status_id, type_id, submission_id, file_type_id) VALUES (4, " + str(Status.getStatus("ready")) + "," + str(Type.getType("external_validation")) + ",1,1)",
            "INSERT INTO job_status (job_id, status_id, type_id, submission_id, file_type_id) VALUES (5, " + str(Status.getStatus("finished")) + "," + str(Type.getType("csv_record_validation")) + ",1,1)",
            "INSERT INTO job_status (job_id, status_id, type_id, submission_id, file_type_id) VALUES (6, " + str(Status.getStatus("finished")) + "," + str(Type.getType("file_upload")) + ",1,1)",
            "INSERT INTO job_status (job_id, status_id, type_id, submission_id, filename, file_type_id) VALUES (7, " + str(Status.getStatus("ready")) + "," + str(Type.getType("csv_record_validation")) + ",1, '" + s3FileNamePrereq + "',1)",
            "INSERT INTO job_dependency (dependency_id, job_id, prerequisite_id) VALUES (2, 7, 6)",
            "INSERT INTO job_status (job_id, status_id, type_id, submission_id, filename, file_type_id) VALUES (8, " + str(Status.getStatus("ready")) + "," + str(Type.getType("csv_record_validation")) + ",1, '" + s3FileNameBadValues + "',1)",
            "INSERT INTO job_status (job_id, status_id, type_id, submission_id, filename, file_type_id) VALUES (9, " + str(Status.getStatus("ready")) + "," + str(Type.getType("csv_record_validation")) + ",1, '" + s3FileNameMixed + "',1)",
            "INSERT INTO job_status (job_id, status_id, type_id, submission_id, filename, file_type_id) VALUES (10, " + str(Status.getStatus("ready")) + "," + str(Type.getType("csv_record_validation")) + ",1, '" + s3FileNameEmpty + "',1)",
            "INSERT INTO job_status (job_id, status_id, type_id, submission_id, filename, file_type_id) VALUES (11, " + str(Status.getStatus("ready")) + "," + str(Type.getType("csv_record_validation")) + ",1, '" + s3FileNameMissingHeader + "',1)",
            "INSERT INTO job_status (job_id, status_id, type_id, submission_id, filename, file_type_id) VALUES (12, " + str(Status.getStatus("ready")) + "," + str(Type.getType("csv_record_validation")) + ",1, '" + s3FileNameBadHeader + "',1)",
            "INSERT INTO job_status (job_id, status_id, type_id, submission_id, filename, file_type_id) VALUES (13, " + str(Status.getStatus("ready")) + "," + str(Type.getType("csv_record_validation")) + ",1, '" + s3FileNameLongString + "',1)"
            ]
            for statement in sqlStatements:
                jobTracker.runStatement(statement)
            validationDB = ValidationInterface()
#"CREATE TABLE file_columns (file_column_id integer PRIMARY KEY DEFAULT nextval('fileColumnSerial'), file_id integer REFERENCES file_type,field_types_id integer REFERENCES field_type , name text ,description text , required  boolean);",

            sqlStatements = [
            "DELETE FROM file_columns",
            "INSERT INTO file_columns (file_column_id,file_id,field_types_id,name,description,required) VALUES (1,3,4,'header 1','',True)",
            "INSERT INTO file_columns (file_column_id,file_id,field_types_id,name,description,required) VALUES (2,3,4,'header 2','',True)",
            "INSERT INTO file_columns (file_column_id,file_id,field_types_id,name,description,required) VALUES (3,3,4,'header 3','',False)",
            "INSERT INTO file_columns (file_column_id,file_id,field_types_id,name,description,required) VALUES (4,3,4,'header 4','',True)",
            "INSERT INTO file_columns (file_column_id,file_id,field_types_id,name,description,required) VALUES (5,3,4,'header 5','',True)"

            ]
            for statement in sqlStatements:
                validationDB.runStatement(statement)
            JobTests.TABLE_POPULATED = True
        else:
            self.stagingDb = StagingInterface()

    def uploadFile(self,filename,user):
        """ Upload file to S3 and return S3 filename"""
        # Get bucket name
        bucketName = s3UrlHandler.getBucketNameFromConfig()

        path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        fullPath = path + "/" +filename

        # Create file names for S3
        s3FileName = str(user) + "/" + filename

        # Use boto to put files on S3
        s3conn = S3Connection()
        key = Key(s3conn.get_bucket(bucketName))
        key.key = s3FileName
        bytesWritten = key.set_contents_from_filename(fullPath)

        assert(bytesWritten > 0)
        return s3FileName

    def test_valid_job(self):
        """ Test valid job """

        self.response = self.validateJob(1)

        if(self.response.status_code != 200):
            print(self.response.status_code)
            print(self.response.json()["errorType"])
            print(self.response.json()["message"])
            print(self.response.json()["trace"])
        assert(self.response.status_code == 200)
        self.assertHeader(self.response)
        # Check that job is correctly marked as finished
        jobTracker = JobTrackerInterface()
        assert(jobTracker.getStatus(1) == Status.getStatus("finished"))
        tableName = self.response.json()["table"]
        assert(self.stagingDb.tableExists(tableName)==True)
        assert(self.stagingDb.countRows(tableName)==1)



    def test_bad_values_job(self):
        # Test job with bad values
        jobId = 8
        self.response = self.validateJob(jobId)
        assert(self.response.status_code == 200)
        self.assertHeader(self.response)
        # Check that job is correctly marked as finished
        jobTracker = JobTrackerInterface()
        assert(jobTracker.getStatus(jobId) == Status.getStatus("finished"))
        tableName = self.response.json()["table"]
        assert(self.stagingDb.tableExists(tableName)==True)
        # TODO change number of rows to 0 once rules limiting type to integer are added
        assert(self.stagingDb.countRows(tableName)==2)

    def test_mixed_job(self):
        """ Test mixed job """
        jobId = 9
        self.response = self.validateJob(jobId)
        assert(self.response.status_code == 200)
        self.assertHeader(self.response)
        # Check that job is correctly marked as finished
        jobTracker = JobTrackerInterface()
        assert(jobTracker.getStatus(jobId) == Status.getStatus("finished"))
        tableName = self.response.json()["table"]
        assert(self.stagingDb.tableExists(tableName)==True)
        assert(self.stagingDb.countRows(tableName)==3)

    def test_empty(self):
        """ Test empty file """
        jobId = 10
        self.response = self.validateJob(jobId)
        assert(self.response.status_code == 400)
        self.assertHeader(self.response)
        # Check that job is correctly marked as finished
        jobTracker = JobTrackerInterface()
        assert(self.response.json()["message"]=="CSV file must have a header")
        tableName = self.response.json()["table"]
        assert(self.stagingDb.tableExists(tableName)==False)
        assert(self.stagingDb.countRows(tableName)==0)

    def test_missing_header(self):
        """ Test missing header in first row """
        jobId = 11
        self.response = self.validateJob(jobId)
        assert(self.response.status_code == 400)
        self.assertHeader(self.response)
        # Check that job is correctly marked as finished
        jobTracker = JobTrackerInterface()
        assert(self.response.json()["message"]=="Header : header 5 is required")
        tableName = self.response.json()["table"]
        assert(self.stagingDb.tableExists(tableName)==False)
        assert(self.stagingDb.countRows(tableName)==0)

    def test_bad_header(self):
        """ Test bad header value in first row """
        jobId = 12
        self.response = self.validateJob(jobId)
        assert(self.response.status_code == 400)
        self.assertHeader(self.response)
        # Check that job is correctly marked as finished
        jobTracker = JobTrackerInterface()
        assert(self.response.json()["message"]=="Header : Walrus not in CSV schema")
        tableName = self.response.json()["table"]
        assert(self.stagingDb.tableExists(tableName)==False)
        assert(self.stagingDb.countRows(tableName)==0)

    def test_long_string(self):
        """ Test many rows, and with one value being a long string with escaped values """
        jobId = 13
        self.response = self.validateJob(jobId)
        if(self.response.status_code != 200):
            print(self.response.status_code)
            print(self.response.json()["errorType"])
            print(self.response.json()["message"])
            print(self.response.json()["trace"])
        assert(self.response.status_code == 200)
        self.assertHeader(self.response)
        # Check that job is correctly marked as finished
        jobTracker = JobTrackerInterface()
        tableName = self.response.json()["table"]
        assert(self.stagingDb.tableExists(tableName)==True)
        print(self.stagingDb.countRows(tableName))
        assert(self.stagingDb.countRows(tableName)==18287)

    def test_bad_id_job(self):
        """ Test job ID not found in job status table """
        self.response = self.validateJob(2001)
        assert(self.response.status_code == 400)
        self.assertHeader(self.response)
        assert(self.response.json()["message"]=="Job ID not found in job_status table")
        tableName = self.response.json()["table"]
        assert(self.stagingDb.tableExists(tableName)==False)
        assert(self.stagingDb.countRows(tableName)==0)

    def test_prereq_job(self):
        """ Test job with prerequisites finished """
        self.response = self.validateJob(7)
        assert(self.response.status_code == 200)
        self.assertHeader(self.response)
        tableName = self.response.json()["table"]
        assert(self.stagingDb.tableExists(tableName)==True)
        assert(self.stagingDb.countRows(tableName)==4)

    def test_bad_prereq_job(self):
        """ Test job with unfinished prerequisites """
        self.response = self.validateJob(3)
        assert(self.response.status_code == 400)
        self.assertHeader(self.response)
        assert(self.response.json()["message"] == "Prerequisites incomplete, job cannot be started")
        tableName = self.response.json()["table"]
        assert(self.stagingDb.tableExists(tableName)==False)
        assert(self.stagingDb.countRows(tableName)==0)

    def test_bad_type_job(self):
        """ Test job with wrong type """
        self.response = self.validateJob(4)
        assert(self.response.status_code == 400)
        self.assertHeader(self.response)
        assert(self.response.json()["message"] == "Wrong type of job for this service")
        tableName = self.response.json()["table"]
        assert(self.stagingDb.tableExists(tableName)==False)
        assert(self.stagingDb.countRows(tableName)==0)

    # TODO uncomment this unit test once jobs are labeled as ready
    #def test_finished_job(self):
        #""" Test job that is already finished """
        #self.response = self.validateJob(5)
        #assert(self.response.status_code == 400)
        #self.assertHeader(self.response)
        #assert(self.response.json()["message"] == "Job is not ready")
        #tableName = self.response.json()["table"]
        #assert(self.stagingDb.tableExists(tableName)==False)
        #assert(self.stagingDb.countRows(tableName)==0)
        #self.dropTables(tableName)

    def assertHeader(self, response):
        """ Assert that content type header exists and is json """
        assert("Content-Type" in response.headers)
        assert(response.headers["Content-Type"] == "application/json")

    def validateJob(self, jobId):
        """ Send request to validate specified job """
        url = "/validate/"
        return requests.request(method="POST", url=self.BASE_URL + url, data=self.jobJson(jobId), headers = self.JSON_HEADER)

    def tearDown(self):
        self.dropTables(self.response.json()["table"])

    def dropTables(self, table):
        if(self.DROP_TABLES):
            stagingDb = StagingInterface()
            stagingDb.dropTable(table)
            return True
        else:
            return False
    def jobJson(self,jobId):
        """ Create JSON to hold jobId """
        return '{"job_id":'+str(jobId)+'}'

