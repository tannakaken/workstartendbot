import os
import requests
import chatpywork
import datetime 

token = os.environ['token']  
roomid = os.environ['roomid']

room = chatpywork.Room(roomid, token)

base_url = 'http://s-proj.com/utils/checkHoliday.php?kind='
check_holiday_url = base_url + 'h'
check_week_start_url = base_url + 'ws'
check_week_end_url = base_url + 'we'
check_month_start_url = base_url + 'ms'
check_month_end_url = base_url + 'me'

def lambda_handler(event, context):
    dt_now = datetime.datetime.now()
    work_end = dt_now.hour > 18
    if work_end:
        message = "[toall]\n皆さんお疲れ様です。\ntoggleとzoomとマネーフォワードを切ることを忘れないようにしてください。"
    else:
        message = "[toall]\n皆さんおはようございます。\ntoggleとzoomとマネーフォワードを忘れないようにしてください。"
    if 'holiday' == requests.get(check_holiday_url).text:
        print('holiday')
        return {'status': 200}
    if 'weekstart' == requests.get(check_week_start_url).text:
        message = message + "\n今週もがんばりましょう。"
    elif 'weekend' == requests.get(check_week_end_url).text:
        if work_end:
            message = message + "\n良い週末を！。"
        else:
            message = message + "\n今週もあと1日です。がんばりましょう。"
    if 'monthend' == requests.get(check_month_end_url).text:
        if work_end:
            message = message + "\n月末ですのでmoneyforwardが提出可能か確認しましたね。"
        else:    
            message = message + "\n月末ですのでmoneyforwardを提出可能にしておきましょう"
    print(message)
    response = room.send_message(message)
    return {'status': response.status}
        
