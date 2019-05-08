import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def addW(list, wins, winning_team):
   index = findCountryIndex(list, winning_team)
   wins[index] += 1
   return wins

def addL(list, loss, losing_team):
   index = findCountryIndex(list, losing_team)
   loss[index] += 1
   return loss

def addT(list, ties, home_team, away_team):
    home_idx = findCountryIndex(list, home_team)
    away_idx = findCountryIndex(list, away_team)
    ties[home_idx] += 1
    ties[away_idx] += 1
    return ties

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

def analysis(print_output):
    # Read in modified CSV file
    f = pd.read_csv('../datasets/results_modified.csv')

    # Only want World Cup matches for analysis
    mask = (f['tournament'] == 'FIFA World Cup')

    # Set arrays of home and away teams, home and away scores for each match
    home_team  = np.array(f[mask]['home_team'])
    away_team  = np.array(f[mask]['away_team'])
    home_score = np.array(f[mask]['home_score'])
    away_score = np.array(f[mask]['away_score'])

    # Not all teams have been both a home and an away team in the World Cup
    # Therefore, combine home and away team lists, choose the unique countries
    # Then sort alphabetically
    ateams = np.sort(np.array(f[mask]['away_team'].unique()))
    hteams = np.sort(np.array(f[mask]['home_team'].unique()))
    teams = np.unique(np.append(ateams,hteams))
    wins = [0 for x in range(0, len(teams))]
    ties = [0 for x in range(0, len(teams))]
    loss = [0 for x in range(0, len(teams))]

    # Count wins, losses, and ties
    for i in range(0, len(home_score)):
        if (home_score[i] > away_score[i]):
            wins = addW(teams, wins, home_team[i])
            loss = addL(teams, loss, away_team[i])
        elif (home_score[i] == away_score[i]):
            ties = addT(teams, ties, home_team[i], away_team[i])
        elif (home_score[i] < away_score[i]):
            wins = addW(teams, wins, away_team[i])
            loss = addL(teams, loss, home_team[i])

    if (print_output):
        print('{:20} {:2} {:2} {:2} {:2}'.format('Team', 'W' , 'T' , 'L' , 'WP'))
        print('___________________________________')
        for i in range(0, len(teams)):
            WP = (wins[i] + 0.5*ties[i]) / (wins[i] + ties[i] + loss[i])
            print('{:20} {:2d} {:2d} {:2d} {:.3f}'.format(teams[i], wins[i], ties[i], loss[i], WP))

    # Put team information into a dataframe for output
    WP = []
    for i in range(0, len(teams)):
        tmp = (wins[i] + 0.5*ties[i]) / (wins[i] + ties[i] + loss[i])
        WP.append(tmp)

    dic = {'country': teams, 'wins': wins, 'ties': ties, 'losses': loss, 'winning_percentage': WP}
    output = pd.DataFrame(dic)
    return output

def plotting():
    world_cup = analysis(False)

    sortWP = world_cup.sort_values('winning_percentage', ascending=False)
    sortW  = world_cup.sort_values('wins', ascending=False)
    sortL  = world_cup.sort_values('losses', ascending=False)
    sortT  = world_cup.sort_values('ties', ascending=False)
    entry  = [i for i in range(0, len(sortW['wins']))]

    team =  sortW['country']
    wins =  sortW['wins']
    ties =  sortW['ties']
    loss = -sortW['losses']

    blank = ['' for x in range(0,len(team))]

    #xticks = [i for i in range(-30,95,5)]
    xticks = [i for i in range(-30,100,10)]

    plt.figure(figsize=(10,10))
    plt.title('Wins, Losses, And Ties For All\n FIFA World Cup Participants', fontsize=24, weight='heavy')
    plt.xlabel('Losses/Wins/Ties', fontsize=20)
    plt.ylabel('Country', fontsize=20)
    plt.xlim(-30, 90)
    plt.ylim(entry[0]-1, entry[len(entry)-1]+1)
    plt.xticks(xticks, np.abs(xticks))
    plt.yticks(entry, blank, fontsize=8)

    plt.barh(entry, wins, height=0.8, color='#66c2a5')
    plt.barh(entry, ties, height=0.8, color='#fc8d62', left=wins)
    plt.barh(entry, loss, height=0.8, color='#8da0cb')
    #plt.gca().tick_params(axis='x', direction='in')
    #plt.gca().tick_params(axis='y', direction='in')
    plt.grid(which='both', axis='both',alpha=0.2,zorder=1)

    plt.text(x=50, y=50, s='Wins',   color='#66c2a5', fontsize=32, weight='heavy')
    plt.text(x=50, y=40, s='Ties',   color='#fc8d62', fontsize=32, weight='heavy')
    plt.text(x=50, y=30, s='Losses', color='#8da0cb', fontsize=32, weight='heavy')

    plt.annotate('Brazil', xy=(0.98,0.02), xycoords='axes fraction',
                 xytext=(0.9,0.15), textcoords='axes fraction',
                 ha='center', va='center',
                 arrowprops=dict(facecolor='white',edgecolor='black',connectionstyle='arc3,rad=-0.4'),
                 fontsize=24)#, weight='bold', color='black')

    plt.annotate('Germany', xy=(0.94,0.03), xycoords='axes fraction',
                 xytext=(0.8,0.09), textcoords='axes fraction',
                 ha='center', va='center',
                 arrowprops=dict(facecolor='white',edgecolor='black',connectionstyle='arc3,rad=-0.4'),
                 fontsize=24)#, weight='bold', color='black')

    plt.annotate('U.S.A.', xy=(0.38,0.30), xycoords='axes fraction',
                 xytext=(0.5,0.4), textcoords='axes fraction',
                 ha='center', va='center',
                 arrowprops=dict(facecolor='white',edgecolor='black',connectionstyle='arc3,rad=-0.4'),
                 fontsize=24)#, weight='bold', color='black')

    plt.annotate('Canada', xy=(0.255,0.915), xycoords='axes fraction',
                 xytext=(0.5,0.83), textcoords='axes fraction',
                 ha='center', va='center',
                 arrowprops=dict(facecolor='white',edgecolor='black',connectionstyle='arc3,rad=0.45'),
                 fontsize=24)#, weight='bold', color='black')

    plt.tight_layout()
    plt.savefig('all_teams_world_cup.pdf', dpi=400)
    plt.show()



plotting()

def horiz_plotting():
    world_cup = analysis(False)

    sortWP = world_cup.sort_values('winning_percentage', ascending=False)
    sortW  = world_cup.sort_values('wins', ascending=False)
    sortL  = world_cup.sort_values('losses', ascending=False)
    sortT  = world_cup.sort_values('ties', ascending=False)
    entry  = [i for i in range(0, len(sortW['wins']))]

    team =  sortW['country']
    wins =  sortW['wins']
    ties =  sortW['ties']
    loss = -sortW['losses']

    #xticks = [i for i in range(-30,95,5)]
    xticks = [i for i in range(-30,100,10)]

    plt.figure(figsize=(10,10))
    plt.title('Wins and Losses')
    plt.xlabel('wins/losses')
    plt.ylabel('country')
    plt.ylim(-30, 90)
    plt.yticks(xticks, xticks)
    plt.xticks(entry, team)

    plt.bar(entry, wins, width=0.9, color='black')
    plt.bar(entry, ties, width=0.9, color='green', bottom=wins)
    plt.bar(entry, loss, width=0.9, color='red')
    plt.gca().tick_params(axis='both', direction='in')
    plt.grid(which='both', axis='both',alpha=0.5,zorder=-1)
    plt.tight_layout()
    plt.show()

#horiz_plotting()

