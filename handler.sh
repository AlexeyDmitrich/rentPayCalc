#! /bin/bash

#объявляем переменными рабочие файлы
bigLog=bigLog.csv
tempLog=temp_log.csv
tempCounters=temp_counters.csv
tempTar=temp_tariphes.csv

#готовим сегодняшнюю дату
datex=`date +'%d.%m.%Y'`
today=$datex

#удаляем пустые строки файла
`sed -i '/^$/d' $bigLog` #.csv`

#читаем последнюю строку из документа
yest=`tail -1 $bigLog` #.csv`
IFS=","
read -a strarr <<< "$yest"

# читаем старый тариф, готовим место под новый, задаем имя параметра
taripheWaterIn=${strarr[6]}
newTaripheWaterIn=0
waterInName="водоснабжение"

taripheWaterOut=${strarr[7]}
newTaripheWaterOut=0
waterOutName="водоотведение"

taripheGas=${strarr[4]}
newTaripheGas=0
gasName="газоснабжение"

taripheEnergy=${strarr[2]}
newTaripheEnergy=0
energyName="электроэнергия"

warm=${strarr[8]}
newTaripheWarm=0
warmName="отопление"

build=${strarr[9]}
newBuild=0
buildName="содержание домового имущества"

waste=${strarr[10]}
newWaste=0
wasteName="обращение с ТКО"

unitedWater=${strarr[11]}
newUnitedWater=0
unitedWaterName="общедомовое ХВС"

rebuilding=${strarr[12]}
newRebuilding=0
rebuildingName="капремонт"

# вносим строку для обработки во временный файл
echo "$today, ${strarr[1]}, ${strarr[2]}, ${strarr[3]}, ${strarr[4]}, ${strarr[5]}, ${strarr[6]}, ${strarr[7]}, ${strarr[8]}, ${strarr[9]}, ${strarr[10]}, ${strarr[11]}, ${strarr[12]}" > $tempLog

# объявляем счетчики
countWaterNew=0
countGasNew=0
countEnergyNew=0

# функция для сверки тарифов с предыдущими
markTariphe (){
        #1 tariphe***In
        #2 ***Name
        `kdialog --title "Сверка тарифов" --yesno "В прошлом месяце тариф на $2 \n составил $1 р. \n Он остался прежним?"`
        if [[ $? = 0 ]] #при нажатии Ок
        then
        kdialog --title "Тариф сохранен" --passivepopup "При необходимости его можно изменить в файле"
        # val=$inpval
        new=$1
        #    return $new
        else # при нажатии нет
                inpval=`kdialog --title "Изменение тарифа" --inputbox "Введите новый тариф на $2, \n используя точку для отделения копеек."`
                if [[ $? = 0 ]] # при вводе данных
                then
                new=$inpval
                kdialog --title "Тариф обновлен" --passivepopup "При необходимости его можно изменить в файле"
                #return $new
                else # при отмене ввода
                        kdialog --title "Что-то пошло не так" --error "Не хотите через форму - вводите вручную."
                exec $EDITOR $tempTar
                fi
        #        return $new
        fi
}

#создаем форму ввода показаний счетчика
#электроэнергия
inpval=`kdialog --title "Электроэнергия" --inputbox "Введите сегодняшние показания электросчётчика."`
if [[ $? = 0 ]] #при наличии введенного значения
then
	# val=$inpval
	countEnergyNew=$inpval
else # при отмене ввода
	kdialog --title "Что-то пошло не так" --error "Не хотите через форму - вводите вручную."
        exec $EDITOR $tempCounters
fi

# вода
inpval=`kdialog --title "Водоснабжение-водоотведение" --inputbox "Введите сегодняшние показания счётчика расхода воды."`
if [[ $? = 0 ]] #при наличии введенного значения
then
	# val=$inpval
	countWaterNew=$inpval
else # при отмене ввода
	kdialog --title "Что-то пошло не так" --error "Не хотите через форму - вводите вручную."
        exec $EDITOR $tempCounters
fi

# газ
inpval=`kdialog --title "Газоснабжение" --inputbox "Введите сегодняшние показания счётчика расхода газа."`
if [[ $? = 0 ]] #при наличии введенного значения
then
	# val=$inpval
	countGasNew=$inpval
else # при отмене ввода
	kdialog --title "Что-то пошло не так" --error "Не хотите через форму - вводите вручную."
        exec $EDITOR $tempCounters
fi

# собираем показания счетчиков в файл
echo "$countWaterNew, $countGasNew, $countEnergyNew" > $tempCounters

# # ------------------------------------------------------------------------------------------
# далее: сверка каждого тарифа с помощью функции markTariphe
# и упаковка результатов в .csv файл

markTariphe $taripheEnergy $energyName
newTaripheEnergy=$new
#echo "Новый тариф на электроснабжение = $newTaripheEnergy"

markTariphe $taripheGas $gasName
newTaripheGas=$new
#echo "Новый тариф на газоснабжение = $newTaripheGas"

markTariphe $taripheWaterIn $waterInName
newTaripheWaterIn=$new
#echo "Новый тариф на водоснабжение = $newTaripheWaterIn"

markTariphe $taripheWaterOut $waterOutName
newTaripheWaterOut=$new
#echo "Новый тариф на водоотведение = $newTaripheWaterOut"

markTariphe $warm $warmName
newTaripheWarm=$new
#echo "Новый тариф на отопление = $newTaripheWarm"

markTariphe $build $buildName
newBuild=$new
#echo "Новый тариф на $buildName = $newBuild"

markTariphe $waste $wasteName
newWaste=$new
#echo "Новый тариф на $wasteName = $newWaste"

markTariphe $unitedWater $unitedWaterName
newUnitedWater=$new
#echo "Новый тариф на $unitedWaterName = $newUnitedWater"

markTariphe $rebuilding $rebuildingName
newRebuilding=$new
#echo "Новый тариф на $rebuildingName = $newRebuilding"

# собираем строковый файл с тарифами
echo "$newTaripheEnergy, $newTaripheGas, $newTaripheWaterIn, $newTaripheWaterOut, $newTaripheWarm, $newBuild, $newWaste, $newUnitedWater, $newRebuilding" > $tempTar


# стартуем обработку собранных данных:
`python calc.py`
