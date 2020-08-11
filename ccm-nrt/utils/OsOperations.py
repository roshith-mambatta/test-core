import subprocess
import shutil
import os
import git
import stat
import paramiko
import csv
from os import path


def call_win_batch(gitUrl,localGitPath):
    subprocess.call([r'C:\00_MyDrive\ccm_packager\run.bat', 'test'])
    print("Git cloned")

def git_clone(gitUrl,localGitPath):
    print("Git cloned")

def remote_transfer_files(method,sshClient,remotefilepath,localfilepath):
    if (method=="get"):
        ftp_client = sshClient.open_sftp()
        ftp_client.get(remotefilepath, localfilepath)
        ftp_client.close()
    else:
        ftp_client = sshClient.open_sftp()
        ftp_client.put(localfilepath, remotefilepath)
        ftp_client.close()

def run_batchOnCCMServer(appCode,pubFile):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("test.ccm.server.com", username="username", password="password")
    remote_transfer_files('put', "test.ccm.server.com", '', "inputPath")
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("cmd_to_execute")
    remote_transfer_files('get', "test.ccm.server.com", '', "inputPath")

def wrtieIntoCSV(file,fieldNames=[]):

    field_names = ['a', 'b', 'c']

    #initial content
    with open('/your/testReport.csv','w') as f:
        f.write('appCode,testCase,testCaseDesc,status,errorDesc\n') # TRAILING NEWLINE

    with open('/your/testReport.csv','a',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(['ADV','TC1','Test Case Description','SUCCESS',''])
        writer.writerow(['ADV','TC2','Test Case Description','FAILED','Error Description'])

"""
with open('/your/testReport.csv') as f:
    print(f.read())
"""