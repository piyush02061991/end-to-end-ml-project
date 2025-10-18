"""
template.py
----------------------------------------
A reusable ML project template script.
Creates a structured folder layout and
skeleton code files for an end-to-end
Machine Learning project.
----------------------------------------
Author: Ranadip
Date: YYYY-MM-DD
"""

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,  # Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="[%(asctime)s]: %(message)s:")

# ======================================================
# 1️⃣ Define folder structure
# ======================================================
PROJECT_NAME = "ml_project"

list_of_files = [
    f"src{PROJECT_NAME}/__init__.py",
    f"src{PROJECT_NAME}/components/__init__.py",
    f"src{PROJECT_NAME}/utils/__init__.py",
    f"src{PROJECT_NAME}/utils/common.py",
    f"src{PROJECT_NAME}/config/__init__.py",
    f"src{PROJECT_NAME}/config/configuration.py",
    f"src{PROJECT_NAME}/pipeline/evaluate.py",
    f"src{PROJECT_NAME}/entity/__init__.py",
    f"src{PROJECT_NAME}/entity/config_entity.py",
    f"src{PROJECT_NAME}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "app.py",
    "main.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

# ======================================================
# 2️⃣ Create folders and files
# ======================================================
for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)


    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        print(f"📁 Created directory: {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"📄 Created empty file: {filepath}")
    else:
        logging.info(f"✅ File already exists: {filepath}")

print("\n🎯 Project template setup complete!")

# ======================================================
# 3️⃣ Next steps (for user guidance)
# ======================================================
print("""
🚀 NEXT STEPS:
--------------
1️⃣ Add your dataset inside the 'data/' folder (create one if needed).
2️⃣ Update 'config/config.yaml' with file paths and model parameters.
3️⃣ Implement:
   - data_ingestion/data_loader.py for loading datasets
   - data_preprocessing/preprocess.py for cleaning and encoding
   - model/train.py for model training
   - model/evaluate.py for testing & metrics
4️⃣ Run 'python main.py' to orchestrate the ML pipeline.
""")
