class Job(object):
    def __init__(self):
        None
class JobStep(Job):
    """
    Job

    """
    def __init__(self):
        None


import json

try:
    with open("config/job_steps.json", "r", encoding="utf-8") as file:
        jobStepsConfig=file.read()
    if not jobStepsConfig=="":
        jobStepsConfig=json.loads(jobStepsConfig)
    else:
        jobStepsConfig={}
except KeyError:
    print("Failed to load Job Steps")
print(type(jobStepsConfig))


for jobType, jobSteps in jobStepsConfig.items():
    print(jobType,"-------->>>")
    for jobStepsDict in jobSteps:
        for jobStep,jobStepInfo in jobStepsDict.items():
            print(jobStep, '->', jobStepInfo)
    print(jobType, "--------<<<")
