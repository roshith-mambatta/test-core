import shutil, os

releaseFolder="C:/00_MyDrive/gitrepo/release.0.1"
os.makedirs(releaseFolder, exist_ok=True)

from_home_path='C:/00_MyDrive/gitrepo'
files = ['/dataframe-pyexamples/src/dataframe/from/sql/FinanceDataAnalysis.py'
         ,'/dataframe-pyexamples/src/dataframe/from/sql/WindowsFuncDemo.py']
for f in files:
    os.makedirs(releaseFolder+"/dataframe-pyexamples/src/dataframe/from/sql", exist_ok=True)
    shutil.copy(from_home_path+f, releaseFolder+"/dataframe-pyexamples/src/dataframe/from/sql")
