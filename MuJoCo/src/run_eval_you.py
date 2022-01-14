import os
import argparse



if not os.path.exists('/attack_rl/rl_adv_valuediff/MuJoCo/src/eval_results/'):
    os.mkdir('eval_results')
if not os.path.exists('/attack_rl/rl_adv_valuediff/MuJoCo/src/eval_results/YouShallNotPass'):
    os.mkdir('/attack_rl/rl_adv_valuediff/MuJoCo/src/eval_results/YouShallNotPass')
for _, seeds_dir, _ in os.walk('/attack_rl/rl_adv_valuediff/MuJoCo/adv-baseline/2021/YouShallNotPass'):
    break

for seed in seeds_dir:
    for _, checkpoints_dir, _ in os.walk('/attack_rl/rl_adv_valuediff/MuJoCo/adv-baseline/2021/YouShallNotPass/{}/checkpoints/'.format(seed)):
        break;
    checkpoints_dir.sort()
    for ckp in checkpoints_dir:
        pi0_path='/attack_rl/rl_adv_valuediff/MuJoCo/multiagent-competition/agent-zoo/you-shall-not-pass/agent2_parameters-v1.pkl'
        pi0_norm_path="/attack_rl/rl_adv_valuediff/MuJoCo/multiagent-competition/agent-zoo/you-shall-not-pass/agent2_parameters-v1.pkl"
        pi1_path = '/attack_rl/rl_adv_valuediff/MuJoCo/adv-baseline/2021/YouShallNotPass/{}/checkpoints/{}/model.pkl'.format(seed, ckp)
        pi1_norm_path = '/attack_rl/rl_adv_valuediff/MuJoCo/adv-baseline/2021/YouShallNotPass/{}/checkpoints/{}/obs_rms.pkl'.format(seed,ckp)
        log = '/attack_rl/rl_adv_valuediff/MuJoCo/src/eval_results/YouShallNotPass/{}-victim-1.log'.format(seed)
        fk = 'eval.py --pi0_path={} --pi0_norm_path={} --pi1_path={} --pi1_norm_path={} --log={} --env=2'.format(pi0_path, pi0_norm_path, pi1_path, pi1_norm_path, log)
        os.system('/anaconda3/envs/mujoco2/bin/python {}'.format(fk))
#       os.system('/data/anaconda3/bin/python {}'.format(fk))
