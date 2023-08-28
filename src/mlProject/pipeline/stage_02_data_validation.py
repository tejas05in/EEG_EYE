from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidation

STAGE_NAME = "Data Validation Stage"


class DataValidationTrainingPipeline:
    def __int__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            raise e
