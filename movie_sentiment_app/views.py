from django.shortcuts import render
from django.http import HttpResponse
import pickle
from .text_preprocessing import text_preprocessing
import joblib

# Create your views here.
model = pickle.load(open('movie_sentiment_model1.pkl','rb'))


def index(request):
    if request.method == "POST":
        review = request.POST.get('review')
        print(review,"-----------------------------------------------------------")
        review_processed = text_preprocessing(review)
        print(review_processed,"===========================================================")
        print(type(review_processed),"===========================================================")
        # Ensure review_processed is a list
        review_processed = [review_processed]
        # Loading model to compare the results
        result = model.predict(review_processed)
        print(result[0])
        print(result)
        print("model loaded successfully................")
        if result[0] == 1:
            review_sentiment = "Positive"
        else:
            review_sentiment = "Negative"

        return render(request, "index.html",context={"result":review_sentiment})
    return render(request, "index.html")
    