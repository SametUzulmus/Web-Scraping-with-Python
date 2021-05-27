# These lines of code visit arabam.com and get some of the features of 11 used cars for sale.

# Used Libraries: Requests, BeautifulSoup , Pandas



import requests
from bs4 import BeautifulSoup
import pandas

url="https://www.arabam.com/ikinci-el/otomobil?take=50"

html=requests.get(url).content

soup1=BeautifulSoup(html,"html.parser")

left_list=soup1.find_all("li",{"class":"category-facet-selection-item inside-li"})

genel_link="https://www.arabam.com"

sayac=1
for li in left_list:
    
    model_linkleri=li.a.get("href") # sol listenin linkleri
    new_link=genel_link+model_linkleri
    #print(model_linkleri)
    new_html=requests.get(new_link).content
    #print(new_link)
    soup2=BeautifulSoup(new_html,"html.parser")
    
    model_sayisi=soup2.find("span",{"class":"color-red4 bold pl4 fz13"}).text.strip().replace(" Sonuç","").replace("(","").replace(")","").replace(".","")
    model_sayisi=int(model_sayisi)
    #print(model_sayisi)
    
    if model_sayisi<=2500:
        
        model_sayisi=int(model_sayisi)//50+1
        
        for i in range(1,model_sayisi+1):
            
            dinamik_link=new_link+"?page="+str(i)
            d_html=requests.get(dinamik_link).content
            soup3=BeautifulSoup(d_html,"html.parser")
            
            in_link=soup3.find_all("td",{"class":"horizontal-half-padder-minus pr"})# her sayfada ayrı liste linklerini 
                                                                                    # almak için.
            for i in in_link:
                
                in_link_in=i.a.get("href") # sayfalardaki arabaların linkleri
                get_link=genel_link+in_link_in
                g_html=requests.get(get_link).content
                soup4=BeautifulSoup(g_html,"html.parser")
                
                #x=soup4.find("li",{"class":"bcd-list-item"})
                #print(sayac,get_link)
                
                x=soup4.find("body").find("ul",{"class":"w100 cf mt16"}).find("li",{"class":"bcd-list-item"})
                
                k=1
        
                while k<11:
                    
                    x=x.findNextSibling()
                    
                    if x.text.startswith("Marka:"):
                        mark=x.text.replace("Marka:","").strip()
                        #print(mark)
                    
                    if x.text.startswith("Seri:"):
                        
                        series=x.text.replace("Seri:","").strip()
                        #print(series)
                    
                    if x.text.startswith("Model:"):
                        
                        model=x.text.replace("Model:","").strip()
                        #print(mark,series,model)
                    
                    if x.text.startswith("Yıl:"):
                        year=x.text.replace("Yıl:","").strip()
                        #print(year)
                        
                    if x.text.startswith("Yakıt Tipi:"):
                        
                        fuel_type=x.text.replace("Yakıt Tipi:","").strip()
                        #print(fuel_type)
                        
                    if x.text.startswith("Vites Tipi:"):
                        
                        gear_type=x.text.replace("Vites Tipi:","").strip()
                        #print(gear_type)
                        
                    if x.text.startswith("Motor Hacmi:"):
                        
                        engine_capacity=x.text.replace("Motor Hacmi:","").strip()
                        #print(engine_capacity)
                        
                    if x.text.startswith("Motor Gücü:"):
                        
                        engine_power=x.text.replace("Motor Gücü:","").strip()
                        #print(engine_power)
                        
                    if x.text.startswith("Kilometre:"):
                        
                        km=x.text.replace("Kilometre:","").strip() # Arada hata veriyor.
                        #print(km)
                    k+=1
                        
                if get_link.startswith("https://www.arabam.com/ilan/galeriden"):
                
                    from_who="Galeriden"
                else:
                                    
                    from_who="Sahibinden"
        
                price=soup4.find("div",{"class":"mb8"}).find("span").text
                price=str(price).strip()
                
                print(sayac,"- ",mark,series,model,year,fuel_type,gear_type,engine_capacity,engine_power,from_who,km,price)
                sayac+=1
