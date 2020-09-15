from django.apps import AppConfig
from django.conf import settings
import os
import pickle
import sklearn


class PolyLinearConfig(AppConfig):
    name = 'poly_linear'
    path = os.path.join(settings.MODELS3, 'poly_models.p')

    # load models into separate variables
    # these will be accessible via this class
    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)
    regressor = data['regressor']
