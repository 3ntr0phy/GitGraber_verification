import requests
import json

supported = ["FACEBOOK","FCM_SERVER_KEY","HEROKU","MAILGUN","SLACK_V1","SLACK_V2","SLACK_WEBHOOK_URL","SQUARE_PERSONAL_ACCESS_TOKEN"]

def verify(token,type):
    if type=="FACEBOOK":
        response = requests.get(f"https://developers.facebook.com/tools/debug/accesstoken/?access_token={token}&version=v3.2")
        if response.status_code == 200:
            return True
    elif type == "FCM_SERVER_KEY":
        url = 'https://fcm.googleapis.com/fcm/send'
        headers = {
            'Authorization': f'key={token}',
            'Content-Type': 'application/json'
        }
        data = '{"registration_ids":["1"]}'
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            return True
    elif type =="HEROKU":
        url = 'https://api.heroku.com/apps'
        headers = {
            'Accept': 'application/vnd.heroku+json; version=3',
            'Authorization': f'Bearer {token}'
        }
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            return True
    elif type=="MAILGUN":
        url = "https://api.mailgun.net/v3/domains"
        response = requests.get(url, auth=('api', token))
        if response.status_code == 200:
            return True
    elif type == "SLACK_V1" or type=="SLACK_v2":
        url = "https://slack.com/api/auth.test"
        params = {
            "token": token,
            "pretty": 1
        }
        response = requests.post(url, params=params)
        if response.status_code == 200:
            return True
    elif type == "SLACK_WEBHOOK_URL":
        url = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
        headers = {"Content-type": "application/json"}
        data = json.dumps({"text": ""})
        response = requests.post(url, headers=headers, data=data)
        if 'missing_text_or_fallback_or_attachments' in response.text:
            return True
    elif type == "SQUARE_PERSONAL_ACCESS_TOKEN":
        url = "https://connect.squareup.com/v2/locations"
        headers = {"Authorization": f"Bearer {token}"}

        response = requests.get(url, headers=headers)
        if 'AUTHENTICATION_ERROR' not in response.text:
            return True

