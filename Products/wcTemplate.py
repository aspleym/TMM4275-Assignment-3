from Python.NXOpen.edges import runWC
import os
import sys
import inspect
current_dir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
print("CURRENT: ", current_dir)
print("PARENT: ", parent_dir)


pathToPrtFile = <<PATH>>

runWC(pathToPrtFile, [<<BOTSIZE>>])
