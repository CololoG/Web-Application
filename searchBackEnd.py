searchInput = input("what do you want to search for? ")

output = ""

# Search for a user inside a database
for user in len(database):
  # If the search input matches the user inside the database then display the user
  if searchInput == user:
    output = user
    print("user " + user + " was found!")
    
    # If the user was not found then display that the user was not found
  else:
    output = "user was not found!"
