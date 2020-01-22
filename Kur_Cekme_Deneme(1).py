import time
from urllib.request import urlopen
from bs4 import BeautifulSoup

time1 = time.time() #For stop the while loop. Starting time
kur_list = []
kelime = input("Search material: ")  #Say dolar or euro
kelime = kelime.replace(" ", "+")
url = "http://bigpara.hurriyet.com.tr/doviz/" + kelime

while True:
    sayfa = urlopen(url)
    soup = BeautifulSoup(sayfa, "html.parser")
    ana = soup.find('html')
    alt= ana.findAll('div',attrs={"class":"kurBox"})
    # x = len(alt)
    alis = alt[1].text.split()
    print(alis)
    alis = alis[1]
    alis = alis.replace(",",".")
    print(alis)
    alis_kuru = float(alis)
    kur_list.append(str(alis_kuru))
    # tl_miktari = int(input("Kaç para dönüştürmek istersiniz: "))
    # alinan_dolar = tl_miktari/alis_kuru
    # print("Elinizdeki parayla " + str(round(alinan_dolar,2)) + " " + kelime.title() + " satin alabilirsiniz.")

    time2 = time.time()
    delta = time2 - time1
    if delta > 120:
        delta_dk = delta/60
        print("\n")
        print("döngü bitti." + str(round(delta_dk,2)) +  " dakika veri çektiniz. ")
        print("\n")
        break
    time.sleep(10)  # Sleep for 10 seconds

print(kur_list)