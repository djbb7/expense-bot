import os
import json
import sys
import logging
logger = logging.getLogger()
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))

import requests

def sendWelcomeMessage(chat_id, url):
    response = {
        'chat_id': chat_id,
        'text': 'Welcome to the Split bot. I will keep track of your expenses and help you save money :-).'
    }
    
    requests.post(url, response)

def sendHelpMessage(chat_id, url):
    response = {
        'chat_id': chat_id,
        'text': 'List of commands:'
    }
    
    requests.post(url, response)
    
def sendNotUnderstoodMessage(chat_id, url):
    response = {
        'chat_id': chat_id,
        'text': 'Sorry. I didn\'t understand this command. Try asking for /help'
    }
    
    requests.post(url, response)
    
def lambda_handler(event, context):
    logger.info('got event{}'.format(event))
    logger.error('error here')
    token = os.environ['TELEGRAM_TOKEN']
    
    url = 'https://api.telegram.org/bot'+ token + '/sendMessage'

    data = json.loads(event['body'])
    
    text = data['message']['text']

    chat_id = data['message']['chat']['id']

    if text == '/start':
        sendWelcomeMessage(chat_id, url)
    elif text == '/help':
        sendHelpMessage(chat_id, url)
    else:
        sendNotUnderstoodMessage(chat_id, url)
    
    first_name = data['message']['chat']['first_name']
    
    
    
    return {"statusCode": 200}

