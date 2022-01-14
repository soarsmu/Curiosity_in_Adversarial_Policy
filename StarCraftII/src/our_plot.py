import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
results_dir = './total_results'
#algos = ['baselines1', 'rnd']
algos = ['retrain']
shuffixs = ['nonloss', 'win']
sns.set_style('darkgrid')
colors = sns.color_palette()
alpha = 0.8
point_num = 60
colors = sns.color_palette()
plt.rcParams['font.family'] = 'Times New Roman'
#hello
def read_filenames(work_dir, algo):
    ret = []
    for _, _, files in os.walk(work_dir +'/' + algo):
        break;
    for f in files:
        ret.append(work_dir +'/' + algo +'/'+ f)
    return ret

def read_ratios(file_name, ty='win'):
    with open(file_name) as f:
        data = f.readlines()
        ret = []
        for line in data:
            line = line.strip(' ').strip('\n').strip(' ').split(' ') 
            if ty == 'win':
                ret.append(float(line[1]))
            else:
                ret.append(float(line[2]))
        return ret[:1501]

step_gap = int(15e5 / point_num)
step = []
for i in range(int(15e5) + 1):
    if i % step_gap == 0:
        step.append(i)

def calnxt(data):
    ret = np.zeros(len(data))
    ret[0] = data[0]
    for i in range(1, len(ret)):
        ret[i] = alpha * data[i] + (1-alpha) * ret[i-1]
    return ret

def caltriple(data):
    for i in range(3):
        data = calnxt(data)
    return data

def sample(data):
    ret = []
    for i in range(len(data)):
        rr = []
        gap = int(len(data[i])/(point_num + 1 ))
        for k in range(len(data[i])):
            if k % gap == 0:
                rr.append(data[i][k])
        ret.append(rr[: point_num + 1])
    return ret
for shuffix in shuffixs:
    label = 'Winning Rate'
    if shuffix == 'nonloss':
        label = 'Non-loss Rate'
    dfs = [pd.DataFrame() for _ in algos] 
    max_means = []
    for algo_i in range(len(algos)):
        algo = algos[algo_i]
        files = read_filenames(results_dir, algo)
        ratios = []
        for f in files:
            ratio = read_ratios(f, shuffix)
            print(ratio)
            if len(ratio) >1500:
                ratios.append(ratio)
        for c in range(len(ratios)):
            ratios[c] = caltriple(ratios[c])
        ratios = sample(ratios)
        new_ratio = []
        for c in ratios:
            new_ratio += list(c)
        dfs[algo_i][label] = new_ratio
        dfs[algo_i]['algo'] = algo
        k = int(len(ratios))
        dfs[algo_i]['Timesteps'] = step * k
        means = []
        for c in range(len(ratios[0])):
            smm=0
            for k in ratios:
                smm += k[c]
            smm = smm / len(ratios)
            means.append(smm)
        means = np.array(means)
        max_means.append(means.max())
    t=pd.concat(dfs)
    t = t.reset_index()
    ax = plt.figure(figsize=(9, 4))
    ax=sns.lineplot(data = t, x= 'Timesteps', y=label, hue='algo', style ='algo', color = colors, markers = True, dashes=False)
    for i in range(len(algos)):
        ax.hlines(max_means[i], 0, 1.5e6, colors = colors[i], ls ='--')
        ax.text(0, max_means[i], '%.2f' % max_means[i], fontsize=16, verticalalignment='bottom', color =colors[i], weight=1000)
    y_range = ax.get_yticks()
    y_min = y_range[0]
    if y_min < 0:
        y_min = 0
    y_max = 1
    new_yticks = []
    gap = (y_max - y_min) / 3.
    for i in range(3):
        new_yticks.append(float('%.2f' % float(y_min + float(i) * gap)))
    new_yticks.append(float('%.2f'%float(1.00)))
    new_yticks_str = []
    for c in new_yticks:
        new_yticks_str.append('%.1f'%c)
    plt.ticklabel_format(axis='x', style='sci', scilimits=(0,0))
    plt.xticks([0, 0.5e6, 1.0e6, 1.5e6], ['0', '0.5', '1.0', '1.5'], size=14)
    plt.yticks(new_yticks,new_yticks_str, size=14)
    plt.ylabel('', fontsize=14)
    plt.xlabel('Timesteps (1e6)', fontsize=14)
    plt.legend([], [], frameon=False)
    plt.xlim([0, 1.5e6+1e4])
    plt.savefig('{}.pdf'.format(shuffix), bbox_inches ='tight')
    plt.close()
