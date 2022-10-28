import pandas as pd

allInOne = pd.read_csv('temp_log.csv', header=None)
print(allInOne)

# объявляем переменные тарифы
waterTarIn= float(allInOne[2])
waterTarOut = float(allInOne[3])
gasTar=float(allInOne[5])
energyTar=float(allInOne[7])
buildTar=float(allInOne[9])
useTar=float(allInOne[10])
generalBuildTar=float(allInOne[11])

# собираем предыдущие показания:
lastWater= float(allInOne[1])
lastGas= float(allInOne[4])
lastEnergy= float(allInOne[6])

# отопление
warmTar=float(allInOne[8])

# bash должен сформировать этот документ:
newCounters = pd.read_csv('temp_counters.csv', header=None)

# принимаем новые показания счетчиков:
newWater = float(newCounters[0])
newGas = float(newCounters[1])
newEnergy = float(newCounters[2])

