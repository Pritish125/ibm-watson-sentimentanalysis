''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package :
# Import the sentiment_analyzer function from the package created:
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

#Initiate the flask app :
app = Flask(__name__)

@app.route("/sentimentAnalyzer", methods=["GET"])
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text = request.args.get("textToAnalyze")
    output_dict = sentiment_analyzer(text)
    score = output_dict['score']
    label = output_dict['label']

    if label is not None:

        label = label.split('_')[1]

    else:

        label = None

    return f"The given text has been identified as {label} with a score of {score}"

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5500)
