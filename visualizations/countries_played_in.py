import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import operator


def addGamePlayed(list, host_nations, country):
    index = findCountryIndex(list, country)
    host_nations[index] += 1
    return host_nations

def findCountryIndex(list, country):
    index = -1
    for i in range(0, len(list)):
        if (list[i] == country):
            index = i
        else:
            continue
    if (index >= 0):
        return index
    else:
        print('Country ', country, ' does not exist')
        exit()

def analysis():
    # Read in modified CSV file
    f = pd.read_csv('../datasets/results_modified.csv')

    # Find country location and sort alphabetically
    # Initialize a couple lists
    countries    = f['country']
    host         = np.sort(f['country'].unique())
    host_nations = [0 for x in range(0, len(host))]

    # Count the number of games played in each country
    for index in range(0, len(countries)):
        host_nations = addGamePlayed(host, host_nations, countries[index])

    # Find the 20 nations with the most games played
    numbers = dict(zip(host, host_nations))
    sorted_countries  = sorted(numbers.items(), key=operator.itemgetter(1), reverse=True)
    top_twenty = sorted_countries[:20]

    return top_twenty

def plotting():
    top_twenty = analysis()

    top_countries = [top_twenty[country][0] for country in range(0, len(top_twenty))]
    for index in range(0,len(top_countries)):
        if (top_countries[index] == 'United Arab Emirates'):
            top_countries[index] = 'U.A.E.'
    top_games     = [top_twenty[games][1] for games in range(0, len(top_twenty))]

    xticks = [i for i in range(0, len(top_games))]
    yticks = [i for i in range(100, 1300, 100)]

    plt.figure(figsize=(15,5))
    plt.title('Top 20 Countries In Number Of\n International Soccer Matches Hosted', fontsize=24, weight='bold')
    #plt.xlabel('Countries', fontsize=20)
    plt.ylabel('Games Played', fontsize=20)
    plt.xlim(-1, 20)
    plt.ylim(0, 1100)
    plt.xticks(xticks, top_countries, y=-.01, rotation=90, fontsize=18)
    plt.yticks(yticks, yticks)

    plt.plot(xticks, top_games, 'ko')
    plt.grid(which='both', axis='y', alpha=0.5)
    #for index in range(1, len(xticks), 2):
    #    plt.gca().get_xaxis().majorTicks[index].label1.set_verticalalignment('top')
    #for index in range(0, len(xticks), 2):
    #    plt.gca().get_xaxis().majorTicks[index].label1.set_verticalalignment('baseline')
    for i in range(0, len(xticks)):
        plt.vlines(i, linestyle='--', color='k', linewidth=2, alpha=0.5, ymin=0, ymax=top_games[i])
    plt.tight_layout()
    plt.savefig('best_hosts.pdf', dpi=400)
    plt.show()


plotting()
