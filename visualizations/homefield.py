import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as mpl

#mpl.rcParams['text.usetex'] = True

def calculate_error(win, tie, loss):
    num = (np.sqrt(win) + 0.5*np.sqrt(tie)) / (win + 0.5*tie)
    den = (np.sqrt(win) + np.sqrt(tie) + np.sqrt(loss)) / (win + tie + loss)

    error = num + den
    return error

# Load in CSV file
f = pd.read_csv('../datasets/results_modified.csv')

# Create masks for international friendlies and tournament style matches
mask1 = f['tournament'] == 'Friendly'
mask2 = f['tournament'] != 'Friendly'
friendly = f[mask1]
tourney  = f[mask2]

# The question here is to find if playing in one's home country has a positive effect on win percentage
# Therefore, there are three cases to look at:
#       Neutral - Neither team is playing in their home country
#       Home    - The home team is playing in their home country
#       Away    - The away team is playing in their home country
neut_friendly = friendly[(friendly['home_team'] != friendly['country']) & (friendly['away_team'] != friendly['country'])]
home_friendly = friendly[(friendly['home_team'] == friendly['country']) & (friendly['away_team'] != friendly['country'])]
away_friendly = friendly[(friendly['away_team'] == friendly['country']) & (friendly['home_team'] != friendly['country'])]
neut_tourney  = tourney[(tourney['home_team'] != tourney['country']) & (tourney['away_team'] != tourney['country'])]
home_tourney  = tourney[(tourney['home_team'] == tourney['country']) & (tourney['away_team'] != tourney['country'])]
away_tourney  = tourney[(tourney['away_team'] == tourney['country']) & (tourney['home_team'] != tourney['country'])]

# For neutral games, the home and away scores are straightforward
nf_home_score = np.array(neut_friendly['home_score'])
nf_away_score = np.array(neut_friendly['away_score'])
nt_home_score = np.array(neut_tourney['home_score'])
nt_away_score = np.array(neut_tourney['away_score'])
# For games where the home team in in their home country
hf_home_score = np.array(home_friendly['home_score'])
hf_away_score = np.array(home_friendly['away_score'])
ht_home_score = np.array(home_tourney['home_score'])
ht_away_score = np.array(home_tourney['away_score'])
# For games where the away team in in their home country
#   So, use the away team as the "home" team
af_home_score = np.array(away_friendly['away_score'])
af_away_score = np.array(away_friendly['home_score'])
at_home_score = np.array(away_tourney['away_score'])
at_away_score = np.array(away_tourney['home_score'])

# Initialize win, loss and tie counters
win_nf = 0; tie_nf = 0; los_nf = 0
win_hf = 0; tie_hf = 0; los_hf = 0
win_af = 0; tie_af = 0; los_af = 0
win_nt = 0; tie_nt = 0; los_nt = 0
win_ht = 0; tie_ht = 0; los_ht = 0
win_at = 0; tie_at = 0; los_at = 0

# Loop through each case and determine if the home team won, lost or tied
for game in range(0, len(nf_home_score)):
    if (nf_home_score[game] > nf_away_score[game]):
        win_nf += 1
    elif (nf_home_score[game] == nf_away_score[game]):
        tie_nf += 1
    elif (nf_home_score[game] < nf_away_score[game]):
        los_nf += 1
    else:
        print('No team won or lost and there was no tie')
        exit()

for game in range(0, len(nt_home_score)):
    if (nt_home_score[game] > nt_away_score[game]):
        win_nt += 1
    elif (nt_home_score[game] == nt_away_score[game]):
        tie_nt += 1
    elif (nt_home_score[game] < nt_away_score[game]):
        los_nt += 1
    else:
        print('No team won or lost and there was no tie')
        exit()

for game in range(0, len(hf_home_score)):
    if (hf_home_score[game] > hf_away_score[game]):
        win_hf += 1
    elif (hf_home_score[game] == hf_away_score[game]):
        tie_hf += 1
    elif (hf_home_score[game] < hf_away_score[game]):
        los_hf += 1
    else:
        print('No team won or lost and there was no tie')
        exit()

for game in range(0, len(ht_home_score)):
    if (ht_home_score[game] > ht_away_score[game]):
        win_ht += 1
    elif (ht_home_score[game] == ht_away_score[game]):
        tie_ht += 1
    elif (ht_home_score[game] < ht_away_score[game]):
        los_ht += 1
    else:
        print('No team won or lost and there was no tie')
        exit()

for game in range(0, len(af_home_score)):
    if (af_home_score[game] > af_away_score[game]):
        win_af += 1
    elif (af_home_score[game] == af_away_score[game]):
        tie_af += 1
    elif (af_home_score[game] < af_away_score[game]):
        los_af += 1
    else:
        print('No team won or lost and there was no tie')
        exit()

for game in range(0, len(at_home_score)):
    if (at_home_score[game] > at_away_score[game]):
        win_at += 1
    elif (at_home_score[game] == at_away_score[game]):
        tie_at += 1
    elif (at_home_score[game] < at_away_score[game]):
        los_at += 1
    else:
        print('No team won or lost and there was no tie')
        exit()

#print(win_nf, tie_nf, los_nf)
#print(win_nt, tie_nt, los_nt)
#print(win_hf, tie_hf, los_hf)
#print(win_ht, tie_ht, los_ht)
#print(win_af, tie_af, los_af)
#print(win_at, tie_at, los_at)

# Individual totals
total_nf = win_nf + tie_nf + los_nf
total_nt = win_nt + tie_nt + los_nt
total_hf = win_hf + tie_hf + los_hf
total_ht = win_ht + tie_ht + los_ht
total_af = win_af + tie_af + los_af
total_at = win_at + tie_at + los_at

# Combining distinctions on which team was the "home" team
combined_wins_f = win_hf + win_af
combined_ties_f = tie_hf + tie_af
combined_loss_f = los_hf + los_af
combined_wins_t = win_ht + win_at
combined_ties_t = tie_ht + tie_at
combined_loss_t = los_ht + los_at
combined_total_f = combined_wins_f + combined_ties_f + combined_loss_f
combined_total_t = combined_wins_t + combined_ties_t + combined_loss_t

# Combining friendly and tournament statistics
combined_wins = combined_wins_f + combined_wins_t
combined_ties = combined_ties_f + combined_ties_t
combined_loss = combined_loss_f + combined_loss_t
combined_total = combined_total_f + combined_total_t
combined_neutral_wins  = win_nf + win_nt
combined_neutral_ties  = tie_nf + tie_nt
combined_neutral_loss  = los_nf + los_nt
combined_neutral_total = total_nf + total_nt

# Individual win percentage
wp_nf = (win_nf + 0.5*tie_nf) / total_nf
wp_nt = (win_nt + 0.5*tie_nt) / total_nt
wp_hf = (win_hf + 0.5*tie_hf) / total_hf
wp_ht = (win_ht + 0.5*tie_ht) / total_ht
wp_af = (win_af + 0.5*tie_af) / total_af
wp_at = (win_at + 0.5*tie_at) / total_at

wp_nf_error = calculate_error(win_nf,tie_nf,los_nf)
wp_nt_error = calculate_error(win_nt,tie_nt,los_nt)
wp_hf_error = calculate_error(win_hf,tie_hf,los_hf)
wp_ht_error = calculate_error(win_ht,tie_ht,los_ht)
wp_af_error = calculate_error(win_af,tie_af,los_af)
wp_at_error = calculate_error(win_at,tie_at,los_at)

# Combining home win percentages
wp_combined_f = (combined_wins_f + 0.5*combined_ties_f) / combined_total_f
wp_combined_t = (combined_wins_t + 0.5*combined_ties_t) / combined_total_t

wp_combined_f_error = calculate_error(combined_wins_f,combined_ties_f,combined_loss_f)
wp_combined_t_error = calculate_error(combined_wins_t,combined_ties_t,combined_loss_t)

# Combining friendlies and tournaments
wp_combined         = (combined_wins + 0.5*combined_ties) / combined_total
wp_combined_neutral = (combined_neutral_wins + 0.5*combined_neutral_ties) / combined_neutral_total

wp_combined_error         = calculate_error(combined_wins,combined_ties,combined_loss)
wp_combined_neutral_error = calculate_error(combined_neutral_wins,combined_neutral_ties,combined_neutral_loss)

# Make the figure
tick_labels = ['Tournament', 'Friendly', 'Tournament', 'Friendly']

neutral       = [wp_nt, wp_nf]
neutral_error = [wp_nt_error, wp_nf_error]
combined       = [wp_combined_t, wp_combined_f]
combined_error = [wp_combined_t_error, wp_combined_f_error]
total       = [wp_combined_neutral, wp_combined,0]
total_error = [wp_combined_neutral_error, wp_combined_error,0]
n_entries = [i for i in range(0, len(neutral))]
h_entries = [i for i in range(len(neutral), len(combined)+len(neutral))]
t_entries = [i for i in range(0, len(total))]

halfs = [i/2 for i in range(1,13,4)]

figure = plt.figure(figsize=(10,5))
figure.add_subplot(111)

plt.subplot(111)
plt.title('Does Playing In Your Home Country\n Improve Your Chances Of Winning?', fontsize=24, weight='bold')
plt.ylabel(r"$\frac{No. Wins + No. Ties/2}{No. Total Games Played}$", fontsize=16)
plt.bar(n_entries, neutral , color='#b2df8a', zorder=3, width=0.7, alpha=0.5, yerr=neutral_error , label='')#, alpha=0.7)
plt.bar(h_entries, combined, color='#a6cee3', zorder=3, width=0.7, alpha=0.5, yerr=combined_error, label='')#, alpha=0.7)
plt.bar(0.5    , total[0]  , color='#33a02c', zorder=1, width=1.9, alpha=0.9, yerr=total_error[0], label='Both Teams\n In A Neutral Country')
plt.bar(2.5    , total[1]  , color='#1f78b4', zorder=1, width=1.9, alpha=0.9, yerr=total_error[1], label='Team Playing\n In Home Country')
plt.bar(4.0    , total[2]  , color='red'    , zorder=1, width=1.9, alpha=1.0, label='')
plt.gca().set_xticks(np.append(n_entries, h_entries))
plt.gca().set_xticklabels(tick_labels, fontsize=16)
plt.gca().set_ylim(0, 0.7)
plt.legend(loc='upper right', fontsize=14)
plt.grid(axis='y', alpha=0.3)

plt.annotate('Background bar\n shows combined\n win percentage for\n tournament and\n friendly matches',
             xy=(0.7,0.25), xycoords='axes fraction', xytext=(0.9,0.45), textcoords='axes fraction',
             ha='center', va='center',
             arrowprops=dict(facecolor='white',edgecolor='black',connectionstyle='arc3,rad=-0.05'),
             fontsize=14, weight='bold', color='black')


plt.tight_layout()
plt.savefig('advantage_hometeam.pdf', dpi=400)
plt.show()
