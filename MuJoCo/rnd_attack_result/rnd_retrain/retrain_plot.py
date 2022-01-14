from inspect import FrameInfo
from logging import Handler
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
for root, dirs ,files in os.walk('./'):
    break
envs = ['KickAndDefend', 'SumoAnts', 'RunToGoalAnts', 'YouShallNotPass', 'SumoHumans'] #
algos = ['our attack'] # 'attack1 ', 'attack2 ',
shuffixs = ['nonloss', 'win']
sns.set_style("darkgrid")
colors = sns.color_palette()
alpha = 0.5
point_num = 60
colors = sns.color_palette()
plt.rcParams['font.family'] = "Times New Roman"
def sample(data):
    ret = []
    for i in range(len(data)):
        rr = []
        gap = int(len(data[i]) / (point_num + 1))
        for k in range(len(data[i])):
            if k % gap == 0:
                rr.append(data[i][k])
        ret.append(rr[:point_num+1])
    return ret

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
            for i in range(len(data)):
                line = data[i]
                line = line.strip(' ').strip('\n').strip(' ').split(',')[-1]
                if len(line) < 1:
                    continue
                ratio = float(line)
                rr.append(ratio)
            ret.append(rr)
    return ret

step_gap = int(2e7 / point_num)
step = []
for i in range(int(2e7) + 1):
    if i % step_gap == 0:
        step.append(i)

def calnxt(data):
    ret = np.zeros(len(data))
    ret[0] = data[0]
    for i in range(1, len(ret)):
        ret[i] = alpha * data[i] + (1-alpha) * ret[i-1]
        if ret[i] < -500.:
            ret[i] = -500.
    return ret

def caltriple(data):
    for i in range(20):
        data = calnxt(data)
    return data

for shuffix in shuffixs:
    label = 'Winning Rate'
    if shuffix == 'nonloss':
        label = 'Non-loss Rate'
    for env in envs:
        dfs = [pd.DataFrame() for _ in algos]
        max_means = []
        for i  in range(len(algos)):
            algo = algos[i]
            dir_name = 'retrain_{}/'.format(shuffix) + env+ '/' + algo
            win = read_ratios(dir_name)
#            win = sample(win)
            for c in range(len(win)):
                win[c] = caltriple(win[c])
            win = sample(win)
            new_win = []
            for c in win:
                new_win += list(c)
            dfs[i][label] = new_win
            dfs[i]['algo'] = algo
            k = int(len(win))
            dfs[i]['Timesteps'] = step * k
            means = []
            for c in range(len(win[0])):
                smm = 0
                for k in win:
                    smm += k[c]
                smm = smm / len(win)
                means.append(smm)
            means = np.array(means)
            max_means.append(means.max())
        t = pd.concat(dfs)
        t = t.reset_index()
        ax = sns.lineplot(data = t, x = 'Timesteps', y = label, hue='algo', style='algo', color = colors, markers=True, dashes=False)
#        t = np.array(max_means).max()
#        print(max_means)
        for i in range(len(algos)):
            ax.hlines(max_means[i], 0, 2e7, colors = colors[i], ls = '--')
            ax.text(0, max_means[i], '%.2f'%max_means[i], fontsize=9, verticalalignment='bottom', color = colors[i])
#        ax.hlines(max_means[1], 0, 2e7, colors = 'green', ls = '--')
#        ax.hlines(max_means[2], 0, 2e7, colors = 'green', ls = '--')
#        ax.hlines(t, 0, 2e7, colors = 'green', ls = '--')
        plt.legend([], [], frameon=False)
        #plt.xticks([])
        #plt.yticks([])
        # plt.axis('off')
        plt.ylim(0, 1)
        plt.xlim([0, 2e7 + 1e4])
        #plt.xlabel('')
        #plt.ylabel('')
        h, l = ax.get_legend_handles_labels()
        # ax.legend(handles= None, labels = None, title = None)
        plt.savefig('{}_{}.pdf'.format(env, shuffix), bbox_inches='tight')
        plt.close()
