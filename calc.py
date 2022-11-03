import pandas as pd
import PySimpleGUI as sg

# установка арендной платы
rent=6000

sg.theme('DarkGrey15')
layout = [[sg.Text('Укажите ежемесячную сумму арендной платы')],      
                 [sg.InputText('6000')], 
                 [sg.Submit('Столько')]]      
window = sg.Window('Проверка стоимости аренды', layout)    
event, values = window.read()    
window.close()
text_input = values[0]    
rent = float(text_input)

# читаем последнюю запись лога, заботливо подготовленную sh скриптом
allInOne = pd.read_csv('temp_log.csv', header=None)
#print(allInOne)    #для отладки
date= (allInOne[0][0])
#print(date)    #для отладки
# собираем предыдущие показания:
lastWater= float(allInOne[5])
lastGas= float(allInOne[3])
lastEnergy= float(allInOne[1])

# bash должен сформировать этот документ:
newCounters = pd.read_csv('temp_counters.csv', header=None)

# принимаем новые показания счетчиков:
newWater = float(newCounters[0])
newGas = float(newCounters[1])
newEnergy = float(newCounters[2])

# о каждом тарифе подробно расспросит sh скрипт
tariphesRefresh= pd.read_csv('temp_tariphes.csv', header=None)
newTaripheEnergy = float(tariphesRefresh[0])
newTaripheGas = float(tariphesRefresh[1])
newTaripheWaterIn = float(tariphesRefresh[2])
newTaripheWaterOut = float(tariphesRefresh[3])
newTaripheWarm = float(tariphesRefresh[4])
newTaripheBuild = float(tariphesRefresh[5])
newTaripheWaste = float(tariphesRefresh[6])
newTaripheUnitedWater = float(tariphesRefresh[7])
newTaripheRebuilding = float(tariphesRefresh[8])
#print(tariphesRefresh)

#payment
# сколько намотали
def usage (last, new):
    return float(new-last)
# стоимость по счётчику
def payByCount (last, new, tariphe1, tariphe2):
    taripheUn=tariphe1+tariphe2
    payment = (usage(last, new))*taripheUn
    return float(payment)
# стоимость по тарифу
def payByTariphe (tariphe):
    return float(tariphe)

# сколько платить за каждую услугу
payEnergy = round(payByCount (lastEnergy, newEnergy, newTaripheEnergy, 0), 2)
payGas = round(payByCount (lastGas, newGas, newTaripheGas, 0), 2)
payWater = round(payByCount (lastWater, newWater, newTaripheWaterIn, newTaripheWaterOut), 2)
payWarm = payByTariphe (newTaripheWarm)
payBuild = payByTariphe (newTaripheBuild)
payWaste = payByTariphe (newTaripheWaste)
payUnitedWater = payByTariphe (newTaripheUnitedWater)
payRebuilding = payByTariphe (newTaripheRebuilding)

# сколько платить за всё вместе, считая аренду
def calcSumPay ():
    summPay=(payEnergy+payGas+payWater+payWarm+payBuild+payWaste+payUnitedWater+payRebuilding+rent)
#    print ("Суммарная оплата составила: ", summPay)     #для отладки
    return summPay

# записываем самую важную строку: из неё будут считаться показания в следующий раз
def writeLog ():
    with open('bigLog.csv', 'a+') as bigLog:
#        bigLog.readline(2)    #для отладки
        bigLog.writelines("\n" + str(date) +","+ str(newEnergy) +","+ str(newTaripheEnergy) +","+ str(newGas) +","+ str(newTaripheGas) +","+ str(newWater) +","+ str(newTaripheWaterIn) +","+ str(newTaripheWaterOut) +","+ str(newTaripheWarm) +","+ str(newTaripheBuild) +","+ str(newTaripheWaste) +","+ str(newTaripheUnitedWater) +","+ str(newTaripheRebuilding ))
        bigLog.close

summPay = calcSumPay ()
#формирование чека 
# делает запись в журнал в читаемом формате
def writeCheck ():
    with open('check.txt', 'a+') as tradeCheck:
        tradeCheck.writelines(date + '\n')
        tradeCheck.writelines("расчет платежа: \n")
        tradeCheck.writelines("|     параметр           |   расход   |   к оплате  |\n")
        tradeCheck.writelines("| электроснабжение       |" + str(usage(lastEnergy,newEnergy)) + "         " + str(payEnergy) + "       \n")
        tradeCheck.writelines("| газоснабжение          |" + str(usage(lastGas,newGas)) + "          " + str(payGas) + "       \n")
        tradeCheck.writelines("| водоснабжение          |" + str(usage(lastWater,newWater)) + "           " + str(payWater) + "       \n")
        tradeCheck.writelines("| отопление              |   ------   | " + str(payWarm) + "        \n")
        tradeCheck.writelines("| содерж.домов.имущества |   ------   | " + str(payBuild) + "       \n")
        tradeCheck.writelines("| обращение с ТКО        |   ------   | " + str(payWaste) + "       \n")
        tradeCheck.writelines("| общедомовое ХВС        |   ------   | " + str(payUnitedWater) + "         \n")
        tradeCheck.writelines("| капремонт              |   ------   | " + str(payRebuilding) + "       \n")
        tradeCheck.writelines("\n Итого, считая стоимость аренды (" + str(rent) + "р.): " + str(summPay) + "р. \n \n")
        tradeCheck.close

# делаем красивенький графический вывод
sg.theme('DarkGrey13')
layout =[[sg.Text('Сводная таблица оплаты', (37, None), (None,None), True, False, False, "sunken", ("Noto Sans Regular", 14))],
                [sg.Text(date)],
                [sg.Text('Параметр', (None, None), (26, 1), True, False, False, "groove", ("Noto Sans Regular", 12)), sg.Text('Расход', (None, None), (7, 1), True, False, False, "groove", ("Noto Sans Regular", 12)), sg.Text('К оплате', (None, None), (9, 1), True, False, False, "groove", ("Noto Sans Regular", 12))],
                [sg.Text('Электроснабжение', (34,1)), sg.Text(str(usage(lastEnergy,newEnergy)), (9,1)), sg.Text(str(payEnergy))],
                [sg.Text('Газоснабжение', (34,1)), sg.Text(str(usage(lastGas,newGas)), (9,1)), sg.Text(str(payGas))],
                [sg.Text('Водоснабжение', (34,1)), sg.Text(str(usage(lastWater,newWater)), (9,1)), sg.Text(str(payWater))],
                [sg.Text('Отопление', (34,1)), sg.Text(' ---- ', (9,1)), sg.Text(str(payWarm))],
                [sg.Text('Содержание общ имущества', (34,1)), sg.Text(' ---- ', (9,1)), sg.Text(str(payBuild))],
                [sg.Text('Обращение с ТКО', (34,1)), sg.Text(' ---- ', (9,1)), sg.Text(str(payWaste))],
                [sg.Text('Общедомовое ХВС', (34,1)), sg.Text(' ---- ', (9,1)), sg.Text(str(payUnitedWater))],
                [sg.Text('Капремонт', (34,1)), sg.Text(' ---- ', (9,1)), sg.Text(str(payRebuilding))],
                [sg.Text('Итого, учитывая стоимость аренды    ('), sg.Text(str(rent)), sg.Text('р.) :'), sg.Text(str(summPay))],
                [sg.Submit('С результатами ознакомлен', (55))]
                ]
window = sg.Window ('Чек за коммунальные услуги', layout)
event, values = window.read(close=True)
window.close()

writeLog ()
writeCheck ()