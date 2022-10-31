import pandas as pd

allInOne = pd.read_csv('temp_log.csv', header=None)
print(allInOne)

# собираем предыдущие показания:
lastWater= float(allInOne[5])
lastGas= float(allInOne[3])
lastEnergy= float(allInOne[1])

# отопление
#warmTar=float(allInOne[8])

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
print(tariphesRefresh)

#payment
def usage (last, new):
    return float(new-last)

def payByCount (last, new, tariphe1, tariphe2):
    taripheUn=tariphe1+tariphe2
    payment = (usage(last, new))*taripheUn
    return float(payment)

def payByTariphe (tariphe):
    return float(tariphe)

payEnergy = payByCount (lastEnergy, newEnergy, newTaripheEnergy, 0)
payGas = payByCount (lastGas, newGas, newTaripheGas, 0)
payWater = payByCount (lastWater, newWater, newTaripheWaterIn, newTaripheWaterOut)
payWarm = payByTariphe (newTaripheWarm)
payBuild = payByTariphe (newTaripheBuild)
payWaste = payByTariphe (newTaripheWaste)
payUnitedWater = payByTariphe (newTaripheUnitedWater)
payRebuilding = payByTariphe (newTaripheRebuilding)

summPay=(payEnergy+payGas+payWater+payWarm+payBuild+payWaste+payUnitedWater+payRebuilding)
print ("Суммарная оплата составила: ", summPay)

# формирование строки для csv
