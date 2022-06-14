import numpy as np
from statistics import mean
import random
import sys
import string


	

def binaryToDecimal(val): 
    return int(val, 2) 


def DecimalTobinary(val):
    return format(val, "05b")


def pop_fitness(val):
	return val**2


def Prob(val,x):
	return val[x]/sum(val)


def Expect(val,x):
	avg=sum(val)/len(val)
	return val[x]/avg


def Mating_pool(cromozoms):
	cross_over=0
	cromozom1=cromozoms[0]
	cromozom2=cromozoms[1]
	cross_over=random.randint(1,3)
	return cromozom2[:cross_over] + cromozom1[cross_over:],cromozom1[:cross_over] + cromozom2[cross_over:],cross_over




population=[]
fitness=[]
probability=[]
expected_count=[]
num_of_pop=4
cromozoms=[]
c=0
new_pop=[]
decimal_pop=[]
crossoverpoint=[]
sum_of_fitness=0
max_of_fitness=0
true=1

for i in range(0,32):
	population.append(DecimalTobinary(i))
	fitness.append(pop_fitness(i))

persons=random.sample(range(32),4)

while true==1:
	
	for x in range(num_of_pop):
		person=persons[x]
		probability.append(Prob(fitness,person))  
		expected_count.append(Expect(fitness,person))
		print('cromozom ',person,': ',population[person],'/ fitness: ',fitness[person],'/ probability: ',probability[x],'/ expected_count: ',expected_count[x])
		cromozoms.append(population[person])
		sum_of_fitness+=fitness[person]
		if max_of_fitness<=fitness[person]:
			max_of_fitness=fitness[person]
		c+=1
		if c==2:
			cro1,cro2,cross=Mating_pool(cromozoms)
			new_pop.append(cro2)
			new_pop.append(cro1)
			crossoverpoint.append(cross)
			cromozoms=[]
			c=0

	
	print('\nSum of fitness:',sum_of_fitness)
	sum_of_fitness=0
	print('\navg of fitness:',sum_of_fitness/4)
	print('\nMax of fitness:',max_of_fitness)
		
	
	if max_of_fitness==961:
		true=0
	else:
		print('\ncroosover point are:',crossoverpoint)	
		print('new population with crossover:(binary) ',new_pop)
		for z in range(0,len(new_pop)):
			decimal_pop.append(binaryToDecimal(new_pop[z]))
		print('new population with croosover:(decimal) ',decimal_pop)
		crossoverpoint=[]
		persons=[]
		new_pop=[]
		persons=decimal_pop
		max_of_fitness=0
		decimal_pop=[]
		print('\n_________________________________________________________________________________________________\n')
