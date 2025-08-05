import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name = "Text_summarizer_NLP"

print("fsdfsdfds")

list_of_files = [
    Path(".github") / "workflows" / ".gitkeep",  # fixed folder name here
    Path("src") / project_name / "__init__.py",
    Path("src") / project_name / "components" / "__init__.py",
    Path("src") / project_name / "utils" / "common.py",
    Path("src") / project_name / "logging" / "__init__.py",
    Path("src") / project_name / "config" / "__init__.py",
    Path("src") / project_name / "config" / "configuration.py",
    Path("src") / project_name / "pipeline" / "__init__.py",
    Path("src") / project_name / "entity" / "__init__.py",
    Path("src") / project_name / "constants" / "__init__.py",
    Path("config") / "config.yaml",
    Path("params.yaml"),
    Path("app.py"),
    Path("main.py"),
    Path("Dockerfile"),
    Path("requirements.txt"),
    Path("setup.py"),
    Path("research") / "trials.ipynb",
]

for filepath in list_of_files:
    # Make sure filepath is a Path object
    filepath = Path(filepath)

    # Create parent directories if they don't exist
    if not filepath.parent.exists():
        filepath.parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory: {filepath.parent}")

    # Create the file if it doesn't exist or is empty
    if (not filepath.exists()) or (filepath.stat().st_size == 0):
        filepath.touch()
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists and is not empty: {filepath}")
