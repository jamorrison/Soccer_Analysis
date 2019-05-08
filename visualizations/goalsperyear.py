import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

f = pd.read_csv('../datasets/results_modified.csv')

years = []
goals = []

for year in range(1872, 2019, 1):
    if year%1 == 0:
        print(year)
    tmp_year = []
    tmp_goal = []
    for index in range(0, len(f['year'])):
        if f['year'][index] != year:
            continue
        elif f['year'][index] > year:
            break
        else:
            tmp_year.append(year)
            tmp_goal.append(f['total_score'][index])
    years.append(tmp_year)
    goals.append(tmp_goal)

year001 = []; goal001 = []; erro001 = []
year005 = []; goal005 = []; erro005 = []
year050 = []; goal050 = []; erro050 = []
year100 = []; goal100 = []; erro100 = []
year500 = []; goal500 = []; erro500 = []
for i in range(0, len(goals)):
    if (len(goals[i]) < 5):
        average = np.mean( np.array(goals[i]) )
        stdev   = np.std( np.array(goals[i]) )
        year001.append(years[i][0])
        goal001.append(average)
        erro001.append(stdev)
    elif (len(goals[i]) >= 5) and (len(goals[i]) < 50):
        average = np.mean( np.array(goals[i]) )
        stdev   = np.std( np.array(goals[i]) )
        year005.append(years[i][0])
        goal005.append(average)
        erro005.append(stdev)
    elif (len(goals[i]) >= 50) and (len(goals[i]) < 100):
        average = np.mean( np.array(goals[i]) )
        stdev   = np.std( np.array(goals[i]) )
        year050.append(years[i][0])
        goal050.append(average)
        erro050.append(stdev)
    elif (len(goals[i]) >= 100) and (len(goals[i]) < 500):
        average = np.mean( np.array(goals[i]) )
        stdev   = np.std( np.array(goals[i]) )
        year100.append(years[i][0])
        goal100.append(average)
        erro100.append(stdev)
    elif (len(goals[i]) >= 500):
        average = np.mean( np.array(goals[i]) )
        stdev   = np.std( np.array(goals[i]) )
        year500.append(years[i][0])
        goal500.append(average)
        erro500.append(stdev)

yticks = [y for y in range(0,14,2)]

plt.figure(figsize=(15,5))
plt.title('Average Number Of Goals\n Scored Between 1882 and 2018', fontsize=24, weight='heavy')
plt.xlabel('Year', fontsize=16, weight='bold')
plt.ylabel('Goals Scored', fontsize=16, weight='bold')

#plt.errorbar(x=year001, y=goal001, yerr=erro001, color='r', marker='o', ecolor='k', linestyle='None', label='0   - 4   matches')
plt.errorbar(x=year005, y=goal005, yerr=erro005, color='b', marker='o', ecolor='k', alpha=0.8, linestyle='None', label='5 - 49 matches')
plt.errorbar(x=year050, y=goal050, yerr=erro050, color='r', marker='o', ecolor='k', alpha=0.8, linestyle='None', label='50 - 99 matches')
plt.errorbar(x=year100, y=goal100, yerr=erro100, color='c', marker='o', ecolor='k', alpha=0.8, linestyle='None', label='100 - 499 matches')
plt.errorbar(x=year500, y=goal500, yerr=erro500, color='m', marker='o', ecolor='k', alpha=0.8, linestyle='None', label='500+ matches')
plt.gca().set_xlim(1880,2020)
plt.gca().set_ylim(0, 12)
plt.gca().set_yticks(yticks)
plt.legend(loc='upper right', fontsize=14)
plt.tight_layout()
plt.savefig('average_goals.pdf', dpi=400)
plt.show()
