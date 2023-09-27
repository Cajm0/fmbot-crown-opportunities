import requests

session1 = requests.Session()
talist = []
k=0
m=0

user = [] #removed for anonymity - enter your last.fm username here (or someone elses)

otheruser = [] #removed for anonymity - enter the last.fm usernames of other people using fmbot on the server here


limit = 600

for i in user:
    #requires API key in below line to function
    ta = session1.get(f"https://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user={i}&api_key={API KEY}&format=json&limit={limit}").json()

    for j in ta['topartists']['artist']:
        if int(j['playcount']) > 29:
            if j['name'] not in talist:
                talist.append(j['name'])
            k+=1
    print(i, k)
    k=0

for i in otheruser:
    #requires API key in below line to function
    ta = session1.get(f"https://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user={i}&api_key={API KEY}&format=json&limit={limit}").json()

    for j in ta['topartists']['artist']:
        if int(j['playcount']) > 29:
            if j['name'] in talist:
                talist.remove(j['name'])
            m+=1
    print(i, m)
    m=0

talist = sorted(talist)
print(talist)

checked = []

for i in talist:
    if i in checked:
        pass
    else:
        print('.w', i)

