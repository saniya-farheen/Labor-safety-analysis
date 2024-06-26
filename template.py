import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "labor-safety-analysis"

list_of_files = [
"data\.gitkeep"
f"{project_name}/_init_.py",
f"{project_name}/components/_init__.py",
f"{project_name}/components/data_ingestion.py",
f"{project_name}/components/data_validation.py",
f"{project_name}/components/model_trainer.py", 
f"{project_name}/components/model_pusher.py",
f"{project_name}/configuration/_init__.py",
f"{project_name}/configuration/s3_operations.py",
f"{project_name}/constant/_init__.py",
f"{project_name}/constant/training_pipeline/_init__.py",
f"{project_name}/constant/application.py",
f"{project_name}/entity/_init__.py",
f"{project_name}/entity/artifacts_entity.py",
f"{project_name}/entity/config_entity.py",
f"{project_name}/exception/_init__.py",
f"{project_name}/logger/_init__.py",
f"{project_name}/pipeline/_init__.py",
f"{project_name}/pipeline/training_pipeline.py",
f"{project_name}/utils/_init_.py",
f"{project_name}/utils/main_utils.py",
"template/index.html",
".dockerignore",
"app.py",
"Dockerfile",
"requirements.txt",
"setup.py"
]

for filepath in list_of_files:
  filepath = Path(filepath)
  
  filedir, filename = os.path.split(filepath)
  
  if filedir !="":
    os.makedirs (filedir, exist_ok=True)
    logging.info(f"Creating directory: {filedir} for the file {filename}")
  if(not os.path.exists (filename)) or (os.path.getsize(filename) == 0):
    with open(filepath, 'w') as f:
      pass
      logging.info(f"Creating empty file: {filename}")

  else:

    logging.info(f"(filename) is already created")