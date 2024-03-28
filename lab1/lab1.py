# ПОПОВ КМ - ЛАБОРАТОРНАЯ РАБОТА 1 - SOAP-Сервисы

'''
curl --location 'https://www.dataaccess.com/webservicesserver/NumberConversion.wso' \
--header 'Content-Type: text/xml; charset=utf-8' \
--data '<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <NumberToWords xmlns="http://www.dataaccess.com/webservicesserver/">
      <ubiNum>500</ubiNum>
    </NumberToWords>
  </soap:Body>
</soap:Envelope>'
'''

from zeep import Client

Services= {
    "Temperature":"https://www.w3schools.com/xml/tempconvert.asmx",
    "Continents":"http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
}

# Получение доступных категорий
def get_cat():
    print("\nДоспупные сервисы:")
    for service_name in Services:
        print(service_name)    
    print()
    set_services = input("Введите сервис и нажмите Enter (для выхода оставте поле пустым) \n")    
    return set_services    

def get_method(set_services): 
    print("\nДоступные методы для выбранного сервиса:")
    client = Client(Services[set_services]+'?WSDL')
    services = client.service
    methods = services.__dir__()
    for method in methods:
        print(f"- {method}")
    method = input("\nВведите метод: ")
    return method


if __name__ == "__main__":
       
    try:           
        cat = get_cat()
        try:
            method = get_method(cat)
            try: 
                param = input("Введите значение (для списка оставте поле пустым) и нажмине Enter: \n") 
                client = Client(Services[cat]+'?WSDL')            
                result = getattr(client.service, method)(param)   
                print('Результат: ', result)    
            except:
                client = Client(Services[cat]+'?WSDL')            
                result = getattr(client.service, method)()  
                print('Результат: ', result)        
        except:
            print("Ошибка. Метод не поддерживается.\n")
    except:
        print("Ошибка. Данные введены некоректно.\n")
    
    
        '''client = Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL')            
        result = getattr(client.service, 'ListOfContinentsByName')()
        print(result)'''

    
  
    
 
