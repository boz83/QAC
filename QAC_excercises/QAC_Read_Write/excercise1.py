teams=["Chennai Super Kings", "Mumbai Indians", "Kings XI Punjab", "Rajasthan Royals", "Sunrisers Hyderabad"]

with open('teams.txt', 'w') as f:
  for item in teams:
    f.write("%s\n" % item)

file = open('teams.txt', 'r')
output=""

for line in range(5):
  if line == 0 or line == 3:
    output+=file.readline()
  else:
    file.readline()

file.close()
print(output)