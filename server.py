# coding: utf-8

# In[4]:

import sys
import os
import json
from flask import Flask
from flask import jsonify

sys.path.append(os.path.join(os.getcwd(),'..'))
import watson_developer_cloud
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features


app = Flask("NLU App")

nlu = watson_developer_cloud.NaturalLanguageUnderstandingV1(
        version='2017-02-27',
        username=os.getenv('NATURAL_LANGUAGE_UNDERSTANDING_USERNAME'),
        password=os.getenv('NATURAL_LANGUAGE_UNDERSTANDING_PASSWORD'))

@app.route("/")
def eval_default():
        response = nlu.analyze(
                text='Bruce Banner is the Hulk and Bruce Wayne is BATMAN! '
                'Superman fears not Banner, but Wayne.',
                features=[features.Entities(), features.Keywords()])
        return jsonify(response)
 
 
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=int(os.getenv('PORT',8080)))
