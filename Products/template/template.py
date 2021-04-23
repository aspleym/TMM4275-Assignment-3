import os
import sys
import inspect

current_dir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)

parparent_dir = os.path.dirname(parent_dir)

sys.path.insert(0, parparent_dir)
print("CURRENT: ", current_dir)
print("PARENT: ", parparent_dir)

from Python.NXOpen.edges import runWC
from Python.mail import *

pathToPrtFile = "d:\Dropbox\Skole\TMM4275 - Automatisering i ingeniørarbeid, prosjekt\TMM4275-Assignment-3\Products/template/template.prt"

runWC(pathToPrtFile, [50, 50, 50])


adress = "aspleym@gmail.com"
password = "KBErocks!"
projectName = "template"

subject = 'Your WC Design has been successfully processed'
body = f"<p>A designer has now finished processing your design {projectName}.\
You can download a .prt file containing weld lines by following this <a href=\"http://127.0.0.1:8080/Products/{projectName}/{projectName}.prt\">link.</a></p>"
sendMailToClient(adress, password, subject, body)