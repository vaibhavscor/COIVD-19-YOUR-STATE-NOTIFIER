from plyer import notification
import requests
from bs4 import BeautifulSoup     
import json

# function for shoing notification on windows 
def notf(title,msg):
    notification.notify(
        title = title, message = msg, app_icon = 'Your icon image  path', timeout = 15 ) 
 



if __name__ == "__main__":
    
    url_slack = 'https://hooks.slack.com/services/ 'Your Web hooker slack channel id' # your slack channel id 
    url = 'https://www.mohfw.gov.in'  # Govenment of india site for data scrapping 
    r  = requests.get(url).text
    soup = BeautifulSoup(r,'html')
    statelist = ""
    for tableb in soup.find_all('tbody')[7].find_all('tr'):
        statelist += tableb.get_text()

    statelist = statelist[1:]
    statelist = statelist.split("\n\n")     
    
    states = ['Chhattisgarh']    # your state name inside list , if multiple states seprate with , 
    for item in statelist[0:22]:
        mainlist = item.split('\n')
        if mainlist[1] in states:
        # windows notifaction 
            notf('Alert',f"{mainlist[1]}  No. of Cases:{mainlist[2]}\n  Foregincases:{mainlist[3]}\n  Cured:{mainlist[4]}\n  Deaths:{mainlist[5]}")

        # slack channel notification 
            slack_msg = {'text':f"Covid-19\n{mainlist[1]}\nNo. of Cases:{mainlist[2]}\nForegincases:{mainlist[3]}\nCured:{mainlist[4]}\n Deaths:{mainlist[5]}"}
            requests.post(url_slack,data=json.dumps(slack_msg))

