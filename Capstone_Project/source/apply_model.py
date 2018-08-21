#!/usr/bin/env python


'''
 This scripts gets a keras model saved into a h5 file and applies it
 to a Image that is also passed as parameter. See example below:

 (In your terminal)
   $ python apply_model.py -m models/dl_second_architecture.h5 -i ../Data/forest/15403446_1737702549890374_779253027662987264_n.jpg
'''

'''
 -Importing some libraries
'''
from keras.models import load_model
from PIL import Image
import numpy as np
import sys, getopt, warnings

def make_prediction(model_path, image_path):
    '''
     -Importing model
    '''
    model = load_model(model_path)
    image = Image.open(image_path).resize((32,32),Image.ANTIALIAS)
    image_scaled = np.asarray([np.asarray(image)/255.])
    
    '''
     -Making predictions
    '''
    prediction, prob= model.predict_classes(image_scaled), np.max(model.predict(image_scaled))
    
    '''
    - Printing results
    '''

    pred_type = "Urban" 
    if prediction == 2:
        pred_type = "Beaches"
    elif prediction == 1:
        pred_type = "Forest"

    print "Prediction: ", pred_type
    print "Probability: {}%".format(int(round(prob,2)*100))


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "m:i:", ["profile=", "amount-of-photos="])
    except getopt.GetoptError as err:
        print str(err) 
        sys.exit(2)

    model_path = None
    image_path = None
    for o, a in opts:
        if o == "-m":
            model_path = a
        elif o == "-i":
            image_path = a

    if not model_path or not image_path:
        print "Invalid Args"
    else:
    	warnings.filterwarnings("ignore")
    	make_prediction(model_path, image_path)

if __name__ == "__main__":
    main()