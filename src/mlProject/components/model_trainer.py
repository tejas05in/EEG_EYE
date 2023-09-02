import pandas as pd
import os
from pathlib import Path
from mlProject import logger
from mlProject.utils.common import save_bin
from pycaret.classification import *
from mlProject.config.configuration import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        logger.info('Model training started')
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        data = pd.concat([train_data,test_data],ignore_index=True)

        # init setup
        s = setup(data, target=self.config.target_column, session_id=123)
        # create model
        knn = create_model('knn')

        # define search space
        # params = {"n_neighbors": self.config.n_neighbors, 'algorithm': self.config.algorithm,
        #          "leaf_size": self.config.leaf_size, "metric": self.config.metric}

        # tune model
        # tuned_knn = tune_model(knn, custom_grid=params)

        # save model obj as pickle file using joblib
        # save_bin(tuned_knn, Path(os.path.join(self.config.root_dir, self.config.model_name)))
        # uncomment the above line to save the tuned model

        save_bin(knn, Path(os.path.join(self.config.root_dir, self.config.model_name)))
