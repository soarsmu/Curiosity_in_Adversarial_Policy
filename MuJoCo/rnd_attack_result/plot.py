from inspect import FrameInfo
from logging import Handler
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
for root, dirs ,files in os.walk('./'):
    break
envs = ['KickAndDefend', 'RunToGoalAnts', 'SumoAnts', 'SumoHumans', 'YouShallNotPass']
algos = ['attack1 ', 'attack2 ', 'our attack']
shuffixs = ['nonloss', 'win']
alpha = 0.3
def read_ratios(dir_name):
    ret = []
    for _, _, files in os.walk(dir_name):
        break
    print(files)
    for file in files:
        with open(dir_name + '/' + file) as f:
            rr = []
            data = f.readlines()
            data = data[1:]
            gap = 50
            if len(data) < 1000:
                gap = 45
            for i in range(len(data)):
                line = data[i]
                line = line.strip(' ').strip('\n').strip(' ').split(',')[-1]
                if len(line) < 1:
                    continue
                ratio = float(line)
                if i % gap == 0:
                    rr.append(ratio)
            ret.append(rr[:100])
    return ret
step = []
for i in range(int(2e7)):
    if i % int(2e5 * 5) == 0:
        step.append(i)
# print(step)
step = step 
dd = []

def calnxt(data):
    ret = np.zeros(len(data))
    ret[0] = data[0]
    for i in range(1, len(ret)):
        ret[i] = alpha * data[i] + (1-alpha) * ret[i-1]
        if ret[i] < -500.:
            ret[i] = -500.
    return ret

def caltriple(data):
    for i in range(3):
        data = calnxt(data)
    # X = calnxt(data)
    # X = calnxt(X)
    # X = calnxt(X)
    return data

sns.set_style("darkgrid")
for shuffix in shuffixs:
    for env in envs:
        dfs = [pd.DataFrame() for _ in algos]
        max_means = [] 
        for i  in range(len(algos)):
            algo = algos[i]
            dir_name = 'rnd_attack_{}/'.format(shuffix) + env+ '/' + algo
            win = read_ratios(dir_name)
            for c in range(len(win)):
                win[c] = caltriple(win[c])
            new_win = []
            for c in win:
                new_win += list(c)
            dfs[i]['ratio'] = new_win
            dfs[i]['algo'] = algo
            k = int(len(new_win)/20)
            dfs[i]['step'] = step * k
            # win = np.array(win)
            for c in range(20):
                smm = 0
                for k in win:
                    smm += k[c]
                smm = smm / len(win)
                max_means.append(smm) 
            # max_means.append(win.max())
        t = pd.concat(dfs)
        t = t.reset_index()

        ax = sns.lineplot(data = t, x = 'step', y ='ratio', hue='algo', style='algo', markers=True, dashes=False)
        t = np.array(max_means).max()
        ax.hlines(t, 0, 2e7, colors = 'green', ls = '--')
        plt.legend([], [], frameon=False)
        #plt.xticks([])
        #plt.yticks([])
        # plt.axis('off')
        #plt.ylim(0, 0.85)
        plt.xlim([0, 2e7])
        #plt.xlabel('')
        #plt.ylabel('')
        h, l = ax.get_legend_handles_labels()
        # ax.legend(handles= None, labels = None, title = None)
        plt.savefig('{}_{}.pdf'.format(env, shuffix), bbox_inches='tight')
        plt.close()
