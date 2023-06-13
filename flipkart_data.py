from bs4 import BeautifulSoup
import requests


def extract_data(usearch):
    
    phone_details = []
    try:
        '''New Url Modulation'''
        url  = "https://www.flipkart.com/search?q="
        x = usearch.split()
        srh = '%20'.join(x)
        newurl = url + srh
        print('New Url: ',newurl)

        response = requests.get(newurl)                               
        soup     = BeautifulSoup(response.text,'html.parser')          
        products   = soup.find_all('div',class_='_3pLy-c row')
        print('Total items found in search',len(products))

        
        # Dictionary format 
        num = 0
        for prod in products:
            phone = {   
                    'pnum':0,'name':'nodata' , 'price':'no data' , 'rate':'no data',
                    'ram':'' ,  'rom':'' ,   'mem':'',
                    'size':'',  'bcam':'',   'fcam':'',
                    'bat':'' ,  'pro':'' ,   'war':'' 
                    }
            num = num + 1
            phone['pnum'] = num 
        
            name  = prod.find('div',class_='col col-7-12').find('div',class_='_4rR01T').text
            phone['name'] = name
            pri = prod.find('div',class_='col col-5-12 nlI3QM').find('div',class_='_30jeq3 _1_WHN1').text
            new = pri.replace(',','')
            price = new.replace('₹','')
            phone['price'] = int(price)

            rate  = prod.find('div',class_='col col-7-12').find('div',class_='_3LWZlK').text
            phone['rate'] = rate
            specs = prod.find('div',class_='col col-7-12').find('div',class_='fMghEO').find('ul').find_all('li',class_='rgWa7D')
            
            '''All Specifictaion are added to List'''
            allspecs = []
            for item in specs:
                allspecs.append(item.text)

            ''' separation of specifications '''
            for each in allspecs:
                if 'GB' in each:
                    storage = each.split('|')

                    for item in storage:
                        if "RAM" in item:
                            phone['ram'] =item
                            
                        elif "ROM" in item:
                            phone['rom'] =item
                        
                        elif "Expandable" in item:
                            phone['mem'] =item

                elif 'Display' in each:
                    size = each
                    phone['size'] =size
                    
                elif 'MP' in each:
                    camera = each
                    if '|' in camera:
                        camera =camera.split('|')
                        bcam = camera[0]
                        fcam = camera[1]
                    else:
                        bcam = camera
                        fcam = ''

                    phone['bcam'] = bcam
                    phone['fcam'] = fcam

                elif 'Battery' in each:
                    bat = each
                    phone['bat'] = bat

                elif 'Processor' in each:
                    pro = each
                    phone['pro'] = pro
                    
                elif 'Warranty' or 'Year' or 'Months' in each:
                    war = each
                    phone['war'] = war
                    
                else:
                    print(each)
                    print('missing criteria')  
            
            phone_details.append(phone)


    
    except Exception as msg:
        print('Error in extracting is  : ',msg)
        


    return phone_details

#****************************************************************************************************










