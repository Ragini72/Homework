movies_db = {}

movies_db["Chhava"] = ["Vicky Kaushal", "Rashmika Mandanna", "Akshaye Khanna"]
movies_db["Fighter"] = ["Hrithik Roshan", "Deepika Padukone", "Anil Kapoor"]
movies_db["Pushpa 2"] = ["Allu Arjun", "Rashmika Mandanna", "Fahadh Faasil"]
movies_db["Kalki 2898 AD"] = ["Prabhas", "Deepika Padukone", "Amitabh Bachchan"]
movies_db["Dhurandhar"] = ["Akshaye Khanna","Ranveer Singh", "Sanjay Dutt", "R. Madhavan"]
movies_db["Singham Again"] = ["Ajay Devgn", "Kareena Kapoor", "Akshay Kumar"]

# print(movies_db.keys())         #dict_keys(['Chhava', 'Fighter', 'Pushpa 2', 'Kalki 2898 AD', 'Dhurandhar', 'Singham Again'])
# print(movies_db.values())   

print(movies_db["Dhurandhar"][0])
i = movies_db.get("Dhurandhar")
print(i[0])

print(movies_db.get("Dhurandhar")[0][5])

# actor_count = {}

# for actors in movies_db.values():
#     for actor in actors:
#         if actor in actor_count:
#             actor_count[actor] += 1
#         else:
#             actor_count[actor] = 1

# print(actor_count)