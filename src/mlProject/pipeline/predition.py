from src.mlProject.utils.common import load_bin
import pandas as pd
from pathlib import Path


class PredictionPipeline:
    def __int__(self):
        self.pipeline = load_bin(Path('artifacts/model_trainer', 'best_pipeline.pkl'))

    def predict(self, data):
        prediction = self.pipeline.predict(data)
        return prediction
