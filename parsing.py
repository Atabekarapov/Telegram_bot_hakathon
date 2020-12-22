import csv
import requests
from bs4 import BeautifulSoup
import re

main_url = 'https://valuta.kg/'

def get_html(url):
    res = requests.get(url) # делает запрос и хранит response
    return res.text # возвр-ет html код как текст

def write_csv(data):
    with open('valuta.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow((
            data['название'],
            data['usd покупка'],
            data['usd продажа'],
            data['eur покупка'],
            data['eur продажа'],
            data['rub покупка'],
            data['rub продажа'],
            data['kzt покупка'],
            data['kzt продажа'],
        ))

def get_all_links(html):
    soup = BeautifulSoup(html, 'html.parser') # Сохраняет красивый код
    # print(soup)
    trs = soup.find('div', class_ = 'rate-list').find('table', class_='vl-list').find('tbody').find_all('tr') # нахождения тега td
    # print(trs)
    list_= []
    for tr in trs:
        try:
        # try:
            title = tr.find('div', class_='td-member__info').find('h4').find('a').text
            # print(title)
            
            valuta = tr.find_all('td', class_='td-rate')
            for td in valuta:
                # print(td)
                one = td.find('div', class_='td-rate__wrp').text.strip()
                # print(one)
                list_.append(one)
            
            usd_pokupka = list_[0]
            usd_prodaja = list_[1]
            eur_pokupka = list_[2]
            eur_prodaja = list_[3]
            rub_pokupka = list_[4]
            rub_prodaja = list_[5]
            kzt_pokupka = list_[6]
            kzt_prodaja = list_[7]

            data = {
                    'название' : title,
                    "usd покупка" : usd_pokupka,
                    "usd продажа" : usd_prodaja,
                    "eur покупка" : eur_pokupka,
                    "eur продажа" : eur_prodaja,
                    "rub покупка" : rub_pokupka,
                    "rub продажа" : rub_prodaja,
                    "kzt покупка" : kzt_pokupka,
                    "kzt продажа" : kzt_prodaja,
                }
            list_.clear()
            # print(data)
        except:
            list_.append('')

        write_csv(data)

def main():
    base_url = 'https://kaktus.media/doc/'
    html_text = get_html(main_url)
    all_links = get_all_links(html_text)
    

if __name__ == '__main__':
    main()

    