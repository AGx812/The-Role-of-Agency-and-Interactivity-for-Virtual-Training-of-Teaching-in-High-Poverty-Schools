# from rasa import api,model
# from rasa import __main__ as ma
# from rasa_sdk import Tracker
# from rasa import core
# import actions.actions as action
import requests
# TEST = "http://localhost:5005/conversations/{conversation_id}/tracker"
# import sys

# PARSE = "http://localhost:5005/model/parse"
URL = "http://localhost:5005/webhooks/rest/webhook"
# ADD_MESSAGE = ""
# PARAMS = {"text":"hello"} # user_input should be in dictionary form

# ____________________________________________________
# Input: Userinput: text
# Output: (Intent: String, Responses: List of Strings)
#_____________________________________________________
def main(userIn):
    # intent = requests.post(url=PARSE, json={"text": userIn})
    message = {"sender":"test_user", "message": userIn}
    feedback = requests.post(url=URL, json=message).json()
    # print(feedback)
    # intent = intent.json()['intent']['name']
    # tracker = core.retrieve()
    # print("intent is ", intent)
    # intent = action.ActionPrintIntent()

    # print('Your intent is ', intent)
    # data = feedback.json()
    responses = []
    if feedback:
        userID = feedback[0]['recipient_id']
        TEST = "http://localhost:5005/conversations/"+userID+"/tracker"
        # print(TEST)
        # print('userID is ', userID)
        intent = requests.get(url=TEST).json()["latest_message"]['intent']['name']
        print(intent)
    # print('-----------',userID)
        # print(feedback)
        for response in feedback:
        # print(i.keys())
            if response['recipient_id'] == userID:
                if 'text' in response:
                    responses.append(response['text'])
                    print(response['text']) #reponse['text'] are text responses from the bot
                if 'image' in response:
                    responses.append(response['image'])
                    print(response['image']) #image response from the bot
        # print('responses is ', responses)
        return intent, responses
# def interact():
#     print("To stop talking, enter '\stop' ")

#     while(True):
#         text = input("Prompt: ")
#         # print(text)
#         if text == '\stop':
#             break
#         else:
#             main(text)
# interact()