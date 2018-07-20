'''
hungry dice game
'''

def roll():
    from random import randint
    return randint(1,6)

def dice_game():
	strikes=0
	winnings=0
	while strikes < 3:
		die1 = roll()
		die2 = roll()
		if die1 == die2:
			strikes = strikes + 1
		else:
			winnings = winnings + die1 + die2
	return winnings

'''
clueless student problem
'''

def average_winnings(runs):
    total=0
    for n in range(runs):
        total = total + dice_game()

    return total/runs

[round(average_winnings(10000),2) for i in range(5)]


import random as r
def student(pairs, samples):
    num_correct = 0
    matching = list(range(pairs))
    for i in range(samples):
        r.shuffle(matching)
        for j in range(pairs):
            if matching[j] == j:
                num_correct = num_correct + 1
    return num_correct / samples

'''
Umbrella Quandary problem
'''

from random import random

def umbrella(p):
    wet = False
    trips = 0
    location = 0
    umbrellas = [1,1]
    while (not wet):
        if random() < p :
            if umbrellas[location] == 0:
                wet = True
            else:
                trips = trips + 1
                umbrellas[location] -= 1
                location = 1 - location
                umbrellas[location] += 1
        else:
            trips += 1
            location = 1-location
    return trips

def test():
    result = [None]*99
    p=0.01
    for i in range(99):
        trips=0
        for k in range(10000):
            trips = trips + umbrella(p)
        result[i] = trips/10000
        p=p+0.01

    return result

probability_list = test()

for j in range(1,100):
	print('The number of non-wet trips under the probability',j,'%:',probability_list[j-1])