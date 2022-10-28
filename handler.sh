#! /bin/bash

#Объявляем переменные окружения
DISPLAY=:0.0
#SESSION_MANAGER=local/reu-sigma:@/tmp/.ICE-unix/897,unix/reu-sigma:/tmp/.ICE-unix/897
XAUTHORITY=/home/reu/.Xauthority
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
XDG_RUNTIME_DIR=/run/user/1000
BEEP=/usr/share/sounds/freedesktop/stereo/bell.oga
#Экспортируем окружения
export DISPLAY SESSION_MANAGER XAUTHORITY DBUS_SESSION_BUS_ADDRES XDG_RUNTIME_DIR #BEEP

#объявляем переменными рабочие файлы
bigLog=bigLog #.csv
tempLog=temp_log.csv
tempCounters=temp_counters.csv
tempTar=temp_tariphes.csv


#готовим сегодняшнюю дату
datex=`date +'%d.%m.%Y'`
today=$datex

#удаляем пустые строки файла
`sed -i '/^$/d' $bigLog.csv`

#читаем последнюю строку из документа
yest=`tail -1 $bigLog.csv`
IFS=","
read -a strarr <<< "$yest"
taripheWaterIn=${strarr[1]}
taripheWaterOut=${strarr[2]}
taripheGas=${strarr[4]} 
taripheEnergy=${strarr[6]}
warm=${strarr[7]}
build=${strarr[8]}
useBuild=${strarr[9]}
rebuilding=${strarr[10]}

# вносим строку для обработки во временный файл
echo "$today, $yest" > $tempLog

countWaterNew=0
countGasNew=0
countEnergyNew=0

# ------------------------------------------------------------------------------------------------
#создаем форму ввода показаний счетчика
# электроэнергия
inpval=`kdialog --title "Электроэнергия" --inputbox "Введите сегодняшние показания электросчётчика."`
if [[ $? = 0 ]] #при наличии введенного значения
then
	# val=$inpval
	countEnergyNew=$inpval
else # при отмене ввода
	kdialog --title "Что-то пошло не так" --error "Не хотите через форму - вводите вручную."
        exec mousepad $tempCounters
fi

# вода
inpval=`kdialog --title "Водоснабжение-водоотведение" --inputbox "Введите сегодняшние показания счётчика расхода воды."`
if [[ $? = 0 ]] #при наличии введенного значения
then
	# val=$inpval
	countWaterNew=$inpval
else # при отмене ввода
	kdialog --title "Что-то пошло не так" --error "Не хотите через форму - вводите вручную."
        exec mousepad $tempCounters
fi

# газ
inpval=`kdialog --title "Газоснабжение" --inputbox "Введите сегодняшние показания счётчика расхода газа."`
if [[ $? = 0 ]] #при наличии введенного значения
then
	# val=$inpval
	countGasNew=$inpval
else # при отмене ввода
	kdialog --title "Что-то пошло не так" --error "Не хотите через форму - вводите вручную."
        exec mousepad $tempCounters
fi

echo "$countWaterNew, $countGasNew, $countEnergyNew" > $tempCounters

# ------------------------------------------------------------------------------------------
# сверка тарифов:

`kdialog --title "Сверка тарифов" --yesno "На данный момент тариф на электроэнергию \n составляет $taripheEnergy"`
if [[ $? = 0 ]] #при нажатии Ок
then
    kdialog --title "Тариф сохранен" --passivepopup "При необходимости его можно изменить в файле"
     # val=$inpval
    newTaripheEnergy=$taripheEnergy
else # при нажатии нет
	inpval=`kdialog --title "Изменение тарифа" --inputbox "Введите новый тариф на электроэнергию, \n используя точку для отделения копеек."`
        if [[ $? = 0 ]] # при вводе данных
        then
            newTaripheEnergy=$inpval
        else # при отмене ввода
	        kdialog --title "Что-то пошло не так" --error "Не хотите через форму - вводите вручную."
            exec mousepad $tempTar
        fi
fi

`kdialog --title "Сверка тарифов" --yesno "На данный момент тариф на водоснабжение \n составляет $taripheWaterIn"`
if [[ $? = 0 ]] #при нажатии Ок
then
    kdialog --title "Тариф сохранен" --passivepopup "При необходимости его можно изменить в файле"
     # val=$inpval
    newTaripheWaterIn=$taripheWaterIn
else # при нажатии нет
	inpval=`kdialog --title "Изменение тарифа" --inputbox "Введите новый тариф на водоснабжение, \n используя точку для отделения копеек."`
        if [[ $? = 0 ]] # при вводе данных
        then
            newTaripheWaterIn=$inpval
        else # при отмене ввода
	        kdialog --title "Что-то пошло не так" --error "Не хотите через форму - вводите вручную."
            exec mousepad $tempTar
        fi
fi

`kdialog --title "Сверка тарифов" --yesno "На данный момент тариф на водоотведение \n составляет $taripheWaterOut"`
if [[ $? = 0 ]] #при нажатии Ок
then
    kdialog --title "Тариф сохранен" --passivepopup "При необходимости его можно изменить в файле"
     # val=$inpval
    newTaripheWaterOut=$taripheWaterOut
else # при нажатии нет
	inpval=`kdialog --title "Изменение тарифа" --inputbox "Введите новый тариф на водоотведение, \n используя точку для отделения копеек."`
        if [[ $? = 0 ]] # при вводе данных
        then
            newTaripheWaterOut=$inpval
        else # при отмене ввода
	        kdialog --title "Что-то пошло не так" --error "Не хотите через форму - вводите вручную."
            exec mousepad $tempTar
        fi
fi

`kdialog --title "Сверка тарифов" --yesno "На данный момент тариф на газоснабжение \n составляет $taripheGas"`
if [[ $? = 0 ]] #при нажатии Ок
then
    kdialog --title "Тариф сохранен" --passivepopup "При необходимости его можно изменить в файле"
     # val=$inpval
    newTaripheGas=$taripheGas
else # при нажатии нет
	inpval=`kdialog --title "Изменение тарифа" --inputbox "Введите новый тариф на газоснабжение, \n используя точку для отделения копеек."`
        if [[ $? = 0 ]] # при вводе данных
        then
            newTaripheGas=$inpval
        else # при отмене ввода
	        kdialog --title "Что-то пошло не так" --error "Не хотите через форму - вводите вручную."
            exec mousepad $tempTar
        fi
fi

`kdialog --title "Сверка тарифов" --yesno "В прошлом месяце тариф на отопление \n составил $taripheGas р. \n Он остался прежним?"`
if [[ $? = 0 ]] #при нажатии Ок
then
    kdialog --title "Тариф сохранен" --passivepopup "При необходимости его можно изменить в файле"
     # val=$inpval
    newWarm=$warm
else # при нажатии нет
	inpval=`kdialog --title "Изменение тарифа" --inputbox "Введите новый тариф на отопление, \n используя точку для отделения копеек."`
        if [[ $? = 0 ]] # при вводе данных
        then
            newWarm=$inpval
        else # при отмене ввода
	        kdialog --title "Что-то пошло не так" --error "Не хотите через форму - вводите вручную."
            exec mousepad $tempTar
        fi
fi


echo "$newTaripheWaterIn, $newTaripheWaterOut, $newTaripheGas, $newTaripheEnergy, $newWarm" > $tempTar