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
tempLog=temp_log #.csv
tempCounters=temp_counters.csv


#готовим сегодняшнюю дату
datex=`date +'%d.%m.%Y'`
today=$datex

#удаляем пустые строки файла
`sed -i '/^$/d' $bigLog.csv`

#читаем последнюю строку из документа в формате "вчера, показания, расход"
yest=`tail -1 $bigLog.csv`
# IFS=","
# read -a strarr <<< "$yest"

# вносим строку для обработки во временный файл
echo "$today, $yest" > $tempLog

countWaterNew=0
countGasNew=0
countEnergyNew=0

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
