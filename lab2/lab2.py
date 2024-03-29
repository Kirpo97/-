# ПОПОВ КМ - ЛАБОРАТОРНАЯ РАБОТА 2 - Распространенные форматы слабоструктурированных данных

import json
import xmltodict
import pandas as pd
import html_to_json

def WriteFile(File_2, dataPath_2, nameFile_2, prefix_2):
    f = open(dataPath_2 + nameFile_2 + prefix_2, 'w')
    f.write(File_2)
    f.close()  
    
def JSON_to_XML(file):
    File_1 = json.load(file)
    return xmltodict.unparse(File_1) 
        
def XML_to_CSV(file):
    File_1 = xmltodict.parse(file.read())
    return pd.DataFrame(File_1)

def CSV_to_TSV(dataPath_1, nameFile_1, prefix_1):
    File_1 = pd.read_csv(dataPath_1 + nameFile_1 + prefix_1, escapechar='\n')
    return pd.DataFrame(File_1)

def TSV_to_HTML(dataPath_1, nameFile_1, prefix_1, dataPath_2, nameFile_2, prefix_2):
    File_1 = pd.read_csv(dataPath_1 + nameFile_1 + prefix_1)
    return File_1.to_html()

def HTML_to_JSON(file):
    html_file = file.read()
    return html_to_json.convert(html_file) 
        
def Convert(dataPath_1, nameFile_1, prefix_1, dataPath_2, nameFile_2, prefix_2):
    with open(dataPath_1 + nameFile_1 + prefix_1, encoding='utf-8') as file:
        
        if (prefix_1 == '.json') and (prefix_2 == '.xml'):     # JSON to XML (1)
            File_2 = JSON_to_XML(file, dataPath_2, nameFile_2, prefix_2)
            WriteFile(File_2, dataPath_2, nameFile_2, prefix_2)
            
        if (prefix_1 == '.xml') and (prefix_2 == '.csv'):      # XML to CSV (2)
            File_2 = XML_to_CSV(file)
            File_2.to_csv( dataPath_2 + nameFile_2 + prefix_2, encoding='utf-8', index=False)
        
        if (prefix_1 == '.csv') and (prefix_2 == '.tsv'):      # CSV to TSV (3)   
            File_2 = CSV_to_TSV(dataPath_1, nameFile_1, prefix_1)
            File_2.to_csv( dataPath_2 + nameFile_2 + prefix_2, sep='\t', encoding='utf-8', index=False )
        
        if (prefix_1 == '.tsv') and (prefix_2 == '.html'):    # TSV to HTML (4)
            File_2 = TSV_to_HTML(dataPath_1, nameFile_1, prefix_1, dataPath_2, nameFile_2, prefix_2)
            WriteFile(File_2, dataPath_2, nameFile_2, prefix_2)
            
        if (prefix_1 == '.html') and (prefix_2 == '.json'):   # HTML to JSON (5)    
            File_2 = HTML_to_JSON(file)
            out_file = open(dataPath_2 + nameFile_2 + prefix_2, "w")
            json.dump(File_2, out_file, indent = 2) 
            out_file.close() 
            
        if (prefix_1 == '.xml') and (prefix_2 == '.csv'): # XML to CSV (6)
           pass

        if (prefix_1 == '.xml') and (prefix_2 == '.tsv'): # XML to TSV (7)
            pass
           
        if (prefix_1 == '.xml') and (prefix_2 == '.html'): # XML to HTML (8)
            pass    
            
        if (prefix_1 == '.csv') and (prefix_2 == '.json'): # CSV to JSON (9)
            pass     
        
        if (prefix_1 == '.csv') and (prefix_2 == '.xml'): # CSV to XML (10)
           pass
       
        if (prefix_1 == '.csv') and (prefix_2 == '.tsv'):  # CSV to TSV (11)
            pass
        
        # CSV to HTML (12)

        
        print("\nКонвертация ... Успех!\n")     
            
                

''' 


# CSV to HTML (12)
import pandas as pd
def CSV_to_HTML(): 
    df1 = pd.read_csv('student_details.csv')
    print("The dataframe is:")
    print(df1)
    html_string = df1.to_html()
    print("The html string is:")
    print(html_string)

# TSV to JSON (13)
import csv
import json
import collections
def TSV_to_JSON(): 
    OrderedDict = collections.OrderedDict
    src = '/tmp/data.log'
    dst = '/tmp/data.json'
    header = [
        'date', 'time', 'time_taken', 'c_ip', 'cs_username', 'cs_auth_group',
        'x_exception_id', 'sc_filter_result', 'cs_categories', 'cs_Referer',
        'sc_status', 's_action', 'cs_method', 'rs_Content_Type', 'cs_uri_scheme',
        'cs_host', 'cs_uri_port', 'cs_uri_path', 'cs_uri_query',
        'cs_uri_extension', 'cs_User_Agent', 's_ip', 'sc_bytes', 'cs_bytes',
        'x_virus_id'
    ]
    data = []
    with open(src, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='"')
        for row in reader:
            if row[0].strip()[0] == '#':  #
                continue
            row = filter(None, row)
            data.append(OrderedDict(zip(header, row)))
    with open(dst, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)

# TSV to CSV (14)
import pandas as pd 
def TSV_to_CSV(): 
    tsv_file='name.tsv'
    csv_table=pd.read_table(tsv_file,sep='\t')
    csv_table.to_csv('new_name.csv',index=False)

# TSV to XML (15)
from collections import defaultdict
from xml.etree.ElementTree import Element, SubElement,ElementTree
def TSV_to_XML(): 
    data = defaultdict(list)
    with open('in.txt') as f:
    next(f)
    for line in f:
        parts = line.split(',')
        data[parts[0]].append(parts[1].strip())
    root = Element('root')
    for k,v in data.items():
    sub = SubElement(root,'coupon-codes',attrib={'coupon-id':k})
    for vv in v:
        sub_v = SubElement(sub,'code')
        sub_v.text = vv
    tree = ElementTree(root)
    with open('out.xml', 'w') as f:
    tree.write(f, encoding='unicode')

# TSV to HTML (16)
def TSV_to_HTML(): 
    df = pd.read_csv("myfile.csv")
    df.to_html('your_file.html')

# HTML to JSON (17)
import json
import codecs
def HTML_to_JSON(): 
    # Load the JSON file by specifying the location and filename
    with codecs.open(filename="json_file.json", mode="r", encoding="utf-8") as jsonf:
        json_file = json.loads(jsonf.read())
    # Load the HTML file by specifying the location and filename
    with codecs.open(filename="html_file.html", mode='r', encoding="utf-8") as htmlf:
        html_file = htmlf.read()
    # Chose the key name where the HTML source code will live as a string
    json_file['Key1']['Key2'] = html_file
    # Dump the dictionary to JSON object and save it in a specific location 
    json_object = json.dumps(json_file, indent=4)
    with codecs.open(filename="final_json_file.json", mode="w", encoding="utf-8") as ojsonf:
        ojsonf.write(json_object)

# HTML to CSV (18)
from bs4 import BeautifulSoup
import urlopen as urllib2
import csv
def HTML_to_CSV(): 
    url = 'http://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s3_en.php?block_no=47401&view=1'
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    table = soup.select_one("table.data2_s")
    # python3 just use th.text
    headers = [th.text.encode("utf-8") for th in table.select("tr th")]
    with open("out.csv", "w") as f:
        wr = csv.writer(f)
        wr.writerow(headers)
        wr.writerows([[td.text.encode("utf-8") for td in row.find_all("td")] for row in table.select("tr + tr")])

# HTML to TSV (19)

# HTML to XML (20)
from lxml import html, etree 
def HTML_to_XML(): 
    file = "input.html"
    with open(file, 'r', encoding='utf-8') as inp: 
        htmldoc = html.fromstring(inp.read()) 
    with open("output.xml", 'wb') as out: 
        out.write(etree.tostring(htmldoc))
'''

if __name__ == '__main__':
   

  Convert('/home/kirill/projects/Methods-and-algorithms-for-weakly-structured-data/Methods-and-algorithms-for-weakly-structured-data/lab2/data/',
      'example', '.html', '/home/kirill/projects/Methods-and-algorithms-for-weakly-structured-data/Methods-and-algorithms-for-weakly-structured-data/lab2/data/',
          'example', '.json'
              )
  
  
  