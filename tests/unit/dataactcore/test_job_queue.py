from dataactcore.utils.jobQueue import JobQueue
from dataactcore.config import CONFIG_BROKER
from unittest.mock import Mock
from pytest import raises
from dataactcore.utils.responseException import ResponseException
import os.path


def test_generate_d_file_success(monkeypatch):
    """ Test successful generation of D1 and D2 files """
    local_file_name = "12345_test_file.csv"

    file_path = "".join([CONFIG_BROKER['d_file_storage_path'], local_file_name])

    with open(file_path, "w") as file:
        file.write("test")

    result_xml = "<results>test_file.csv</results>"

    jq = JobQueue()
    monkeypatch.setattr(jq, 'update_d_file_status', Mock())
    monkeypatch.setattr(jq, 'download_file', Mock())
    monkeypatch.setattr(jq, 'get_xml_response_content', Mock(return_value=result_xml))

    jq.generate_d_file(Mock(), 1, 1, Mock(), local_file_name, True)

    assert os.path.isfile(file_path)


def test_generate_d_file_failure(monkeypatch):
    """ Test unsuccessful generation of D1 and D2 files """
    local_file_name = "12345_test_file.csv"

    file_path = "".join([CONFIG_BROKER['d_file_storage_path'], local_file_name])

    with open(file_path, "w") as file:
        file.write("test")

    result_xml = ""

    jq = JobQueue()
    monkeypatch.setattr(jq, 'update_d_file_status', Mock())
    monkeypatch.setattr(jq, 'get_xml_response_content', Mock(return_value=result_xml))

    with raises(ResponseException) as excinfo:
        jq.generate_d_file(Mock(), 1, 1, Mock(), local_file_name, True)