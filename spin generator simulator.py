from random import choices
from collections import Counter

# simulates wheel spins with a 2 or 50 gold coins
def simulation(gold_coins_amount, spins_amount):
	total_earnings = 0
	samples = choices(combs_list, chances_list, k=spins_amount)
	counter_values = Counter(samples)

	if gold_coins_amount == '2 coins':

		# Loops for every combination that appeared in the 25 spins
		for comb_number in counter_values:

			# Value in cash of a combination
			comb_earning_value = earnings['2 coins'][comb_number]

			# Number of ocurrences of a combination in the 25 spins
			comb_ocurrences = counter_values[comb_number]

			earning = comb_earning_value * comb_ocurrences
			total_earnings += earning
	elif gold_coins_amount == '50 coins':

		# 50 gold coins is only 1 spin, so we just take the first and only element of the samples list
		# and add it to the total_earnings variable
		comb_number = samples[0]

		# Value in cash of a combination
		total_earnings += earnings['50 coins'][comb_number]

	return total_earnings

def amount_comparison(fifty_coins, two_coins):
	if fifty_coins > two_coins:
		return {'bigger_name': 'Fifty coins', 'bigger_wins': fifty_coins, \
				'smaller_name': 'two coins', 'smaller_wins': two_coins
		}
	else:
		return {'bigger_name': 'Two coins', 'bigger_wins': two_coins, \
				'smaller_name': 'fifty coins', 'smaller_wins': fifty_coins
		}

# comb = combination of symbols in the slot machine
earnings = {
			'2 coins': {
						'comb1': 75000,
						'comb2': 90000,
						'comb3': 105000,
						'comb4': 120000,
						'comb5': 135000,
						'comb6': 150000,
						'comb7': 187500,
						'comb8': 225000,
						'comb9': 262500,
						'comb10': 300000,
						'comb11': 375000,
						'comb12': 450000,
						'comb13': 525000,
						'comb14': 600000,
						'comb15': 675000,
						'comb16': 750000,
						'comb17': 1125000,
						'comb18': 1500000,
						'comb19': 1875000,
						'comb20': 2250000,
						'comb21': 3000000,
						'comb22': 7500000,
						'comb23': 11250000,
						'comb24': 15000000,
						'comb25': 37500000,
						'comb26': 150000000
			},
			'50 coins': {
						'comb1': 1875000,
						'comb2': 2250000,
						'comb3': 2625000,
						'comb4': 3000000,
						'comb5': 3375000,
						'comb6': 3750000,
						'comb7': 4687500,
						'comb8': 5625000,
						'comb9': 6562500,
						'comb10': 7500000,
						'comb11': 9375000,
						'comb12': 11250000,
						'comb13': 13125000,
						'comb14': 15000000,
						'comb15': 16875000,
						'comb16': 18750000,
						'comb17': 28125000,
						'comb18': 37500000,
						'comb19': 46875000,
						'comb20': 56250000,
						'comb21': 75000000,
						'comb22': 187500000,
						'comb23': 281250000,
						'comb24': 375000000,
						'comb25': 937500000,
						'comb26': 3750000000

			}
}


# chance for every possible combination
# according to https://zyngasupport.helpshift.com/a/zynga-poker/?l=en&p=all& \
# s=prizes-and-payouts&f=mega-lucky-bonus---chance-of-winning
chances = {
		'comb1': 0.05,
		'comb2': 0.065,
		'comb3': 0.065,
		'comb4': 0.07,
		'comb5': 0.075,
		'comb6': 0.1,
		'comb7': 0.1,
		'comb8': 0.0614,
		'comb9': 0.05,
		'comb10': 0.05,
		'comb11': 0.05,
		'comb12': 0.05,
		'comb13': 0.05,
		'comb14': 0.04,
		'comb15': 0.05,
		'comb16': 0.025,
		'comb17': 0.02,
		'comb18': 0.0150,
		'comb19': 0.0075,
		'comb20': 0.0050,
		'comb21': 0.0009,
		'comb22': 0.0001,
		'comb23': 0.0001,
		'comb24': 0.000009,
		'comb25': 0.0000045,
		'comb26': 0.000001
}

chances_list = []
for n in range(1, 27):
	chances_list.append(chances['comb' + str(n)])

combs_list = []
for n in range(1, 27):
	combs_list.append('comb' + str(n))

# 39 (3900%) = x40
multipliers = {'100%': 1, 'vip': 0.05, 'bonus_multiplier': 39}

# e.g.:
# (earnings value * multiplier) + earning value)
# (100 * 0.05) + 100

# how many times one amount of coins makes more earning than the other over an
# amount of samples
earning_comparison = {'50 coins': 0, '2 coins': 0, 'draws': 0}

# total samples (simulations)
for n in range(10**6):
		two_coins_earning = simulation('2 coins', 25)
		fifty_coints_earning = simulation('50 coins', 1)
		if two_coins_earning > fifty_coints_earning:
			earning_comparison['2 coins'] += 1
		elif fifty_coints_earning > two_coins_earning:
			earning_comparison['50 coins'] += 1
		elif fifty_coints_earning == two_coins_earning:
			earning_comparison['draws'] += 1

fifty_coins_wins = earning_comparison['50 coins']
two_coins_wins = earning_comparison['2 coins']
draws = earning_comparison['draws']

print('\n')
print("Total simulations: 1 million")
print('50 coins wins: {wins} ({percentage}%)'.format(
	wins=str(fifty_coins_wins), percentage=round((fifty_coins_wins/(10**6))*100, 6)))
print('2 coins wins: {wins} ({percentage}%)'.format(
	wins=str(two_coins_wins), percentage=round((two_coins_wins/(10**6))*100, 6)))
print('Draws: ' + str(draws))

amount = amount_comparison(fifty_coins_wins, two_coins_wins)
print("{bigger_name} had {percentage}% more wins than {smaller_name}.".format(
	bigger_name=amount['bigger_name'], 
	percentage=round(((amount['bigger_wins'] - amount['smaller_wins']) / amount['smaller_wins']) * 100, 6),
	smaller_name=amount['smaller_name']
	)
)