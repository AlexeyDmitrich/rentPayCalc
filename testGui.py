# import PySimpleGUI as sg
# import calc as cl
# красивый десктопный вывод
# sg.theme('DarkGrey13')
# layout =[[sg.Text('Сводная таблица оплаты', (37, None), (None,None), True, False, False, "sunken", ("Noto Sans Regular", 14))],
#                 [sg.Text(cl.date)],
#                 [sg.Text('Параметр', (None, None), (26, 1), True, False, False, "groove", ("Noto Sans Regular", 12)), sg.Text('Расход', (None, None), (7, 1), True, False, False, "groove", ("Noto Sans Regular", 12)), sg.Text('К оплате', (None, None), (9, 1), True, False, False, "groove", ("Noto Sans Regular", 12))],
#                 [sg.Text('Электроснабжение', (34,1)), sg.Text(str(cl.usage(cl.lastEnergy,cl.newEnergy)), (9,1)), sg.Text(str(cl.payEnergy))],
#                 [sg.Text('Газоснабжение', (34,1)), sg.Text(str(cl.usage(cl.lastGas,cl.newGas)), (9,1)), sg.Text(str(cl.payGas))],
#                 [sg.Text('Водоснабжение', (34,1)), sg.Text(str(cl.usage(cl.lastWater,cl.newWater)), (9,1)), sg.Text(str(cl.payWater))],
#                 [sg.Text('Отопление', (34,1)), sg.Text(' ---- ', (9,1)), sg.Text(str(cl.payWarm))],
#                 [sg.Text('Содержание общ имущества', (34,1)), sg.Text(' ---- ', (9,1)), sg.Text(str(cl.payBuild))],
#                 [sg.Text('Обращение с ТКО', (34,1)), sg.Text(' ---- ', (9,1)), sg.Text(str(cl.payWaste))],
#                 [sg.Text('Общедомовое ХВС', (34,1)), sg.Text(' ---- ', (9,1)), sg.Text(str(cl.payUnitedWater))],
#                 [sg.Text('Капремонт', (34,1)), sg.Text(' ---- ', (9,1)), sg.Text(str(cl.payRebuilding))],
#                 [sg.Text('Итого, учитывая стоимость аренды    ('), sg.Text(str(cl.rent)), sg.Text('р.) :'), sg.Text(str(cl.summPay))],
#                 [sg.Submit('С результатами ознакомлен', (55))]
#                 ]
# window = sg.Window ('Чек за коммунальные услуги', layout)
# event, values = window.read(close=True)
# window.close()