from django.apps import AppConfig
from django.conf import settings
import os
import pickle
import sklearn

class PredictConfig(AppConfig):
    name = 'predict'
    # create path to models
    path = os.path.join(settings.MODELS, 'simple_models.p')

    # load models into separate variables
    # these will be accessible via this class
    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)
    regressor = data['regressor']
