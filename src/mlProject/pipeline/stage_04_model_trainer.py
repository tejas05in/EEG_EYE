from mlProject import logger
from mlProject.components.model_trainer import ModelTrainer
from mlProject.config.configuration import ConfigurationManager

STAGE_NAME = "Model Trainer Stage"


class ModelTrainerTrainingPipeline:
    def __int__(self):
        pass

    def main(self):
        try:
            logger.info('Model Trainer Pipeline started')
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()
            logger.info('Model Trainer Pipeline completed')
        except Exception as e:
            logger.exception(f"Error occurred in Model Trainer Training Pipeline {e}")
            raise e
