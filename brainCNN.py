import keras
from keras.models import load_model
from scipy import misc, spatial
from PIL import Image
from imageio import imread
import numpy as np

model = load_model("MnistModel.h5")

def predict(InputImg):
    image = imread(InputImg,pilmode="L")
    image = np.invert(image)
    image = misc.imresize(image,(28,28))
    image = image.reshape(1,28,28,1)

    return model.predict(image)[0].tolist().index(1)

