from random import randint
import math

def main():
    task1();
    task4();
    task5();

def task1():
    print("Задание 1")
    print("Количество элементов в массиве: ")
    length = int(input())
    array1 = [randint(0, 10) for _ in range(length)]
    print("Массив #1",array1)
    array2 = [randint(0, 10) for _ in range(length)]
    print("Массив #2",array2)
    array3 = [abs(x - y) for x, y in zip(array1, array2)]
    print("Результат модуля разностей:",array3)
    print()
    
    

def task4():
    print("Задание 4")
    print("Количество генерируемых массивов: ")
    amount = int(input())
    print("Количество элементов в массиве: ")
    length = int(input())
    array_matrix,sum_of_array=random_array(length, amount)
    for i in range(len(array_matrix)):
        print(f"Массив #{i+1}",array_matrix[i],"Cумма элементов",sum_of_array[i])
    print("Массив с наибольшей суммой элементов",array_matrix[sum_of_array.index(max(sum_of_array))])
    print()
    
def random_array(length, amount):
    array_matrix=[]
    sum_of_array=[]
    for i in range(amount):
        array_matrix.append([randint(0, 10) for i in range(length)])
    for i in range(len(array_matrix)):
        sum_of_array.append(sum(array_matrix[i]))
    return [array_matrix,sum_of_array]



def task5():
    print("Задание 5")
    print("Первая точка: ")
    point1 = list(map(float, input().split()))
    while 1:
        print("Вторая точка: ")
        point2=list(map(float, input().split()))
        if len(point1)!=len(point2):
            print("Количество координат не совпадает с первой точкой, введите заново.")
        else:
            break
    print("Евклидово расстояние равно: ",math.sqrt(sum([(point1[i] - point2[i]) ** 2 for i in range(len(point1))])))
    print()
    
main()