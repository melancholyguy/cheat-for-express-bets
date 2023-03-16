import math

events = int(input('\nAmount of events: '))
varieties = int(input('Amount of results in each event: '))
bet = int(input('Bet amount: '))
currency = str(input('Write your currency: '))

combinations = math.factorial(events) // (math.factorial(events - varieties) * math.factorial(varieties))

print('\nAmount of combinations: ', combinations)
print('\nRequired amount: ', combinations * bet, currency)
