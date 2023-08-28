import pandas as pd
from scipy.io.arff import loadarff

from mlProject import logger
from mlProject.config.configuration import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        logger.info("Data validation begins")
        try:
            validation_status = None

            data = pd.DataFrame(loadarff(self.config.unzip_data_dir)[0])
            data['eyeDetection'] = data['eyeDetection'].astype('int8')
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema or data[col].dtype != self.config.all_schema[col]:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
            logger.info(f"The DATA validation status is: {validation_status}")

            return validation_status

        except Exception as e:
            raise e
