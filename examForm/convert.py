import subprocess

print('Running')

p = subprocess.Popen("pyuic5.bat -x mainwindow.ui -o mainDesign.py")

stdout,stderr = p.communicate()

print('Finished')
