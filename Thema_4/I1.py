from datetime import datetime # Импортируем класс datetime из модуля datetime для работы с датой и временем.
from math import sqrt # Импортируем функцию sqrt из модуля math для вычисления квадратного корня.

def main(**kwargs): # функция main принимает именованные аргументы
    for key in kwargs.items(): 
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2) 
        print(result) 


if __name__ == '__main__': 
    start_time = datetime.now() 
    main( 
         one=[10, 3], 
         two=[5, 4], 
         three=[15, 13], 
         four=[93, 53], 
         five=[133, 15] 
         )
    
    time_costs = datetime.now() - start_time 
    print(f"Время выполнения программы - {time_costs}")