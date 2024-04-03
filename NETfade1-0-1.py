import random
def neuralnet (inp, weights):
	return inp * weights

print('----------WELCOME----------')
inp = float(input('INPUT ---> '))
sience_obj = float(input('RIGHT ANSWER ---> '))
alpha = float(input('ALPHA ---> '))
weights = round(random.uniform(0, 2), 1)
print('random weights =', weights)
iterations = int(input('ITERATION ---> '))


for i in range(iterations):
	neuralnet_answer = neuralnet(inp, weights)
	error = (neuralnet_answer - sience_obj) ** 2
	direction_and_amount = (neuralnet_answer - sience_obj) * inp
	weights = weights - direction_and_amount * alpha
	print('error:', error, 'result:', neuralnet_answer)


print('--------------finish--------------')
print('INPUT:', inp)
print('Weight:', weights)
print('NEUROanswer:', neuralnet(inp, weights), '/ sience obj:', sience_obj)
input()