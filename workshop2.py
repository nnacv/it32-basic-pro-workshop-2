quantity = int(input("quantity"))
cost_price = int(input("cost_price"))
sell_price = int(input("sell_price"))
team_members = int(input("team_member"))

cost = cost_price * quantity 
sell = sell_price * quantity 
total = sell - cost 
boss = ( total * 20 ) / 100
people = (( total * 80 ) / 100) / team_members

print(cost_price * quantity)
print(sell_price * quantity)
print(total)

print(boss)
print(people)
