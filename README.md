# Machine Learning For Model Driven Engineering: Toxic Comment Classification

Social media users often encounter abuse, harassment, and insults from other users on most online communication platforms such as Facebook, Instagram, YouTube, etc., due to which many users stop expressing their ideas and opinions.

The solution to this problem is to create an effective model that can identify the level of toxicity of comments, such as threats, obscenities, insults, racism, etc., thus promoting a peaceful environment for online dialogue.

We will better understand the multi-label classification of toxic comments and create a model to classify comments into different toxicity labels.
The multi-label classification is a supervised machine learning approach where a single instance can be associated with multiple labels simultaneously. 

It allows the model to assign zero, one, or more labels to each data sample based on its characteristics.

In the context of toxic comment classification, a comment or text can be labeled with multiple toxicity categories if it contains various forms of harmful language.


## File Predict_Server
This Python script uses the Flask framework to create a web application that exploits a deep learning model (TensorFlow) to predict the toxicity of textual comments. 

The application includes a prediction function that loads a pre-trained model and a text vectorization layer. Prediction occurs when users enter a comment via a POST request. 

The start page is handled by a GET request, which displays a text input form.
The Flask app is started on port 5000 of localhost: to play with the template, run the file and click on the following link [User Interface](http://localhost:5000/predict).

This file has been added to allow the user to experiment with the model, which we have provided, via the GUI.
