import os
from os import listdir
from os.path import isfile, join

from imageai.Prediction import ImagePrediction

# https://github.com/OlafenwaMoses/ImageAI

execution_path = os.getcwd()

prediction = ImagePrediction()
prediction.setModelTypeAsSqueezeNet()
prediction.setModelPath(join(execution_path, "squeezenet_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.loadModel()

images_folder = join(execution_path, 'images')
images = [f for f in listdir(images_folder) if isfile(join(images_folder, f))]
for image in images:
    print(f'\n * Predicting - "{image}"')
    predictions, probabilities = prediction.predictImage(join(images_folder, image), result_count=5)
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction, " : ", eachProbability)
