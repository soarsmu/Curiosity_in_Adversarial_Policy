import os
import argparse



if not os.path.exists('/home/gc/attack_rl/rl_adv_valuediff/MuJoCo/src/eval_results/'):
    os.mkdir('eval_results')
if not os.path.exists('/home/gc/attack_rl/rl_adv_valuediff/MuJoCo/src/eval_results/KickAndDefend'):
    os.mkdir('/home/gc/attack_rl/rl_adv_valuediff/MuJoCo/src/eval_results/KickAndDefend')
for _, seeds_dir, _ in os.walk('/home/gc/attack_rl/rl_adv_valuediff/MuJoCo/adv-baseline/icml2021/KickAndDefend'):
    break

for seed in seeds_dir:
    for _, checkpoints_dir, _ in os.walk('/home/gc/attack_rl/rl_adv_valuediff/MuJoCo/adv-baseline/icml2021/KickAndDefend/{}/checkpoints/'.format(seed)):
        break;
    checkpoints_dir.sort()
    for ckp in checkpoints_dir:
        pi1_path='/home/gc/attack_rl/rl_adv_valuediff/MuJoCo/multiagent-competition/agent-zoo/kick-and-defend/kicker/agent1_parameters-v1.pkl'
        pi1_norm_path="/home/gc/attack_rl/rl_adv_valuediff/MuJoCo/multiagent-competition/agent-zoo/kick-and-defend/kicker/agent1_parameters-v1.pkl"
        pi0_path = '/home/gc/attack_rl/rl_adv_valuediff/MuJoCo/adv-baseline/icml2021/KickAndDefend/{}/checkpoints/{}/model.pkl'.format(seed, ckp)
        pi0_norm_path = '/home/gc/attack_rl/rl_adv_valuediff/MuJoCo/adv-baseline/icml2021/KickAndDefend/{}/checkpoints/{}/obs_rms.pkl'.format(seed,ckp)
        log = '/home/gc/attack_rl/rl_adv_valuediff/MuJoCo/src/eval_results/KickAndDefend/{}-victim-1.log'.format(seed)
        fk = 'eval.py --pi0_path={} --pi0_norm_path={} --pi1_path={} --pi1_norm_path={} --log={} --env=3'.format(pi0_path, pi0_norm_path, pi1_path, pi1_norm_path, log)
        os.system('/home/gc/anaconda3/envs/mujoco2/bin/python {}'.format(fk))
#       os.system('/data/gc/anaconda3/bin/python {}'.format(fk))
