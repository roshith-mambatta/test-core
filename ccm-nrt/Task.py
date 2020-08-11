import error

import tasks
from utils.FileOperations import  readXml
import os
import shutil

class Task:

    exstreamPackageTaskList=[]
    fileCopyTaskLsit=[]
    def __init__(self):
        state = "STARTING"

    def runTask(self, **inputPars):
        pass #raise error.MethodNotImplemented('All tasks must have a run method')

    def updateActionListAndReleaseNote(self, releasefile):
        releaseTagContent = readXml(releasefile)
        print("Updating fileCopyTaskLsit")
        self.fileCopyTaskLsit=['CCM_services/EDITIQ/batches/*','CCM_services/ADV/Engine_batch.sh','CCM_services/DEMAT/*']
        print("inside updateActionListAndReleaseNote",self.fileCopyTaskLsit)

    def copyFileWithDirectorySignature(self, jobDirectory, repo):
        for sourcePath in self.fileCopyTaskLsit:
            src = ""
            dst = ""
            if sourcePath[-1] == "*":
                src = jobDirectory + "/git_copy/" + repo + "/" + sourcePath[:-2]
                dst = jobDirectory + "/package_content/" + sourcePath[:-2]
                shutil.copytree(src, dst)
            else:
                src = jobDirectory + "/git_copy/" + repo + "/" + sourcePath
                dst = jobDirectory + "/package_content/" + sourcePath
                dstfolder = os.path.dirname(dst)
                if not os.path.exists(dstfolder):
                    os.makedirs(dstfolder)
                shutil.copy(src, dst)
            print(src)

