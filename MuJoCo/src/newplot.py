import seaborn as sns
import matplotlib.pyplot as plt
import numpy as py
import pandas as pd
import os

# YouShallNotPass
# SumoHumans
# SumoAnts
# KickAndDefend
env = 'YouShallNotPass'
log_dir = './eval_results/YouShallNotPass'
env_dir = '/home/gc/attack_rl/rl_adv_valuediff/MuJoCo/adv-baseline/icml2021/YouShallNotPass'
for _, dirs, files in os.walk(log_dir):
    break
for _, seeds, _ in os.walk(env_dir):
    break
timestep = [] 
for seed in seeds:
    ckp_dir = env_dir + '/' + seed + '/checkpoints'
    for _, times, _ in os.walk(ckp_dir):
        break;
    for i in range(len(times)):
        times[i] = int(times[i])
    times.sort()
    timestep.append(times)
agent0wins = []
agent1wins = []
ties = []
i = 0
pds = []
for fl in files:
    with open(log_dir +'/'+fl, 'r') as f:
        data = f.readlines()
        a0w = []
        a1w = []
        tie = []
        a1_NF = []
        for line in data:
            line = line.strip(' ').strip('\n').strip(' ')
            line = line.split(':')
            if 'win_0'  in line[0]:
                a0w.append(float(line[1]))
            if 'win_1' in line[0]:
                a1w.append(float(line[1]))
            if 'tie' in line[0]:
                tie.append(float(line[1]))
        for c in range(len(a1w)):
            a1_NF.append(a1w[c] + tie[c])
        agent0wins.append(a0w)
        agent1wins.append(a1w)
        ties.append(tie)
        #print(len(a0w))
        #print(len(a1w))
        #print(len(tie))
        pd1 = pd.DataFrame()
        pd2 = pd.DataFrame()
        pd1['timestep'] = timestep[0]
        pd2['timestep'] = timestep[0]
        pd1['ratio'] = a0w
        pd2['ratio'] = a1w
        pd1['ratio2'] = a0w
        pd2['ratio2'] = a1_NF
        pd1['type'] = 'victim'
        pd2['type'] = 'adversary'
        pds.append(pd.concat([pd1,pd2]))
df = pd.concat(pds)
df.index = list(range(len(df)))
sns.lineplot(data=df, x='timestep', y='ratio', hue='type')
plt.savefig(env+'_win.pdf')
plt.close()
sns.lineplot(data=df, x='timestep', y='ratio2', hue='type')
plt.savefig(env+'_NF.pdf')
plt.close()
