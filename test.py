import pandas as pd

# получаем значения тарифов из csv
# tariphes = pd.read_csv('tariphesConst.csv', header=None, skiprows=[0])
# waterTarOut = float(tariphes[1])
# waterTarIn= float(tariphes[0])
# gasTar=float(tariphes[2])
# energyTar=float(tariphes[3])
# buildTar=float(tariphes[4])
# useTar=float(tariphes[5])
# generalBuildTar=float(tariphes[6])

allInOne = pd.read_csv('temp_log.csv', header=None)
print(allInOne)
# объявляем переменные тарифы
waterTarIn= float(allInOne[2])
waterTarOut = float(allInOne[3])
gasTar=float(allInOne[5])
warmTar=float(allInOne[8])
buildTar=float(allInOne[9])
useTar=float(allInOne[10])
generalBuildTar=float(allInOne[11])

# собираем предыдущие показания:
lastWater= float(allInOne[1])
lastGas= float(allInOne[4])
lastEnergy= float(allInOne[6])

# отопление
energyTar=float(allInOne[7])

newCounters = pd.read_csv('temp_counters.csv', header=None)

# инициализируем место под новые:
newWater = float(newCounters[0])
newGas = float(newCounters[1])
newEnergy = float(newCounters[2])