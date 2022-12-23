import numpy as np
import random

#Задание 1
data = open('var1.txt')
i=0
X=[]
for line in data:
    if i==0:
        N=float((line.split())[0])
        i+=1
        X=np.zeros((int(N),int(N)))
        continue
    j=0
    for number in line.split():
        X[i-1][j]=float(number)
        j+=1
    i+=1

l = list(range(1, int(N+1)))

#print(l)
#Задание 2
def F(list_of_cities_array):
    '''list_of_cities_array=[]
    for number in list_of_cities.split():
        list_of_cities_array.append(int(number))'''
    sum=0
    if len(list_of_cities_array)==2:
        sum = X[list_of_cities_array[len(list_of_cities_array) - 1]-1, list_of_cities_array[0]-1]
    else:
        for i in range(len(list_of_cities_array)-1):
            sum+=X[list_of_cities_array[i]-1,list_of_cities_array[i+1]-1]
        sum+=X[list_of_cities_array[len(list_of_cities_array)-1]-1,list_of_cities_array[0]-1]
    return sum
#Задание 3

def mutation(list_of_cities_array):
    '''list_of_cities_array = []
    N=len(list_of_cities)
    for number in list_of_cities.split():
        list_of_cities_array.append(int(number))'''
    N = len(list_of_cities_array)
    rand_1 = random.randint(0, N-1)
    number=list_of_cities_array[rand_1]
    list_of_cities_array.remove(list_of_cities_array[rand_1])
    while 1:
        rand_2 = random.randint(0, N-1)
        if (rand_1!=rand_2):
            break
    list_of_cities_array.insert(rand_2,number)
    return list_of_cities_array

#Задание 4
def two_neighbour(list,index):
    if (F([list[index%len(list)],list[(index+1)%len(list)]])<F([list[index%len(list)],list[(index-1)%len(
            list)]])):
        result=list[(index+1)%len(list)]
        index=index+1
    else:
        result=list[(index-1)%len(list)]
        index = index - 1
    return result,index

def one_neighbour(list,index):
    return list[index%len(list)],index

def no_neighbours(list,unusedcities,index):
    cost = []
    cost_i = []
    for i in unusedcities:
        cost.append(F([list[index%len(list)], i]))
        cost_i.append(i)
    result = cost_i[cost.index(min(cost))]
    return result,list.index(result)

def crossing_over(list1,list2):
    result=[]
    index=random.randint(0,len(list1)-1)
    current_parent=0
    unusedcities=[]
    unusedcities.extend(list1)
    result.append(list1[index])
    unusedcities.remove(list1[index])
    while len(unusedcities)>=2:
        if current_parent==0:
            if list1[(index+1)%len(list1)] in unusedcities and list1[(index-1)%len(list1)] in unusedcities:
                res,index=two_neighbour(list1,index)
                result.append(res)
                unusedcities.remove(result[-1])
                current_parent=not current_parent
            elif list1[(index+1)%len(list1)] in unusedcities and list1[(index-1)%len(list1)] not in unusedcities:
                res, index = one_neighbour(list1, index+1)
                result.append(res)
                unusedcities.remove(result[-1])
                current_parent = not current_parent
            elif list1[(index-1)%len(list1)] in unusedcities and list1[(index+1)%len(list1)] not in unusedcities:
                res, index = one_neighbour(list1, index-1)
                result.append(res)
                unusedcities.remove(result[-1])
                current_parent = not current_parent
            else:
                res,index=no_neighbours(list1, unusedcities, index)
                result.append(res)
                unusedcities.remove(result[-1])
                current_parent = not current_parent
        else:
            if list2[(index+1)%len(list1)] in unusedcities and list2[(index-1)%len(list1)] in unusedcities:
                res, index = two_neighbour(list2, index)
                result.append(res)
                unusedcities.remove(result[-1])
                current_parent = not current_parent
            elif list2[(index+1)%len(list1)] in unusedcities and list2[(index-1)%len(list1)] not in unusedcities:
                res, index = one_neighbour(list2, index + 1)
                result.append(res)
                unusedcities.remove(result[-1])
                current_parent = not current_parent
            elif list2[(index-1)%len(list1)] in unusedcities and list2[(index+1)%len(list1)] not in unusedcities:
                res, index = one_neighbour(list2, index - 1)
                result.append(res)
                unusedcities.remove(result[-1])
                current_parent = not current_parent
            else:
                res, index = no_neighbours(list2, unusedcities, index)
                result.append(res)
                unusedcities.remove(result[-1])
                current_parent = not current_parent
    result.append(unusedcities[-1])
    return result

def sort(population):
    population.sort(key=lambda i: F(i) )
    return population

def main():
    number_of_individuals = 100  # Количество особей
    probability_of_mutation = 0.9  # Вероятность мутации
    number_of_crosses = 20  # Количество скрещиваний
    number_of_GA=100
    population = []
    # TODO: Раскомментировать цикл и убрать population
    for i in range(0,number_of_individuals):
        pop = list(range(1, len(X)+1))
        random.shuffle(pop)
        population.append(pop)
    distance = []
    population = sort(population)
    for i in population:
        print('Путь: %s, Длиной: %f' % (i, F(i)))
        distance.append(F(i))
    print()
    min_distance=min(distance)
    min_population=population[distance.index(min(distance))]
    print('Минимальная длина: %f, Путь:%s \n' % (min_distance, min_population))
    for i in range(number_of_GA):
        for j in range(number_of_crosses):
            a,b=random.randint(1,len(population)-1),random.randint(1,len(population)-1)
            while True:
                if a!=b:
                    break
                else:
                    a, b = random.randint(0, len(population) - 1), random.randint(0, len(population) - 1)
            population_cross=crossing_over(population[a],population[b])
            if F(population_cross)<min_distance:
                population[len(population)-1]=population_cross
                population=sort(population)
                min_distance=F(population[0])
                min_population=population[0]
                print(min_distance)
                break
            if random.random()<probability_of_mutation:
                for item in range(1,len(population)-2):
                    population[item]=mutation(population[item])
                    if F(population[item]) < min_distance:
                        population[len(population) - 1] = population[item]
                        population=sort(population)
                        min_distance=F(population[0])
                        min_population=population[0]
                        print(min_distance)
    print("Результат работы генетического алгоритма:",min_population)
    print("Длина пути:", min_distance)

main()
