# ПОПОВ КМ - ЛАБОРАТОРНАЯ РАБОТА 2 - Распространенные форматы слабоструктурированных данных

import pandas as pd

def Convert(dataPath_1, nameFile_1, prefix_1, dataPath_2, nameFile_2, prefix_2):
    try:
        with open(dataPath_1 + nameFile_1 + prefix_1, encoding='utf-8') as file:

            # JSON to XML (1)
            if (prefix_1 == '.json') and (prefix_2 == '.xml'):    
                df = pd.read_json(dataPath_1 + nameFile_1 + prefix_1, orient = 4, encoding='utf-8')
                pd.DataFrame(df).to_xml(dataPath_2 + nameFile_2 + prefix_2)
            
            # JSON to CSV (2)
            elif (prefix_1 == '.json') and (prefix_2 == '.csv'):    
                df = pd.read_json(dataPath_1 + nameFile_1 + prefix_1, encoding='utf-8')
                pd.DataFrame(df).to_csv(dataPath_2 + nameFile_2 + prefix_2)
                
            # JSON to TCV (3)
            elif (prefix_1 == '.json') and (prefix_2 == '.tsv'):    
                df = pd.read_json(dataPath_1 + nameFile_1 + prefix_1, encoding='utf-8')
                pd.DataFrame(df).to_csv(dataPath_2 + nameFile_2 + prefix_2, sep="\t")
                
            # JSON to HTML (4)
            elif (prefix_1 == '.json') and (prefix_2 == '.html'):    
                df = pd.read_json(dataPath_1 + nameFile_1 + prefix_1, encoding='utf-8')
                pd.DataFrame(df).to_html(dataPath_2 + nameFile_2 + prefix_2)
                
            # XML to JSON (5)
            elif (prefix_1 == '.xml') and (prefix_2 == '.json'):    
                df = pd.read_xml(dataPath_1 + nameFile_1 + prefix_1, encoding='utf-8')
                pd.DataFrame(df).to_json(dataPath_2 + nameFile_2 + prefix_2, indent = 4)
            
            # XML to CSV (6)
            elif (prefix_1 == '.xml') and (prefix_2 == '.csv'):    
                df = pd.read_xml(dataPath_1 + nameFile_1 + prefix_1, encoding='utf-8')
                pd.DataFrame(df).to_csv(dataPath_2 + nameFile_2 + prefix_2)
                
            # XML to TSV (7)
            elif (prefix_1 == '.xml') and (prefix_2 == '.tsv'):    
                df = pd.read_xml(dataPath_1 + nameFile_1 + prefix_1, encoding='utf-8')
                pd.DataFrame(df).to_csv(dataPath_2 + nameFile_2 + prefix_2, sep="\t")
                
            # XML to HTML (8)
            elif (prefix_1 == '.xml') and (prefix_2 == '.html'):    
                df = pd.read_xml(dataPath_1 + nameFile_1 + prefix_1, encoding='utf-8')
                pd.DataFrame(df).to_html(dataPath_2 + nameFile_2 + prefix_2)
                
            # CSV to JSON (9)
            elif (prefix_1 == '.csv') and (prefix_2 == '.json'):    
                df = pd.read_csv(dataPath_1 + nameFile_1 + prefix_1,  encoding='utf-8')
                pd.DataFrame(df).to_json(dataPath_2 + nameFile_2 + prefix_2, indent = 4)
            
            # CSV to XML (10)
            elif (prefix_1 == '.csv') and (prefix_2 == '.xml'):    
                df = pd.read_csv(dataPath_1 + nameFile_1 + prefix_1, encoding='utf-8')
                pd.DataFrame(df).to_xml(dataPath_2 + nameFile_2 + prefix_2)
                
            # CSV to TSV (11)
            elif (prefix_1 == '.csv') and (prefix_2 == '.tsv'):    
                df = pd.read_csv(dataPath_1 + nameFile_1 + prefix_1, encoding='utf-8')
                pd.DataFrame(df).to_csv(dataPath_2 + nameFile_2 + prefix_2, sep="\t")
                
            # CSV to HTML (12)
            elif (prefix_1 == '.csv') and (prefix_2 == '.html'):    
                df = pd.read_csv(dataPath_1 + nameFile_1 + prefix_1, encoding='utf-8')
                pd.DataFrame(df).to_html(dataPath_2 + nameFile_2 + prefix_2)
                
            # TSV to JSON (13)
            elif (prefix_1 == '.tsv') and (prefix_2 == '.json'):    
                df = pd.read_csv(dataPath_1 + nameFile_1 + prefix_1,  encoding='utf-8', escapechar='\n')
                pd.DataFrame(df).to_json(dataPath_2 + nameFile_2 + prefix_2, indent = 4)
            
            # TSV to XML (14)
            elif (prefix_1 == '.tsv') and (prefix_2 == '.xml'):    
                df = pd.read_csv(dataPath_1 + nameFile_1 + prefix_1, encoding='utf-8', escapechar='\n')
                pd.DataFrame(df).to_xml(dataPath_2 + nameFile_2 + prefix_2)
                
            # TSV to CSV (15)
            elif (prefix_1 == '.tsv') and (prefix_2 == '.csv'):    
                df = pd.read_csv(dataPath_1 + nameFile_1 + prefix_1, encoding='utf-8', escapechar='\n')
                pd.DataFrame(df).to_csv(dataPath_2 + nameFile_2 + prefix_2)
                
            # TSV to HTML (16)
            elif (prefix_1 == '.tsv') and (prefix_2 == '.html'):    
                df = pd.read_csv(dataPath_1 + nameFile_1 + prefix_1, encoding='utf-8', escapechar='\n')
                pd.DataFrame(df).to_html(dataPath_2 + nameFile_2 + prefix_2)
                
            # HTML to JSON (17)
            elif (prefix_1 == '.html') and (prefix_2 == '.json'):    
                df = pd.read_html(dataPath_1 + nameFile_1 + prefix_1, encoding='utf-8')
                pd.DataFrame(df).to_json(dataPath_2 + nameFile_2 + prefix_2, indent = 4)
            
            # HTML to XML (18)
            elif (prefix_1 == '.html') and (prefix_2 == '.xml'):    
                df = pd.read_html(dataPath_1 + nameFile_1 + prefix_1, encoding='utf-8')
                pd.DataFrame(df).to_xml(dataPath_2 + nameFile_2 + prefix_2)
                
            # HTML to CSV (19)
            elif (prefix_1 == '.html') and (prefix_2 == '.csv'):    
                df = pd.read_html(dataPath_1 + nameFile_1 + prefix_1, encoding='utf-8')
                pd.DataFrame(df).to_csv(dataPath_2 + nameFile_2 + prefix_2)
                
            # HTML to TSV (20)
            elif (prefix_1 == '.html') and (prefix_2 == '.tsv'):    
                df = pd.read_html(dataPath_1 + nameFile_1 + prefix_1, encoding='utf-8')
                pd.DataFrame(df).to_csv(dataPath_2 + nameFile_2 + prefix_2)
            
            else: 
                print("\nОшибка! Данные введены некоректно!\n")        
                                    
            print("\nКонвертация ... Успех!\n")
            
    except:
        print('\nCritical error! Exit...\n')
        
if __name__ == '__main__':
   
    Convert('/home/kirill/projects/Methods-and-algorithms-for-weakly-structured-data/Methods-and-algorithms-for-weakly-structured-data/lab2/data/',
        'ex4', '.tsv', '/home/kirill/projects/Methods-and-algorithms-for-weakly-structured-data/Methods-and-algorithms-for-weakly-structured-data/lab2/data/',
            'ex4', '.json'
                )
  