import yaml                                                                      
from dataclasses import dataclass, field                                
from typing import List
import matplotlib.pyplot as plt

# Создаём структуру   
@dataclass                                                
class Value:
    date: List[str] = field(default_factory=list)                                                   
    val: List[int] = field(default_factory=list)  
    
# Парсим файл    
def parse_yaml_file(path:str): 
    with open(path, 'r') as stream:
        yaml_file = yaml.safe_load(stream)

    # Наполняем структуру содержимым файла
    week = yaml_file['weather']
    dey = [(date) for date in week]
    temp = [(week[val]) for val in week]
    return Value(date=dey, val=temp)

# Выводим график из заполненной структуры
def plot_weather(object):
    dey = object.date
    val = object.val
    plt.plot(dey, val)                                               
    plt.xlabel('Дата')                                                     
    plt.ylabel('Среднее значения параметра "Влажность полотна"')                                                       
    plt.show() 
    
path = '/home/kirill/projects/Methods-and-algorithms-for-weakly-structured-data/Methods-and-algorithms-for-weakly-structured-data/lab3/weather.yaml'
parsed_data = parse_yaml_file(path)   
plot_weather(parsed_data)