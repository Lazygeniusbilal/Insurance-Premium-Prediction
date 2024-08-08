import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "Insurance_premium_prediction"
files_path = [

    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py"
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "params.yaml",
    "schema.yaml",
    "requirements.txt",
    ".gitignore",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html"
]

for file in files_path:

    file = Path(file)
    filedir, filename = os.path.split(file)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"{filedir} created for {filename}")
    if (not os.path.exists(file)) or (os.path.getsize(file) == 0):
        with open(file, "w") as f:
            pass
            logging.info(f"Creating an empty file {file}")
    else:
        logging.info(f"{filename} already exists!")