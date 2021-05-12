import datetime

import requests
import os


def lambda_handler(event, context):
    current_time = datetime.datetime.now()
    current_time += datetime.timedelta(hours=5, minutes=30)
    if current_time.strftime("%H") >= "08":
        current_time += datetime.timedelta(days=1)
    date = str(current_time.strftime('%d')) + '-' + str(current_time.strftime('%m')) + '-' + str(
        current_time.strftime('%y'))
    discord_url = os.environ['discord_webhook']
    districts_role = [{"district_id": int(os.environ['id']), "district_role": os.environ['role_id']}]

    for j in districts_role:
        url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=" + str(
            j["district_id"]) + " &date=" + date
        headers = {
            'Accept': 'application/json',
            'referer': 'https://www.cowin.gov.in/',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'cache-control': 'no-cache'
        }
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            if response.status_code == 403:
                print("403 " + j['district_id'])
            continue
        resp = response.json()
        message = ""
        for i in resp['sessions']:
            if i['min_age_limit'] < 45 and i['available_capacity'] > 0:
                message = message + "Name : " + str(i['name']) + "\n"
                message = message + "City : " + str(i['district_name']) + "\n"
                message = message + "Pincode : " + str(i['pincode']) + "\n"
                message = message + "Available Capacity : " + str(i['available_capacity']) + "\n"
        if message != "":
            message = message + "<@&" + j['district_id'] + ">\n"
            response = requests.post(discord_url, json={"content": message})
            print(message)
    return "FINISHED"
