events = int(input('\nAmount of events: '))
varieties = int(input('Amount of results in each event: '))
bet = int(input('Bet amount: '))
currency = str(input('Write your currency: '))

combinations = events * pow(varieties, events)

print('\nAmount of combinations: ', combinations)
print('\nRequired amount: ', combinations * bet, currency)
