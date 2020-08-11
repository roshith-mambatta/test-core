import zipfile
import os
import re
import sys
import ssl
import sys
import time
import Job
import error

# pip install urllib3
try:
    from urllib.error import URLError
    from urllib import request as urllib2
except ImportError:
    from urllib import URLError


def git_clone(job: Job, git_url, branch_name='master'):
    path = job.jobDir + "/git_copy"
    print("path :", path)
    git_url = git_url.replace(' ', '')
    username, projectname = re.match('https://github.com/(.+)/(.+)',
                                     git_url).groups()[0:2]
    url = 'https://codeload.github.com/{}/{}/zip/{}'.format(
        username, projectname, branch_name)
    filename = path + '/' + projectname
    zipfile_name = filename + '.zip'
    try:
        urllib2.urlretrieve(url, zipfile_name, reporthook=report_hook)
    except URLError:
        raise error.ValidationError(url)


    with zipfile.ZipFile(zipfile_name, 'r') as f:
        f.extractall(path + '/.')
    if os.path.exists(filename + '-' + branch_name):
        os.rename(filename + '-' + branch_name, filename)
    os.remove(zipfile_name)
    print('\n{} downloaded'.format(git_url))


def report_hook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return

    duration = time.time() - start_time + 0.000001
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    if 100 >= percent >= 0:
        sys.stdout.write("\r{} %, {} KB, {} KB/s, {} seconds passed         " .format(
            percent, progress_size / 1024, speed, round(duration,2)))
    else:
        sys.stdout.write("\r{} KB, {} KB/s, {} seconds passed         " .format(
            progress_size / 1024, speed, round(duration,2)))
    sys.stdout.flush()