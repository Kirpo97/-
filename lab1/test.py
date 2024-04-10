# ПОПОВ КМ - ЛАБОРАТОРНАЯ РАБОТА 1 - SOAP-Сервисы

from zeep import Client

Services= {
    "Temperature":"https://www.w3schools.com/xml/tempconvert.asmx",
    "Continents":"http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
}

# Получение доступных категорий
def get_cat(input_services):
    print("\nДоспупные сервисы:")
    for service_name in Services:
        print(service_name)    
    print()
    if input_services == None:
        input_services = input("Введите сервис и нажмите Enter (для выхода оставте поле пустым) \n")  
    print('\nВведён метод: ', input_services)
    return input_services    

def get_method(set_services, input_method=None): 
    print("\nДоступные методы для выбранного сервиса:")
    client = Client(Services[set_services]+'?WSDL')
    services = client.service
    methods = services.__dir__()
    for method in methods:
        print(f"- {method}")
    if input_method == None:
        input_method = input("\nВведите метод: ")
    print('\nВведён метод :', input_method)
    return input_method

def init(input_services=None, input_method=None, value=None):
    try:           
        cat = get_cat(input_services)
        try:
            method = get_method(cat, input_method)
            try: 
                if value == None:  
                    value = input("Введите значение (для списка оставте поле пустым) и нажмине Enter: \n") 
                client = Client(Services[cat]+'?WSDL')            
                result = getattr(client.service, input_method)(value)   
                print('Результат: ', result)    
            except:
                client = Client(Services[cat]+'?WSDL')            
                result = getattr(client.service, method)()  
                print('Результат: ', result)        
        except:
            print("Ошибка. Метод не поддерживается.\n")
    except:
        print("Ошибка. Данные введены некоректно.\n")

if __name__ == "__main__":

    print('\nТест на запросы конвертации температуры: \n')
    init()
    init(input_services = 'Temperature')
    init(input_services = 'Temperature', input_method='CelsiusToFahrenheit', value='10')
    init(input_services = 'Temperature', input_method='FahrenheitToCelsius', value='100')
    init(input_services = 'Temperature', input_method='CelsiusToFahrenheit', value='')
    init(input_services = 'Temperature', input_method='FahrenheitToCelsius', value='')
    init(input_services = 'Temperature', input_method='123', value='55')
    init(input_services = '123', input_method='', value='')

    print('\nТест сервис континенты: \n')
    init(input_services = 'Continents', input_method='ListOfContinentsByName', value='')
    init(input_services = 'Continents', input_method='ListOfContinentsByCode', value='')
    init(input_services = 'Continents', input_method='ListOfCurrenciesByName', value='')