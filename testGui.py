# форма ввода 
#import PySimpleGUI as sg
#sg.preview_all_look_and_feel_themes()
# sg.theme('DarkGrey15')
# layout = [[sg.Text('Окошко ввода.')],      
#                  [sg.InputText('010111')], 
#                  [sg.Checkbox('Согласие с действием', True)],
#                  [sg.Submit('Океей'), sg.Cancel('Неа')]]      
# window = sg.Window('Заголовок окошка ввода', layout)    

# event, values = window.read()    
# window.close()

# text_input = values[0]    
# sg.popup('Вы ввели значение:', text_input, )

# sg.theme('DarkGrey13')
# layout =[[sg.Text('Это окно полностью создано вручную \n оно экспериментальное.', (None, None), (None,None), True, False, False, "sunken", ("Noto Sans Regular", 16))],
#                 [sg.Submit('Ok \n ну а чё?', (None, None), (25, 10)), sg.Text('Этот текст будет \n аккуратненько размещен \n справа от большой \n кнопки \"окей\"', (None, None), (None, 6), True, False, False, "groove", ("Noto Sans Regular", 12))]
#                 ]
# window = sg.Window ('Нешаблонное окно', layout)
# event = window.read()
# window.close()
