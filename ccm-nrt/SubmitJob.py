import os
from Job import Job
import sys


# Set environment variables
os.environ['jobType'] = 'RELEASE'
os.environ['gitBranch'] = 'master'

jobType = os.getenv("jobType")
targetEnv = os.getenv("targetEnv")
gitBranch = os.getenv("gitBranch")
releaseTag = os.getenv("releaseTag")

buildParameters = {"jobType":jobType,"targetEnv":targetEnv,"gitBranch":gitBranch,"releaseTag":releaseTag}

print(" Build Parameters :",buildParameters)

# version = common.version
version = '1.3.0'

default_config_file = '/usr/local/pkg/hub/etc/dispatcher.conf'


def main():
    usage = """Usage: %prog [options] [args]

Manage Hub dispatcher

Arguments:
        [start|stop|restart|status]

Examples:
    ctrl-hub-dispatcher [start|stop|restart|status]
    ctrl-hub-dispatcher -c /etc/hub/hub.conf status
"""

    newjob = Job("RELEASE")

    print(newjob.jobDir)
    print('fileCopyTaskLsit :',newjob.fileCopyTaskLsit)

    for jobStepsDict in newjob.getTaskList():
        newjob.runTask(taskName=jobStepsDict["Step"],taskParameters=jobStepsDict.get("Arguments",None),buildParameters=buildParameters)

    print('fileCopyTaskLsit :', newjob.fileCopyTaskLsit)


"""
    # Setup logging
    log_level = conf.get('LOGGING', 'log_level', 'info')
    if options.trace:
        log_level = 'debug'
    log_file = conf.get('LOGGING', 'log_file', '/tmp/hub-dispatcher.log')
    log_max_size = conf.get('LOGGING', 'log_max_size', 5242880)  # 5MB
    log_retain = conf.get('LOGGING', 'log_retain', 5)

    log = logger.log_to_file(level=log_level, log_file=log_file,
                             max_size=log_max_size, retain=log_retain,
                             trace=options.trace)

    if options.verbose:
        log_level = 'debug'
    if options.quiet:
        log_level = 'critical'
    log = logger.log_to_console(level=log_level, trace=options.trace)

    if len(args) != 1:
        parser.error("Script takes exactly one argument")
    action = args[0]

    broker = conf.get('HUB', 'broker')
    pid_file = conf.get('HUB', 'pid_file')

    daemon = DispatcherDaemon(pid_file)
    if action == 'start':
        log.info('Starting dispatcher, connecting to broker {0}...'.format(
            broker))
        try:
            daemon.start(broker)
        except Exception, e:
            log.exception(e)
    if action == 'stop':
        log.info('Shutting down dispatcher...')
        try:
            daemon.stop()
        except Exception, e:
            log.exception(e)
"""

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        sys.stderr.write(
            'Aborting, something went wrong : ERROR : '
            '{0}\n'.format(e))
        sys.exit(2)
