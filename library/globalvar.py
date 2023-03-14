import os

BASE_DIR=os.path.dirname(os.path.dirname(__file__))
DATA_DIR=BASE_DIR+"/data/"
CACHE_DIR=DATA_DIR+"cache/"
CONFIG_DIR=DATA_DIR+"config/"
MODELS_DIR=DATA_DIR+"models/"
PREDS_DIR=DATA_DIR+"preds/"
LOGS_DIR=DATA_DIR+"logs/"
RUNNING_DIR=DATA_DIR+"running/"
FACTORS_DIR=DATA_DIR+"factors/"
CODE_FACTORS_DIR=FACTORS_DIR+"code_factors/"
DATE_FACTORS_DIR=FACTORS_DIR+"date_factors/"
SINGLE_FACTORS_DIR=FACTORS_DIR+"single_factors/"
FACTORS_CACHE_DIR=CACHE_DIR+"factors/"
PRICE_CACHE_DIR=CACHE_DIR+"price/"