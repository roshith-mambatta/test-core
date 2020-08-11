import json
import error
import tarfile
import os


def readXml(file):
    try:
        with open(file, "r", encoding="utf-8") as file:
            fileContent = file.read()
        if not fileContent == "":
            _jsonData = json.loads(fileContent)
        else:
            _jsonData = {}
        return _jsonData
    except KeyError:
        print("Failed to load Job Steps")


def createTarFile(location, targetFileName):
    print(location + "/" + targetFileName)
    with tarfile.open(location + "/" + targetFileName, mode='w') as archive:
        archive.add(location, recursive=True, arcname='')


    """
def copyFileWithDirectorySignature(job: Job,repo):

    for sourcePath in job.fileCopyTaskLsit:
        src = ""
        dst = ""
        if sourcePath[-1] == "*":
            src = job.jobDir + "/git_copy/" + repo + "/" + sourcePath[:-2]
            dst = job.jobDir + "/package_content/" + sourcePath[:-2]
            shutil.copytree(src, dst)
        else:
            src = job.jobDir + "/git_copy/" + repo + "/" + sourcePath
            dst = job.jobDir + "/package_content/" + sourcePath
            dstfolder = os.path.dirname(dst)
            if not os.path.exists(dstfolder):
                os.makedirs(dstfolder)
            shutil.copy(src, dst)
        print(src)
        
        if src[-1] == '*':
            shutil.copytree(src, dst)
        dstfolder = os.path.dirname(dst)
        if not os.path.exists(dstfolder):
            os.makedirs(dstfolder)
        shutil.copytree(src, dst)
        """


"""
src = "Folder1/Folder2/file1"
dst = "Folder3" + src
dstfolder = os.path.dirname(dst)
if not os.path.exists(dstfolder):
    os.makedirs(dstfolder)
shutil.copy(src, dst)
"""
