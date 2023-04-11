import requests
import json
import html


def getquestion():
    global answer
    url = 'https://opentdb.com/api.php?amount=50&type=boolean'
    response = requests.get(url).json()
    questionresponse = response['results'][0]['question']
    question = html.unescape(questionresponse)
    answer = response['results'][0]['correct_answer']
    return question
getquestion()

answer = answer

