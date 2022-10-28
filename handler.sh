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
bigLog=bigLog.csv
tempCounterGas=temp_counter_gas
tempCounterWater=temp_counter_water
tempCounterEnergy=temp_counter_energy


#готовим сегодняшнюю дату
datex=`date +'%d.%m.%Y'`
today=$datex

#удаляем пустые строки файла
`sed -i '/^$/d' $bigLog.csv`

#читаем последнюю строку из документа в формате "вчера, показания, расход"
yest=`tail -1 $bigLog.csv`
IFS=","
read -a strarr <<< "$yest"

waterCountLast=${strarr[0]}    #
waterTaripheIn=${strarr[1]}    #
waterTaripheOut=${strarr[2]}   #

gasCounter=${strarr[3]}
gasTariphe=${strarr[4]}

energyCounter=${strarr[5]}
energyTariphe=${strarr[6]}

warm=${strarr[7]}

com1=${strarr[8]}
com2=${strarr[9]}
build=${strarr[10]}

