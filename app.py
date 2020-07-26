
friends = [
  {
    'name': 'Rolf',
    'location': 'Washington, D.C.'
  },
  {
    'name': 'Anna',
    'location': 'San Francisco'
  },
  {
    'name': 'Charlie',
    'location': 'San Francisco'
  },
  {
    'name': 'Jose',
    'location': 'San Francisco'
  },
]

user_location = input("Enter your location: ")
friends_nearby = [friend for friend in friends if friend['location'] == user_location]

if any(friends_nearby):
    print("You are not alone")
else:
    print("Sorry, No friends are near by")
