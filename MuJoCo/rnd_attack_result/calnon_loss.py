import numpy as np
import os
envs = ['KickAndDefend', 'RunToGoalAnts', 'SumoAnts', 'SumoHumans', 'YouShallNotPass']
algos = ['attack1 ', 'attack2 ', 'our attack']
tie_prefix = 'rnd_attack_tie'
win_prefix = 'rnd_attack_win'
non_loss_prefix = './rnd_attack_nonloss'
os.mkdir(non_loss_prefix)
for env in envs: 
    os.mkdir(non_loss_prefix +'/' + env +'/')

for env in envs: 
    for algo in algos:
        os.mkdir(non_loss_prefix +'/' + env +'/' + algo)

for env in envs:
    for algo in algos:
        for _, _, files in os.walk(tie_prefix + '/' + env+'/' + algo):
            break
        for file in files:
            tie = []
            win = []
            non_loss = [] 
            with open(tie_prefix + '/' + env +'/' + algo +'/' + file) as f:
                data = f.readlines()
            for line in data[1:]:
                tie.append(float(line.strip(' ').strip('\n').strip(' ').split(',')[-1]))
            with open(win_prefix + '/' + env +'/' + algo +'/' + file) as f:
                data = f.readlines()
            for line in data[1:]:
                win.append(float(line.strip(' ').strip('\n').strip(' ').split(',')[-1]))
            for i in range(len(win)):
                non_loss.append(win[i] + tie[i])
            with open(non_loss_prefix +'/' + env + '/' + algo +'/' + file, 'a+') as f:
                f.write('title')
                f.write('\n')
                for c in non_loss:
                    f.write(',,{}'.format(c))
                    f.write('\n')