import requests
import configparser
from datetime import datetime, date, time

class Build:
    def __init__(self, key, num, state, completeddt):
        self.key = key
        self.num = num
        self.state = state
        self.completeddt = completeddt



ini = configparser.ConfigParser()
#ini.read('C:/DATA/TEST/BuildSiren/buildsiren.cfg')
ini.read('/etc/buildsiren/buildsiren.conf')

url = ini.get('config','url')
user = ini.get('config','user')
pwd = ini.get('config','pwd')

completedon = datetime.min

# Get the list of builds
r = requests.get(url + '/rest/api/latest/result.json?os_authType=basic&max-results=1000', auth=(user, pwd))
bamboodata = r.json()

# iterate through the build the find the latest
# this will be the base build will generate no event
for i in range(0, bamboodata['results']['max-result']):
    planurl = bamboodata['results']['result'][i]['link']['href'] + '.json?os_authType=basic'
    planresult = requests.get(planurl,  auth=(user, pwd))
    planjson = planresult.json()
    if completedon < datetime.strptime(planjson['buildCompletedDate'], '%Y-%m-%dT%H:%M:%S.%fZ'):
        completedon = datetime.strptime(planjson['buildCompletedDate'], '%Y-%m-%dT%H:%M:%S.%fZ')
        plankey = planjson['plan']['key']
        buildnum = planjson['buildNumber']
        buildstate = planjson['state']
    # print(str(complettedon) + ',' + planjson['plan']['key'] + ',' + str(planjson['buildNumber']) + ',' + planjson['state'])

print(str(completedon) + ',' + plankey + ',' + str(buildnum) + ',' + buildstate)

while True:
    # Get the list of builds
    r = requests.get(url + '/rest/api/latest/result.json?os_authType=basic&max-results=1000', auth=(user, pwd))
    bamboodata = r.json()

    buildlist = []

    # iterate through the build the find the newer builds
    for i in range(0, bamboodata['results']['max-result']):
        planurl = bamboodata['results']['result'][i]['link']['href'] + '.json?os_authType=basic'
        planresult = requests.get(planurl,  auth=(user, pwd))
        planjson = planresult.json()
        if completedon < datetime.strptime(planjson['buildCompletedDate'], '%Y-%m-%dT%H:%M:%S.%fZ'):
            buildlist.append(Build.__init__(planjson['plan']['key'], planjson['buildNumber'], planjson['state'], datetime.strptime(planjson['buildCompletedDate'], '%Y-%m-%dT%H:%M:%S.%fZ')))
        # print(str(complettedon) + ',' + planjson['plan']['key'] + ',' + str(planjson['buildNumber']) + ',' + planjson['state'])

    while buildlist.__len__() > 0:
        earliestdate = datetime.max
        for i in range(0, buildlist.__len__()):
            if buildlist.index(i).completeddt < earliestdate:
                earliestindex = i
        completedon = buildlist.index(earliestindex).completeddt
        plankey = buildlist.index(earliestindex).key
        buildnum = buildlist.index(earliestindex).num
        buildstate = buildlist.index(earliestindex).state
        buildlist.remove(earliestindex)
        # run the voodooo
        print(str(completedon) + ',' + plankey + ',' + str(buildnum) + ',' + buildstate)


