import requests
import json
import html


def getquestion():
    global response
    url = 'https://opentdb.com/api.php?amount=20&category=12&type=boolean'
    response = requests.get(url).json()
    questionresponse = response['results'][0]['question']
    question = html.unescape(questionresponse)
    return question
getquestion()

answer = response['results'][0]['correct_answer']
print(answer)
if answer == 'True':
    getquestion()
    answer = response['results'][0]['correct_answer']
elif answer == 'False':
    getquestion()
    answer = response['results'][0]['correct_answer']
