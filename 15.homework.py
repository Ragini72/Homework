MI = [
{"jn":45,"p_name":"Rohit Sharma","runs":5656,"wickets":29,"t_name":"Mumbai Indians"},
{"jn":18,"p_name":"Suryakumar Yadav","runs":4567,"wickets":12,"t_name":"Mumbai Indians"},
{"jn":17,"p_name":"Ishan Kishan","runs":3456,"wickets":15,"t_name":"Mumbai Indians"},
{"jn":5,"p_name":"Kieron Pollard","runs":2345,"wickets":20,"t_name":"Mumbai Indians"},
{"jn":9,"p_name":"Jasprit Bumrah","runs":1234,"wickets":50,"t_name":"Mumbai Indians"}
]

CSK = [
{"jn":7,"p_name":"MS Dhoni","runs":4567,"wickets":12,"t_name":"Chennai Super Kings"},
{"jn":9,"p_name":"Ravindra Jadeja","runs":3456,"wickets":15,"t_name":"Chennai Super Kings"},
{"jn":18,"p_name":"Ruturaj Gaikwad","runs":2345,"wickets":20,"t_name":"Chennai Super Kings"},
{"jn":45,"p_name":"Devon Conway","runs":1234,"wickets":50,"t_name":"Chennai Super Kings"},
{"jn":17,"p_name":"Deepak Chahar","runs":5678,"wickets":29,"t_name":"Chennai Super Kings"}
]

RCB = [
{"jn":18,"p_name":"Virat Kohli","runs":7263,"wickets":4,"t_name":"Royal Challengers Bangalore"},
{"jn":33,"p_name":"Glenn Maxwell","runs":2750,"wickets":35,"t_name":"Royal Challengers Bangalore"},
{"jn":97,"p_name":"Faf du Plessis","runs":4100,"wickets":5,"t_name":"Royal Challengers Bangalore"},
{"jn":21,"p_name":"Mohammed Siraj","runs":200,"wickets":78,"t_name":"Royal Challengers Bangalore"},
{"jn":19,"p_name":"Dinesh Karthik","runs":4516,"wickets":0,"t_name":"Royal Challengers Bangalore"}
]

KKR = [
{"jn":12,"p_name":"Shreyas Iyer","runs":3200,"wickets":0,"t_name":"Kolkata Knight Riders"},
{"jn":74,"p_name":"Andre Russell","runs":2100,"wickets":96,"t_name":"Kolkata Knight Riders"},
{"jn":25,"p_name":"Sunil Narine","runs":1200,"wickets":163,"t_name":"Kolkata Knight Riders"},
{"jn":22,"p_name":"Nitish Rana","runs":2600,"wickets":8,"t_name":"Kolkata Knight Riders"},
{"jn":29,"p_name":"Varun Chakravarthy","runs":100,"wickets":62,"t_name":"Kolkata Knight Riders"}
]

RR = [
{"jn":8,"p_name":"Sanju Samson","runs":3900,"wickets":0,"t_name":"Rajasthan Royals"},
{"jn":63,"p_name":"Jos Buttler","runs":3600,"wickets":0,"t_name":"Rajasthan Royals"},
{"jn":25,"p_name":"Yuzvendra Chahal","runs":100,"wickets":187,"t_name":"Rajasthan Royals"},
{"jn":11,"p_name":"Trent Boult","runs":200,"wickets":105,"t_name":"Rajasthan Royals"},
{"jn":99,"p_name":"Shimron Hetmyer","runs":1800,"wickets":0,"t_name":"Rajasthan Royals"}
]

SRH = [
{"jn":31,"p_name":"Aiden Markram","runs":2500,"wickets":5,"t_name":"Sunrisers Hyderabad"},
{"jn":19,"p_name":"Bhuvneshwar Kumar","runs":300,"wickets":170,"t_name":"Sunrisers Hyderabad"},
{"jn":13,"p_name":"Mayank Agarwal","runs":2600,"wickets":0,"t_name":"Sunrisers Hyderabad"},
{"jn":22,"p_name":"Rahul Tripathi","runs":2200,"wickets":0,"t_name":"Sunrisers Hyderabad"},
{"jn":95,"p_name":"Umran Malik","runs":50,"wickets":40,"t_name":"Sunrisers Hyderabad"}
]

DC = [
{"jn":17,"p_name":"Rishabh Pant","runs":3000,"wickets":0,"t_name":"Delhi Capitals"},
{"jn":25,"p_name":"Axar Patel","runs":1400,"wickets":112,"t_name":"Delhi Capitals"},
{"jn":99,"p_name":"David Warner","runs":6400,"wickets":0,"t_name":"Delhi Capitals"},
{"jn":21,"p_name":"Kuldeep Yadav","runs":150,"wickets":81,"t_name":"Delhi Capitals"},
{"jn":5,"p_name":"Prithvi Shaw","runs":1700,"wickets":0,"t_name":"Delhi Capitals"}
]

PBKS = [
{"jn":42,"p_name":"Shikhar Dhawan","runs":6617,"wickets":4,"t_name":"Punjab Kings"},
{"jn":97,"p_name":"Sam Curran","runs":800,"wickets":45,"t_name":"Punjab Kings"},
{"jn":23,"p_name":"Arshdeep Singh","runs":50,"wickets":76,"t_name":"Punjab Kings"},
{"jn":54,"p_name":"Liam Livingstone","runs":1500,"wickets":20,"t_name":"Punjab Kings"},
{"jn":7,"p_name":"Jitesh Sharma","runs":900,"wickets":0,"t_name":"Punjab Kings"}
]

GT = [
{"jn":33,"p_name":"Hardik Pandya","runs":2300,"wickets":53,"t_name":"Gujarat Titans"},
{"jn":19,"p_name":"Shubman Gill","runs":3200,"wickets":0,"t_name":"Gujarat Titans"},
{"jn":6,"p_name":"Rashid Khan","runs":500,"wickets":139,"t_name":"Gujarat Titans"},
{"jn":12,"p_name":"Mohammed Shami","runs":200,"wickets":127,"t_name":"Gujarat Titans"},
{"jn":14,"p_name":"David Miller","runs":2600,"wickets":0,"t_name":"Gujarat Titans"}
]

LSG = [
{"jn":1,"p_name":"KL Rahul","runs":4200,"wickets":0,"t_name":"Lucknow Super Giants"},
{"jn":63,"p_name":"Quinton de Kock","runs":2900,"wickets":0,"t_name":"Lucknow Super Giants"},
{"jn":19,"p_name":"Marcus Stoinis","runs":1800,"wickets":40,"t_name":"Lucknow Super Giants"},
{"jn":99,"p_name":"Nicholas Pooran","runs":1600,"wickets":0,"t_name":"Lucknow Super Giants"},
{"jn":56,"p_name":"Ravi Bishnoi","runs":100,"wickets":60,"t_name":"Lucknow Super Giants"}
]

all_teams = MI + CSK + RCB + KKR + RR + SRH + DC + PBKS + GT + LSG

teams = {}
for player in all_teams:
    team = player["t_name"]

    if team not in teams:
        teams[team] = []
    teams[team].append(player["p_name"])

for team, player in teams.items():
    print("Team : ",team)
    for p in player:
        print(p)
    print()
# print(teams)
'''------------------------------'''
'''
OUTPUT :
Team :  Mumbai Indians
Rohit Sharma
Suryakumar Yadav
Ishan Kishan
Kieron Pollard
Jasprit Bumrah

Team :  Chennai Super Kings
MS Dhoni
Ravindra Jadeja
Ruturaj Gaikwad
Devon Conway
Deepak Chahar

Team :  Royal Challengers Bangalore
Virat Kohli
Glenn Maxwell
Faf du Plessis
Mohammed Siraj
Dinesh Karthik

Team :  Kolkata Knight Riders
Shreyas Iyer
Andre Russell
Sunil Narine
Nitish Rana
Varun Chakravarthy

Team :  Rajasthan Royals
Sanju Samson
Jos Buttler
Yuzvendra Chahal
Trent Boult
Shimron Hetmyer

Team :  Sunrisers Hyderabad
Aiden Markram
Bhuvneshwar Kumar
Mayank Agarwal
Rahul Tripathi
Umran Malik

Team :  Delhi Capitals
Rishabh Pant
Axar Patel
David Warner
Kuldeep Yadav
Prithvi Shaw

Team :  Punjab Kings
Shikhar Dhawan
Sam Curran
Arshdeep Singh
Liam Livingstone
Jitesh Sharma

Team :  Gujarat Titans
Hardik Pandya
Shubman Gill
Rashid Khan
Mohammed Shami
David Miller

Team :  Lucknow Super Giants
KL Rahul
Quinton de Kock
Marcus Stoinis
Nicholas Pooran
Ravi Bishnoi
'''
'''--------------------------------'''

max_runs = 0
run_player = ""

max_wickets = 0
wicket_player = ""

for player in all_teams:
    if player["runs"] > max_runs:
        max_runs = player["runs"]
        run_player = player["p_name"]

    if player["wickets"] > max_wickets:
        max_wickets = player["wickets"]
        wicket_player = player["p_name"]

print("Highest Run Scorer:", run_player, "-", max_runs)
print("Most Wickets Taker:", wicket_player, "-", max_wickets)

'''-----------------------------------------------------------
OUTPUT : 
        Highest Run Scorer: Virat Kohli - 7263
        Most Wickets Taker: Yuzvendra Chahal - 187
---------------------------------------------------------------'''


min_runs = float('inf')
min_run_player = ""

min_wickets = float('inf')
min_wicket_player = ""

for player in all_teams:
    if player["runs"] < min_runs:
        min_runs = player["runs"]
        min_run_player = player["p_name"]

    if player["wickets"] < min_wickets:
        min_wickets = player["wickets"]
        min_wicket_player = player["p_name"]

print("Lowest Run Scorer:", min_run_player, "-", min_runs)
print("Lowest Wicket Taker:", min_wicket_player, "-", min_wickets)

'''----------------------------------------------------------------
OUTPUT : 
Lowest Run Scorer: Umran Malik - 50
Lowest Wicket Taker: Dinesh Karthik - 0
--------------------------------------------------------------------'''

team_runs = {}

for player in all_teams:
    team = player["t_name"]
    runs = player["runs"]

    if team not in team_runs:
        team_runs[team] = 0

    team_runs[team] += runs

for team, total in team_runs.items():
    print(team, "Total Runs =", total)

'''----------------------------------------------
Mumbai Indians Total Runs = 17258
Chennai Super Kings Total Runs = 17280
Royal Challengers Bangalore Total Runs = 18829
Kolkata Knight Riders Total Runs = 9200
Rajasthan Royals Total Runs = 9600
Sunrisers Hyderabad Total Runs = 7650
Delhi Capitals Total Runs = 12650
Punjab Kings Total Runs = 9867
Gujarat Titans Total Runs = 8800
Lucknow Super Giants Total Runs = 10600
---------------------------------------------------'''