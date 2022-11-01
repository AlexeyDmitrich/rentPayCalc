# форма ввода 
import PySimpleGUI as sg
#sg.preview_all_look_and_feel_themes()
sg.theme('DarkGrey15')
layout = [[sg.Text('Окошко ввода.')],      
                 [sg.InputText('010111')], 

                 [sg.Submit('Океей'), sg.Cancel('Неа')]]      
window = sg.Window('Заголовок окошка ввода', layout)    

event, values = window.read()    
window.close()

text_input = values[0]    
sg.popup('Вы ввели значение:', text_input)

#If you want to use a key instead of an auto-generated key:
