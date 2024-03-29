# ПОПОВ КМ - ЛАБОРАТОРНАЯ РАБОТА 2 - Распространенные форматы слабоструктурированных данных

import json
import xmltodict
import pandas as pd
import csv

def Convert(dataPath_1, nameFile_1, prefix_1, dataPath_2, nameFile_2, prefix_2):
    with open(dataPath_1 + nameFile_1 + prefix_1, encoding='utf-8') as file:
        
        if (prefix_1 == '.json') and (prefix_2 == '.xml'):
            File_1 = json.load(file)
            File_2 = xmltodict.unparse(File_1)
            xml = open(dataPath_2 + nameFile_2 + prefix_2, 'w')
            xml.write(File_2)
            xml.close()            
            
        if (prefix_1 == '.json') and (prefix_2 == '.csv'):
            File_1 = pd.read_json(file)
            File_1.to_csv(dataPath_2 + nameFile_2 + prefix_2, encoding='utf-8', index=False)
            
        if (prefix_1 == '.json') and (prefix_2 == '.tsv'):    
            File_1 = csv.DictWriter(dataPath_2 + nameFile_2 + prefix_2, sorted(file[0].keys()), delimiter='\t')
            File_1.writeheader()
            File_1.writerows(file)
            
            asd
        print("Конвертация ... Успех!")     
            
        '''               
                
            if (prefix_1 == '.json') and (prefix_2 == 'xml'):
                
                
            if (prefix_1 == '.json') and (prefix_2 == 'xml'):
                
            
            if (prefix_1 == '.json') and (prefix_2 == 'xml'):
            
            
            if (prefix_1 == '.json') and (prefix_2 == 'xml'):
                
            
            if (prefix_1 == '.json') and (prefix_2 == 'xml'):
                
                
            if (prefix_1 == '.json') and (prefix_2 == 'xml'):
                
                
            if (prefix_1 == '.json') and (prefix_2 == 'xml'):
                
                
            if (prefix_1 == '.json') and (prefix_2 == 'xml'):
                
            
            if (prefix_1 == '.json') and (prefix_2 == 'xml'):
                
                
            if (prefix_1 == '.json') and (prefix_2 == 'xml'):
                
                
            if (prefix_1 == '.json') and (prefix_2 == 'xml'):
                
                
            if (prefix_1 == '.json') and (prefix_2 == 'xml'):
                
            
            if (prefix_1 == '.json') and (prefix_2 == 'xml'):
            
            
            if (prefix_1 == '.json') and (prefix_2 == 'xml'):
                
            
            if (prefix_1 == '.json') and (prefix_2 == 'xml'):
                
                
            if (prefix_1 == '.json') and (prefix_2 == 'xml'):
                
                
            if (prefix_1 == '.json') and (prefix_2 == 'xml'):
                
                
            if (prefix_1 == '.json') and (prefix_2 == 'xml'):
                    '''
                    

''' 
# JSON to TSV (3)

import pandas as pd
def JSON_to_TSV():
    table = pd.read_json('...', orient='records')
    table.to_csv(sys.stdout, sep='\t', index=False)

# JSON to HTML (4)
import json2html
def JSON_to_HTML():
    infoFromJson = json.loads('jsonfile')
    print(json2html.convert(json = infoFromJson)) 

# XML to JSON (5)
from xml.dom import minidom
import simplejson as json
def XML_to_JSON(element):
    dict_data = dict()
    if element.nodeType == element.TEXT_NODE:
        dict_data['data'] = element.data
    if element.nodeType not in [element.TEXT_NODE, element.DOCUMENT_NODE, 
                                element.DOCUMENT_TYPE_NODE]:
        for item in element.attributes.items():
            dict_data[item[0]] = item[1]
    if element.nodeType not in [element.TEXT_NODE, element.DOCUMENT_TYPE_NODE]:
        for child in element.childNodes:
            child_name, child_dict = parse_element(child)
            if child_name in dict_data:
                try:
                    dict_data[child_name].append(child_dict)
                except AttributeError:
                    dict_data[child_name] = [dict_data[child_name], child_dict]
            else:
                dict_data[child_name] = child_dict 
    return element.nodeName, dict_data

# XML to CSV (6)
import xml.etree.ElementTree as Xet 
import pandas as pd 
def XML_to_CSV():
    xmlparse = Xet.parse('sample.xml') 
    root = xmlparse.getroot() 
    for i in root: 
        name = i.find("name").text 
        phone = i.find("phone").text 
        email = i.find("email").text 
        date = i.find("date").text 
        country = i.find("country").text 
        rows.append({"name": name, 
                    "phone": phone, 
                    "email": email, 
                    "date": date, 
                    "country": country}) 
    df = pd.DataFrame(rows, columns=cols) 
    df.to_csv('output.csv') 

# XML to TSV (7)
from xml.etree import ElementTree
def XML_to_TSV():
    file = 'sample.xml'
    tree = ElementTree.parse(file)
    root = tree.getroot()
    for sentence in root.iter('sentence'):
        for opinion in sentence.iter('Opinion'):
            print([opinion.attrib['polarity'], sentence.find('text').text, opinion.attrib['category']])

# XML to HTML (8)
import aspose.pdf as ap
def XML_to_HTML(self, infile, outfile):
        path_infile = self.dataDir + infile
        path_outfile = self.dataDir + outfile
        options = ap.XmlLoadOptions("template.xslt")
        # Open XML document
        document = ap.Document(path_infile, options)
        option = ap.HtmlSaveOptions()
        document.Save(path_outfile, option)
        print(infile + " converted into " + outfile)

# CSV to JSON (9)
import csv
import json
def CSV_to_JSON():
    csvfile = open('file.csv', 'r')
    jsonfile = open('file.json', 'w')
    fieldnames = ("FirstName","LastName","IDNumber","Message")
    reader = csv.DictReader( csvfile, fieldnames)
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')

# CSV to XML (10)
import csv  
import pandas as pd
def CSV_to_XML():        
    f = open('movies2.csv')
    csv_f = csv.reader(f)   
    data = []

    for row in csv_f: 
        data.append(row)
    f.close()

    df = pd.read_csv('movies2.csv')
    header= list(df.columns)

    def convert_row(row):
        str_row = """<%s>%s</%s> \n"""*(len(header)-1)
        str_row = """<%s>%s""" +"\n"+ str_row + """</%s>"""
        var_values = [list_of_elments[k] for k in range(1,len(header)) for list_of_elments in [header,row,header]]
        var_values = [header[0],row[0]]+var_values+[header[0]]
        var_values =tuple(var_values)
        return str_row % var_values

    text ="""<collection shelf="New Arrivals">"""+"\n"+'\n'.join([convert_row(row) for row in data[1:]])+"\n" +"</collection >"
    print(text)
    with open('output.xml', 'w') as myfile: 
        pass
    #    myfile.write(text)

# CSV to TSV (11)
def CSV_to_TSV(): 
    df = pd.read_csv(r'a.csv', escapechar='\n')
    df.to_csv('data.tsv', sep='\t', encoding='utf-8', index=False)

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
      'menu', '.json', '/home/kirill/projects/Methods-and-algorithms-for-weakly-structured-data/Methods-and-algorithms-for-weakly-structured-data/lab2/data/',
          'menu', '.tsv'
              )
  
  
  