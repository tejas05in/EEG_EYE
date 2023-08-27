# EEG EYE moevement prediction project (E2E) with MLflow

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update entity
5. Update configuration manager (configuration.py) in src config
6. Update components
7. Update pipeline
8. Update the main.py
9. Update the app.py


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/tejas05in/EEG_EYE.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -p env python=3.8 -y
```

```bash
conda activate env/
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/tejas05in/End-to-End-Machine-Learning-Project-with-MLflow.mlflow \
MLFLOW_TRACKING_USERNAME=tejas05in \
MLFLOW_TRACKING_PASSWORD=9efcb5c7b79d0e949378459b922b1462a80fa413 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/tejas05in/End-to-End-Machine-Learning-Project-with-MLflow.mlflow

export MLFLOW_TRACKING_USERNAME=tejas05in 

export MLFLOW_TRACKING_PASSWORD=9efcb5c7b79d0e949378459b922b1462a80fa413

```




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model

youtube video [link](https://www.youtube.com/watch?v=pxk1Fr33-L4)