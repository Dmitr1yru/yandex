import random
import os


def neuralnet (inp, weights):
	result = [0, 0, 0]
	for i in range(len(weights)):
		result[i] = w_sum(inp, weights[i])
	return result

def w_sum (a, b):
	result = 0
	for i in range(len(a)):
		result = result + a[i] * b[i]
	return result

inp = [0, 0, 0]
weights = [[0, 0, 0],
		   [0, 0, 0],
		   [0, 0, 0]]
sience_obj = [0, 0, 0]

while True:

	print('')
	print('|----------WELCOME----------|')
	print('Select protocol: NOII - none output inference information')
	print('Select protocol: AOII - avialable output inference information')
	print('Select protocol:   - close programm')
	print('')

	mode = input('PROTOCOL ---> ')
	print('')
	if mode == 'NOII' or mode == 'AOII':
		alpha = float(input('ALPHA ---> '))
		print('')
		inp[0] = float(input('1INPUT ---> '))
		inp[1] = float(input('2INPUT ---> '))
		inp[2] = float(input('3INPUT ---> '))
		print('')
		sience_obj[0] = float(input('1RIGHT ANSWER ---> '))
		sience_obj[1] = float(input('2RIGHT ANSWER ---> '))
		sience_obj[2] = float(input('3RIGHT ANSWER ---> '))
		print('')
		weights[0][0] = round(random.uniform(0, 2), 1)
		weights[0][1] = round(random.uniform(0, 2), 1)
		weights[0][2] = round(random.uniform(0, 2), 1)
		weights[1][0] = round(random.uniform(0, 2), 1)
		weights[1][1]= round(random.uniform(0, 2), 1)
		weights[1][2] = round(random.uniform(0, 2), 1)
		weights[2][0] = round(random.uniform(0, 2), 1)
		weights[2][1] = round(random.uniform(0, 2), 1)
		weights[2][2] = round(random.uniform(0, 2), 1)
		print('random weights claster №1 =', weights[0])
		print('random weights claster №2 =', weights[1])
		print('random weights claster №3 =', weights[2])
		print('')
		iterations = int(input('ITERATION ---> '))
		print('')


		for iternum in range(iterations):
			neuralnet_answer = neuralnet(inp, weights)
			weight_delta = [0, 0, 0]
			delta = [0, 0, 0]
			error = [0, 0, 0]
			weight_delta = [[0, 0, 0],
							[0, 0, 0],
							[0, 0, 0]]


			for i in range(len(sience_obj)):
				delta[i] = neuralnet_answer[i] - sience_obj[i]
				error[i] = delta[i] ** 2
				for j in range(len(delta)):
					weight_delta[i][j] = inp[j] * delta[i]
			if mode == 'AOII':
				print('ITERATION', iternum)
				print('ANSWER', neuralnet_answer)
				print('ERROR', error)
				print('WEIGHT', weights)
				print('WEIGHT DELTA', weight_delta, "\n")

			for i in range(len(weights)):
				for j in range(len(weights[0])):
					weights[i][j] = weights[i][j] - weight_delta[i][j] * alpha

		print('')
		print('--------------finish--------------')
		print('')
		print('INPUT:', inp)
		print('WEIGHT:', weights) 
		print('FINAL ERROR:', error)
		print('NEUROanswer:', neuralnet(inp, weights), '/ sience obj:', sience_obj)
		clear = input('Clear? Y/N ---> ')
		if clear == 'Y' or clear == 'y':
			os.system('cls')
	else:
		break