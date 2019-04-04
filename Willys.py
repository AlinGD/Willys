# Willys web scraping script.

import requests, re, time
import json

# Create the file - date will be included in its name.
file = 'SE_Willys_' + time.strftime('%Y%m%d') +'.ibs-utf8'

# Write the header of the file.
with open(file, 'w', encoding="utf-8") as f:
    f.write('SE\tCPSHub\tWillys\tPublic\n')

# Simple regex to filter out the EAN.
regex = re.compile(r'(\/)(\d{8,14})(.jpg|_\w|-\w)')

# URLS of all the Product Pages
urls = ['https://www.willys.se/c/Kott-chark-och-fagel/Korv?avoidCache=1554390165743&categoryPath=Kott-chark-och-fagel%2FKorv&size=5000',
        'https://www.willys.se/c/Frukt-och-Gront?avoidCache=1554401601399&categoryPath=Frukt-och-Gront&size=5000',
        'https://www.willys.se/c/Mejeri-ost-och-agg?avoidCache=1554401632761&categoryPath=Mejeri-ost-och-agg&size=5000',
        'https://www.willys.se/c/Skafferi?avoidCache=1554401666259&categoryPath=Skafferi&size=5000',
        'https://www.willys.se/c/Brod-och-Kakor?avoidCache=1554401695083&categoryPath=Brod-och-Kakor&size=5000',
        'https://www.willys.se/c/Fryst?avoidCache=1554401733992&categoryPath=Fryst&size=5000',
        'https://www.willys.se/c/Fisk-och-Skaldjur?avoidCache=1554401755860&categoryPath=Fisk-och-Skaldjur&size=5000',
        'https://www.willys.se/c/Vegetariskt?avoidCache=1554401786514&categoryPath=Vegetariskt&size=5000',
        'https://www.willys.se/c/Glass-godis-och-snacks?avoidCache=1554401808928&categoryPath=Glass-godis-och-snacks&size=5000',
        'https://www.willys.se/c/Dryck?avoidCache=1554401830141&categoryPath=Dryck&size=5000',
        'https://www.willys.se/c/Fardigmat?avoidCache=1554401849215&categoryPath=Fardigmat&size=5000',
        'https://www.willys.se/c/Barn?avoidCache=1554401868337&categoryPath=Barn&size=5000',
        'https://www.willys.se/c/Blommor?avoidCache=1554401888426&categoryPath=Blommor&size=5000',
        'https://www.willys.se/c/Hem-och-Stad?avoidCache=1554401908569&categoryPath=Hem-och-Stad&size=5000',
        'https://www.willys.se/c/Halsa-och-Skonhet?avoidCache=1554401936020&categoryPath=Halsa-och-Skonhet&size=5000',
        'https://www.willys.se/c/Apotek?avoidCache=1554401955637&categoryPath=Apotek&size=5000',
        'https://www.willys.se/c/Tradgard?avoidCache=1554401992624&categoryPath=Tradgard&size=5000',
        'https://www.willys.se/c/Husdjur?avoidCache=1554402011723&categoryPath=Husdjur&size=5000',
        'https://www.willys.se/c/Tobak-tandare-och-tobakstillbehor?avoidCache=1554402030578&categoryPath=Tobak-tandare-och-tobakstillbehor&size=5000']
        
# Loop through the pages and write in the file.   
for url in urls:  
    try:
        response = requests.get(url)
    except Exception as e:
        print("An error occured: " + e)
        
    responseStr = response.text
    data = json.loads(responseStr)


    with open(file, 'a', encoding="utf-8") as f:
        for i in range(len(data["results"])):
            
            long_url = data["results"][i]["image"]["url"]
            if long_url:
                short_url = regex.search(long_url)
                
            if (short_url.group(2)[0:6]) == '000000':
                f.write(short_url.group(2)[6:] + '\t' + data["results"][i]["name"] + ' | ' + data["results"][i]["productLine2"] + '\n')
            elif (len(short_url.group(2))) > 13:
                f.write(short_url.group(2)[1:] + '\t' + data["results"][i]["name"] + ' | ' + data["results"][i]["productLine2"] + '\n')
            else:
                f.write(short_url.group(2) + '\t' + data["results"][i]["name"] + ' | ' + data["results"][i]["productLine2"] + '\n')
    
    print(url[24:40] + " is successful")

    



