import pandas as pd

rent=6000

allInOne = pd.read_csv('temp_log.csv', header=None)
#print(allInOne)

date= (allInOne[0][0])
#print(date)
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
def usage (last, new):
    return float(new-last)

def payByCount (last, new, tariphe1, tariphe2):
    taripheUn=tariphe1+tariphe2
    payment = (usage(last, new))*taripheUn
    return float(payment)

def payByTariphe (tariphe):
    return float(tariphe)

payEnergy = round(payByCount (lastEnergy, newEnergy, newTaripheEnergy, 0), 2)
payGas = round(payByCount (lastGas, newGas, newTaripheGas, 0), 2)
payWater = round(payByCount (lastWater, newWater, newTaripheWaterIn, newTaripheWaterOut), 2)
payWarm = payByTariphe (newTaripheWarm)
payBuild = payByTariphe (newTaripheBuild)
payWaste = payByTariphe (newTaripheWaste)
payUnitedWater = payByTariphe (newTaripheUnitedWater)
payRebuilding = payByTariphe (newTaripheRebuilding)

summPay=(payEnergy+payGas+payWater+payWarm+payBuild+payWaste+payUnitedWater+payRebuilding+rent)
#print ("Суммарная оплата составила: ", summPay)

# формирование чека
tradeCheck = open ('check.txt', 'a+')
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

bigLog = open('bigLog.csv', 'a+')
bigLog.writelines("\n" + str(date) +","+ str(newEnergy) +","+ str(newTaripheEnergy) +","+ str(newGas) +","+ str(newTaripheGas) +","+ str(newWater) +","+ str(newTaripheWaterIn) +","+ str(newTaripheWaterOut) +","+ str(newTaripheWarm) +","+ str(newTaripheBuild) +","+ str(newTaripheWaste) +","+ str(newTaripheUnitedWater) +","+ str(newTaripheRebuilding ))
bigLog.close

# bigLog= pd.DataFrame([[str(date) , str(newEnergy) , str(newTaripheEnergy) , str(newGas) , str(newTaripheGas) , str(newWater) , str(newTaripheWaterIn) , str(newTaripheWaterOut) , str(newTaripheWarm) , str(newTaripheBuild) , str(newTaripheWaste) , str(newTaripheUnitedWater) , str(newTaripheRebuilding )]])
# bigLog.to_csv('bigLog', index=False)