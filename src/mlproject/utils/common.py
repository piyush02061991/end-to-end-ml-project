import yaml
import joblib
import logging
from ensure import ensure_annotations
from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError


# ====================== LOGGER CONFIGURATION ============================
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)
# =======================================================================


@ensure_annotations
def read_yaml_file(file_path: Path) -> ConfigBox:
    """
    =======================================================================
                                FUNCTION DETAILS
    =======================================================================
    Function Name : read_yaml_file
    -----------------------------------------------------------------------
    Description :
        Reads a YAML configuration file and returns its content as a
        ConfigBox object. This allows accessing configuration keys
        using dot notation (e.g., config.model.name).

    Input :
        file_path : Path
            Path object representing the YAML file to read.

    Output :
        ConfigBox
            Parsed YAML data returned as a ConfigBox object.

    Example :
        config = read_yaml_file(Path("config/config.yaml"))
        print(config.model.name)

    Raises :
        FileNotFoundError : If the YAML file does not exist.
        BoxValueError : If YAML content is empty.
        yaml.YAMLError : If there is an error parsing the YAML file.
    =======================================================================
    """

    if not file_path.exists():
        logger.error(f"❌ YAML file not found at: {file_path}")
        raise FileNotFoundError(f"YAML file not found at: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise BoxValueError("⚠️ YAML file is empty.")
            logger.info(f"✅ YAML file loaded successfully from: {file_path}")
            return ConfigBox(content)
    except yaml.YAMLError as e:
        logger.error(f"⚠️ Error parsing YAML file: {e}")
        raise yaml.YAMLError(f"Error parsing YAML file: {e}")


@ensure_annotations
def save_object(file_path: Path, obj) -> None:
    """
    =======================================================================
                                FUNCTION DETAILS
    =======================================================================
    Function Name : save_object
    -----------------------------------------------------------------------
    Description :
        Saves any Python object (model, preprocessor, etc.) to disk
        using joblib for serialization.

    Input :
        file_path : Path
            Path to save the object.
        obj : Any
            The object to serialize and save.

    Output :
        None

    Example :
        save_object(Path("artifacts/model.pkl"), model)
    =======================================================================
    """

    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(obj, file_path)
        logger.info(f"💾 Object saved successfully at: {file_path}")
    except Exception as e:
        logger.error(f"❌ Error saving object: {e}")
        raise e
