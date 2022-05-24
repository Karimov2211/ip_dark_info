from pyfiglet import Figlet
import folium
import requests
from colorama import Fore, init
init()

def get_ip_info(ip="127.0.0.1"):
    try:
        hom = requests.get(url=f"http://ip-api.com/json/{ip}").json()
        #print(hom)

        data = {
           "[IP]":hom.get("query"),
           "[Сатус]":hom.get("status"),
           "[Мамлакат]":hom.get("country"),
           "[Коди мамлакат]":hom.get("countryCode"),
           "[Вилоят]":hom.get("region"),
           "[Номи вилоят]":hom.get("regionName"),
           "[Шахр]":hom.get("city"),
           "[Нохия]": hom.get("district"),
           "[Пахнои]":hom.get("lat"),
           "[Дарози]":hom.get("lon"),
           "[Вохиди пули]": hom.get("currency"),
           "[Соат]": hom.get("offset"),
           "[Ташкилот]": hom.get("org"),
           "[Рака,телефон]": hom.get("mobile"),
           "[Провайдер]": hom.get("isp"),
           "[Хостинг]": hom.get("hosting"),
           "[ZIP]": hom.get("zip"),
           "[Таймзона]":hom.get("timezone"),
           "[Номер AS]":hom.get("as"),
           "[Хамчу ном]": hom.get("asname"),
           "[Баргаштан reverse]": hom.get("reverse"),
           "[Прокси]": hom.get("proxy"),
           "[Континент]": hom.get("continent"),
           "[Континент код]": hom.get("continentCode"),


        }
        for k, v in data.items():
            print(f'{k} : {v}')
            area = folium.Map(location=[hom.get("lat"), hom.get("lon")])
            area.save(f'{hom.get("query")} {hom.get("city")}.html')
    except requests.exceptions.ConnectionError:
        print(Fore.RED + " [!]-Илтимос алокаи интернетиатонро санчед! ")

def main():
    privew_text = Figlet(font="slant")
    print(privew_text.renderText("Dark Net Tj"))
    ip = input(Fore.CYAN + " IP-адресро ворид кунед: ")
    get_ip_info(ip=ip)


if __name__ == "__main__":
    main()



