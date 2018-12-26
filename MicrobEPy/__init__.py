import os
import sys

PROJECT_NAME = "MicrobEPy"
# Names of the directories in this project
PYTHON_SUBDIRECTORIES = [
    "statistics", "model", "correlation",
    "data", "plot", "search", "common",
    ]

def getProjectDirectory():
  """
  :return str path:
  """
  curdir = os.getcwd()
  paths = []
  # Find the list of subpaths to this name
  while len(curdir) > 1:
    paths.append(curdir)
    curdir = os.path.split(curdir)[0]
  paths.reverse()
  # Find the path to the directory for this project
  found = False
  for path in paths:
    if PROJECT_NAME in path:
      found = True
      break
  if not found:
    raise RuntimeError("Could not find project path.")
  return path

def addPythonPaths(project_dir=None):
  """
  Adds the paths needed for python code.
  """
  if project_dir is None:
    project_dir = getProjectDirectory()
  # Directory of python codes
  main_code_path = os.path.join(project_dir, PROJECT_NAME)
  # Directory of python codes
  sys.path.append(main_code_path)
  for directory in PYTHON_SUBDIRECTORIES:
    path = os.path.join(main_code_path, directory)
    sys.path.append(path)

def isProjectModule():
  return PROJECT_NAME in os.getcwd()
    

if isProjectModule():
  addPythonPaths()
pass
  
