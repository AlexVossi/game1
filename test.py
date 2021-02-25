from territory import Territory

new_land =  Territory("New Land","red")
sater = Territory("sater", "red")


new_land.takeover("player1")
sater.takeover("player2")
new_land.add_troops(6)
sater.add_troops(3)