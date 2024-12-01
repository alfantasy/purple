import requests
from bs4 import BeautifulSoup
import re
import datetime
url = "https://lk.ks.psuti.ru/?mn=2&obj=136"
tod = datetime.datetime.today()
tod_d = f"{tod.day}.{tod.month}.{tod.year}"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

current_date_table = soup.findAll("h3")

this_scan = soup.findAll("td", height="20", bgcolor="3481A6", align="center", background="lib/img/itf_ht/bg_h2_03.gif")

links = []

for item in soup.findAll('a'):
    for it in item.findAll("h3"):
        if it.text == "предыдущая неделя":
            link = item['href']
            links.append(link)
        if it.text == "следующая неделя":
            link = item['href']
            links.append(link)

links_current = list(set(links))
number = []
for link in links_current:
    mass = re.findall(r'\d+', link)
    number.append(mass)

parametr_for_page = False
for item in current_date_table:
    new = item.text.strip()
    if tod_d in new:
        parametr_for_page = False
        break
    else:
        parametr_for_page = True
        continue

print(number[0][2] + " " + number[1][2])

if number[0][2] > number[1][2]:
    if parametr_for_page == True:
        url = "https://lk.ks.psuti.ru/?mn=2&obj=136&wk="+ str(number[0][2])
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
else:
    if parametr_for_page == True:
        url = "https://lk.ks.psuti.ru/?mn=2&obj=136&wk="+ str(number[0][2])
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

table = soup.find("table", border="0", cellpadding="1", cellspacing="1", bgcolor="3481A6")

text = table.findAll("td")
allPars = []
monday_pars = []
tuesday_pars = []
wednesday_pars = []
thursday_pars = []
friday_pars = []
saturday_pars = []

for data in table:
    if data.find("td") is not None:
        rx = re.compile('\s+')
        new = data.text.strip()
        string = rx.sub(' ', new)
        new_string = re.split(r"([А-ЯЁ][а-яё]*)", string)
        allPars.append(new_string)

for data in allPars:
    #if re.search(r'\d\d\.\d\d\.\d{4}', data):
    #    print(data)
    try: 
        while True:
            allPars.remove([''])
    except ValueError:
        pass
    if "Понедельник" in data:  
        allPars.remove(data)
        continue
    if "№ пары" in data or "Время" in data or "Занятий" in data or 'Способ' in data or "Дисциплина" in data or "преподаватель" in data or 'Тема' in data or "занятия" in data or 'Ресурс' in data or 'Задание' in data or 'для выполнения' in data:
        allPars.remove(data)
        continue
    if "С" in data and "С" in data and "А" in data and "-7" in data:
        allPars.remove(data)
        continue
    if "Вторник" in data:
        break
    monday_pars.append(data)

for date in monday_pars:
    try:
        allPars.remove(date)
    except:
        pass

for data in allPars:
    try: 
        while True:
            allPars.remove([''])
    except ValueError:
        pass
    if "Понеделник" in data: 
        continue
    if "Вторник" in data:  
        continue
    if "№ пары" in data or "Время" in data or "Занятий" in data or 'Способ' in data or "Дисциплина" in data or "преподаватель" in data or 'Тема' in data or "занятия" in data or 'Ресурс' in data or 'Задание' in data or 'для выполнения' in data:
        continue
    if "С" in data and "С" in data and "А" in data and "-7" in data:
        continue
    if "Замена" in data:
        continue
    if "Среда" in data:
        break
    tuesday_pars.append(data)

for date in tuesday_pars:
    try:
        allPars.remove(date)
    except:
        pass

for data in allPars:
    try: 
        while True:
            allPars.remove([''])
    except ValueError:
        pass
    if "Понеделник" in data and "Замена" in date: 
        continue
    if "Вторник" in data:  
        continue
    if "Среда" in data:
        continue
    if "№ пары" in data or "Время" in data or "Занятий" in data or 'Способ' in data or "Дисциплина" in data or "преподаватель" in data or 'Тема' in data or "занятия" in data or 'Ресурс' in data or 'Задание' in data or 'для выполнения' in data:
        continue
    if "С" in data and "С" in data and "А" in data and "-7" in data:
        continue
    #print(data)
    if "Четверг" in data:
        break
    #print(data)
    wednesday_pars.append(data)  

for date in wednesday_pars:
    try:
        allPars.remove(date)
    except:
        pass

for data in allPars:
    try: 
        while True:
            allPars.remove([''])
    except ValueError:
        pass
    if "Понеделник" in data and "Замена" in date: 
        continue
    if "Вторник" in data:  
        continue
    if "Среда" in data:
        continue
    if "№ пары" in data or "Время" in data or "Занятий" in data or 'Способ' in data or "Дисциплина" in data or "преподаватель" in data or 'Тема' in data or "занятия" in data or 'Ресурс' in data or 'Задание' in data or 'для выполнения' in data:
        continue
    if "С" in data and "С" in data and "А" in data and "-7" in data:
        continue
    #print(data)
    if "Четверг" in data:
        continue
    if "Пятница" in data:
        break
    #print(data)
    thursday_pars.append(data)  

for date in thursday_pars:
    try:
        allPars.remove(date)
    except:
        pass

for data in allPars:
    try: 
        while True:
            allPars.remove([''])
    except ValueError:
        pass
    if "Понеделник" in data and "Замена" in date: 
        continue
    if "Вторник" in data:  
        continue
    if "Среда" in data:
        continue
    if "№ пары" in data or "Время" in data or "Занятий" in data or 'Способ' in data or "Дисциплина" in data or "преподаватель" in data or 'Тема' in data or "занятия" in data or 'Ресурс' in data or 'Задание' in data or 'для выполнения' in data:
        continue
    if "С" in data and "С" in data and "А" in data and "-7" in data:
        continue
    #print(data)
    if "Четверг" in data:
        continue
    if "Пятница" in data:
        continue
    if "Суббота" in data:
        break
    #print(data)
    friday_pars.append(data)  

for date in friday_pars:
    try:
        allPars.remove(date)
    except:
        pass

for data in allPars:
    try: 
        while True:
            allPars.remove([''])
    except ValueError:
        pass
    if "Понеделник" in data and "Замена" in date: 
        continue
    if "Вторник" in data:  
        continue
    if "Среда" in data:
        continue
    if "№ пары" in data or "Время" in data or "Занятий" in data or 'Способ' in data or "Дисциплина" in data or "преподаватель" in data or 'Тема' in data or "занятия" in data or 'Ресурс' in data or 'Задание' in data or 'для выполнения' in data:
        continue
    if "С" in data and "С" in data and "А" in data and "-7" in data:
        continue
    #print(data)
    if "Четверг" in data:
        continue
    if "Пятница" in data:
        continue
    if "Суббота" in data:
        continue
    #print(data)
    saturday_pars.append(data)

def show_monday():
    print("  | Вывожу корректное расписание на понедельник: \n")
    for date in monday_pars:
        current_class = date[0].split()
        primary = "".join(date[3:4])
        past = "".join(date[5:6])
        secondary = "".join(date[7:8])
        lesson0 = "".join(date[1:2])
        lesson1 = "".join(date[2:3])
        time0 = "".join(current_class[1:2])
        time1 = "".join(current_class[3:4])
        current_par = "".join(current_class[:-3])
        time = f"{time0} - {time1}"
        if not "Замена" in date:
            text = [
                f"Номер пары: {current_par}",
                f" Время занятий: {time}",
                f" Предмет: {lesson0}{lesson1}",
                f" Преподаватель: {primary} {past} {secondary}",
                f" Кабинет{date[-1]}"
            ]
        else:
            try:
                text = [
                    f"Произведена замена! Корректная пара представлена снизу:",
                    f"Номер пары: {current_par}",
                    f" Время занятий: {time}",
                    f" Предмет: {date[19]}{date[20]}",
                    f" Преподаватель: {date[21]} {date[23]} {date[25]}",
                    f" Кабинет{date[30]}"
                ]
            except:
                pass
        for line in text:
            if "Время занятий:  - " not in line and ":" in line and line.split(":")[1].strip() != "":
                print(line)

        #print(f"Номер пары: \n Время занятий: {time} \n Предмет: {lesson0}{lesson1} \n Преподаватель: {primary} {past} {secondary}\n Кабинет{date[-1]}")

#print("\n\n\n\n")

def show_tuesday():
    print("  | Вывожу корректное расписание на вторник: \n")
    notsv = False
    pdate = []
    param = False
    for date in tuesday_pars:
        #print(date)
        current_class = date[0].split()
        try:
            pdate.append(current_class[6])
        except:
            pass
        if "Замена" in date:
            param = True 
            if "Свободное" in date:
                pass 
            else:
                continue
        if param == True:
            if "перенос" in current_class:
                print(f"Номер пары: {current_class[0]} \n Перенос на дату {pdate[0]} \n Назначено свободное время. \n Предмет: {date[3]}{date[5]} \n Преподаватель: {date[7]} {date[9]}.{date[11]}")
            elif notsv == False:
                print(f"Номер пары: {current_class[0]} \n Назначено свободное время. \n Предмет: {date[3]}{date[5]}{date[7]}{date[9]}{date[11]} \n Преподаватель: {date[13]} {date[15]}.{date[17]}")
            elif notsv == True:
                param = False 
                print(f"Номер пары: {current_class[0]} \n Время занятий: {current_class[1]} - {current_class[3]} \n Предмет: {date[5]}{date[6]} \n Преподаватель: {date[7]} {date[9]} {date[11]}\n Кабинет{date[16]}")
        else:
            print(f"Номер пары: {current_class[0]} \n Время занятий: {current_class[1]} - {current_class[3]} \n Предмет: {date[1]} {date[2]} \n Преподаватель: {date[3]} {date[5]} {date[7]} \n Кабинет{date[12]}")   

def show_wednesday():
    print("  | Вывожу корректное расписание на среду: \n")
    pdate = []
    notsv = False
    param = False
    for date in wednesday_pars:
        #print(date)
        current_class = date[0].split()
        try:
            pdate.append(current_class[6])
        except:
            pass
        if "Замена" in date:
            param = True
            if "Свободное" in date:
                pass 
            else:
                continue
        if param == True:
            if "перенос" in current_class:
                print(f"Номер пары: {current_class[0]} \n Перенос на дату {pdate[0]} \n Назначено свободное время. \n Предмет: {date[3]}{date[5]} \n Преподаватель: {date[7]} {date[9]}.{date[11]}")
            elif notsv == False:
                print(f"Номер пары: {current_class[0]} \n Назначено свободное время. \n Предмет: {date[3]}{date[5]}{date[7]}{date[9]}{date[11]} \n Преподаватель: {date[13]} {date[15]}.{date[17]}")
            elif notsv == True:
                param = False 
                print(f"Номер пары: {current_class[0]} \n Время занятий: {current_class[1]} - {current_class[3]} \n Предмет: {date[5]}{date[6]} \n Преподаватель: {date[7]} {date[9]} {date[11]}\n Кабинет{date[16]}")
        else:
            print(f"Номер пары: {current_class[0]} \n Время занятий: {current_class[1]} - {current_class[3]} \n Предмет: {date[1]} {date[2]} \n Преподаватель: {date[3]} {date[5]} {date[7]} \n Кабинет{date[12]}")   

def show_thursday():
    print("  | Вывожу корректное расписание на четверг: \n")
    pdate = []
    param = False
    notsv = False
    for date in thursday_pars:
        #print(date)
        current_class = date[0].split()
        try:
            pdate.append(current_class[6])
        except:
            pass
        if "Замена" in date:
            param = True
            if "Свободное" in date:
                pass 
            else:
                notsv = True
        if param == True:
            if "перенос" in current_class:
                print(f"Номер пары: {current_class[0]} \n Перенос на дату {pdate[0]} \n Назначено свободное время. \n Предмет: {date[3]}{date[5]} \n Преподаватель: {date[7]} {date[9]}.{date[11]}")
            elif notsv == False:
                print(f"Номер пары: {current_class[0]} \n Назначено свободное время. \n Предмет: {date[3]}{date[5]}{date[7]}{date[9]}{date[11]} \n Преподаватель: {date[13]} {date[15]}.{date[17]}")
            elif notsv == True:
                param = False 
                print(f"Номер пары: {current_class[0]} \n Время занятий: {current_class[1]} - {current_class[3]} \n Предмет: {date[5]}{date[6]} \n Преподаватель: {date[7]} {date[9]} {date[11]}\n Кабинет{date[16]}")
        else:
            print(f"Номер пары: {current_class[0]} \n Время занятий: {current_class[1]} - {current_class[3]} \n Предмет: {date[1]} {date[2]} \n Преподаватель: {date[3]} {date[5]} {date[7]} \n Кабинет{date[12]}")    

def show_friday():
    print("  | Вывожу корректное расписание на пятницу: \n")
    pdate = []
    param = False
    notsv = False
    for date in friday_pars:
        #print(date)
        current_class = date[0].split()
        try:
            pdate.append(current_class[6])
        except:
            pass
        if "Замена" in date:
            param = True
            if "Свободное" in date:
                pass 
            else:
                continue
        if param == True:
            if "перенос" in current_class:
                print(f"Номер пары: {current_class[0]} \n Перенос на дату {pdate[0]} \n Назначено свободное время. \n Предмет: {date[3]}{date[5]} \n Преподаватель: {date[7]} {date[9]}.{date[11]}")
            elif notsv == False:
                print(f"Номер пары: {current_class[0]} \n Назначено свободное время. \n Предмет: {date[3]}{date[5]}{date[7]}{date[9]}{date[11]} \n Преподаватель: {date[13]} {date[15]}.{date[17]}")
            elif notsv == True:
                param = False 
                print(f"Номер пары: {current_class[0]} \n Время занятий: {current_class[1]} - {current_class[3]} \n Предмет: {date[5]}{date[6]} \n Преподаватель: {date[7]} {date[9]} {date[11]}\n Кабинет{date[16]}")
        else:
            print(f"Номер пары: {current_class[0]} \n Время занятий: {current_class[1]} - {current_class[3]} \n Предмет: {date[1]} {date[2]} \n Преподаватель: {date[3]} {date[5]} {date[7]} \n Кабинет{date[12]}")    

def show_saturday():
    print("  | Вывожу корректное расписание на субботу: \n")
    pdate = []
    notsv = False
    param = False
    for date in saturday_pars:
        #print(date)
        current_class = date[0].split()
        try:
            pdate.append(current_class[6])
        except:
            pass
        if "Замена" in date:
            param = True
            if "Свободное" in date:
                pass 
            else:
                continue
        if param == True:
            if "перенос" in current_class:
                print(f"Номер пары: {current_class[0]} \n Перенос на дату {pdate[0]} \n Назначено свободное время. \n Предмет: {date[3]}{date[5]} \n Преподаватель: {date[7]} {date[9]}.{date[11]}")
            elif notsv == False:
                print(f"Номер пары: {current_class[0]} \n Назначено свободное время. \n Предмет: {date[3]}{date[5]}{date[7]}{date[9]}{date[11]} \n Преподаватель: {date[13]} {date[15]}.{date[17]}")
            elif notsv == True:
                param = False 
                print(f"Номер пары: {current_class[0]} \n Время занятий: {current_class[1]} - {current_class[3]} \n Предмет: {date[5]}{date[6]} \n Преподаватель: {date[7]} {date[9]} {date[11]}\n Кабинет{date[16]}")
        else:
            print(f"Номер пары: {current_class[0]} \n Время занятий: {current_class[1]} - {current_class[3]} \n Предмет: {date[1]} {date[2]} \n Преподаватель: {date[3]} {date[5]} {date[7]} \n Кабинет{date[12]}")      

show_monday()
print("\n")
show_tuesday()
print("\n")
show_wednesday()
print("\n")
show_thursday()
print("\n")
show_friday()
print("\n")
show_saturday()