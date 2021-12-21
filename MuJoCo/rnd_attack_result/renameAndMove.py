import os
import shutil

# algo = 'SAC'
envs = ['KickAndDefend', 'RunToGoalAnts', 'SumoAnts', 'SumoHumans', 'YouShallNotPass']
for _, dirs, files in os.walk('./'):
    for file in files:
        name = file.split('.')
        if name[-1] != 'csv':
            continue
        pattens = file.split('_')
        if '-' in pattens[0]:
            env = pattens[0].split('-')[1].split('N')[0]
            seed = pattens[1].split('-')[1][-1]
        else:
            env = pattens[1].split('N')[0]
            # print(pattens[2])
            seed = pattens[2].split('-')[1][-1]
        print(seed)
        # if env not in dirs:
            # print('mkdir {}'.format(env))
            # os.system('mkdir {}'.format(env))
            # dirs.append(env)
        # new_name = env + '_' + algo +'_' + seed  + '.csv'
        # print(new_name)
        # os.rename(file, new_name)
        # shutil.move(new_name, './' + env)
    break
# envs = ['KickAndDefend']
#
# for env in envs:
#     d = './rnd_attack_tie/' + env
#
#     for _, dirs, _ in os.walk(d):
#         break
#     for dir in dirs:
#         for _, _, files in os.walk(d+'/' + dir):
#             break
#         for file in files:
#             seed = file.split('-')[2][0]
#             new_name = seed+'.csv'
#             print(file.split('-'))
#             print(seed)
#             os.rename(d +'/'+dir+'/' + file, d+'/' + dir + '/' + new_name)
