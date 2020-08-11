# import the class from the module Task
from Task import Task
from datetime import datetime
from utils.FileOperations import readXml,createTarFile
import error
import os
import tasks.GitClone as G

class Job(Task):
    """
    A job is a collection of tasks
    """

    def __init__(self, jobtype=None):
        Task.__init__(self)
        self.jobType = jobtype
        self.jobID  = jobtype + "_" + datetime.now().strftime('%Y%m%d%H%M%S%f')
        base_dir="C:/00_MyDrive/Python/orc-jobs"
        self.jobDir = base_dir + "/" + self.jobID
        self.taskList = None
        self._validate()
        self._setUp()

    def _validate(self):
        _checkJobTypeExists = False
        for jobType, jobSteps in readXml("config/job_steps.json").items():
            if jobType == self.jobType:
                _checkJobTypeExists = True
                self.taskList = jobSteps

        if not _checkJobTypeExists:
            raise error.ValidationError('Invalid job type')

    def _setUp(self):
        """
        Set up job working directory
        -- {jobType}_{jobID}
           |-- git_copy
           |-- package_content
           |-- exstream_pubfiles
           |-- tasks.log
        :return:
        """
        os.makedirs(self.jobDir, exist_ok=True)
        os.makedirs(self.jobDir + "/git_copy", exist_ok=True)
        os.makedirs(self.jobDir + "/package_content", exist_ok=True)
        os.makedirs(self.jobDir + "/exstream_pubfiles", exist_ok=True)
        open(self.jobDir+"/tasks.log", 'a').close()

    def getTaskList(self):
        return self.taskList

    def runTask(self,  **inputPars):

        if inputPars["taskName"] == 'GIT_CLONE':
            print("------------------------",inputPars["taskName"],"----------------------------------------")
            print("Getting in clone",inputPars["taskParameters"]["giturl"],inputPars["buildParameters"]["gitBranch"])
            G.git_clone(self,inputPars["taskParameters"]["giturl"], inputPars["buildParameters"]["gitBranch"])
        elif inputPars["taskName"] == 'READ_RELEASE_TAG':
            self.updateActionListAndReleaseNote('config/job_steps.json')
            self.copyFileWithDirectorySignature(self.jobDir,"test-core")
            createTarFile(self.jobDir+"/package_content", "ccm.build.tar")
"""
import importlib
module=importlib.import_module("tasks.GitClone.git_clone")
getattr(module,'GitClone.git_clone')()
#https://stackoverflow.com/questions/448271/what-is-init-py-for#448279
"""