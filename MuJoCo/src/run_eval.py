import os
if not os.path.exists('/data/gc/rl_adv/rl_adv_valuediff/MuJoCo/src/eval_results/'):
    os.mkdir('eval_results')
if not os.path.exists('/data/gc/rl_adv/rl_adv_valuediff/MuJoCo/src/eval_results/KickAndDefend'):
    os.mkdir('/data/gc/rl_adv/rl_adv_valuediff/MuJoCo/src/eval_results/KickAndDefend')
for _, seeds_dir, _ in os.walk('/data/gc/rl_adv/rl_adv_valuediff/MuJoCo/agent-zoo/baselines/KickAndDefend-v0_1_MLP_MLP_1_const_-1_const_0_const_False'):
    break
for i in range(1,4):
    for seed in seeds_dir:
        for _, checkpoints_dir, _ in os.walk('/data/gc/rl_adv/rl_adv_valuediff/MuJoCo/agent-zoo/baselines/KickAndDefend-v0_1_MLP_MLP_1_const_-1_const_0_const_False/{}/checkpoints/'.format(seed)):
            break;
        checkpoints_dir.sort()
        for ckp in checkpoints_dir:
            pi0_path='/data/gc/rl_adv/rl_adv_valuediff/MuJoCo/multiagent-competition/agent-zoo/kick-and-defend/kicker/agent1_parameters-v{}.pkl'.format(i)
            pi0_norm_path="/data/gc/rl_adv/rl_adv_valuediff/MuJoCo/multiagent-competition/agent-zoo/kick-and-defend/kicker/agent1_parameters-v{}.pkl".format(i)
            pi1_path = '/data/gc/rl_adv/rl_adv_valuediff/MuJoCo/agent-zoo/baselines/KickAndDefend-v0_1_MLP_MLP_1_const_-1_const_0_const_False/{}/checkpoints/{}/model.pkl'.format(seed, ckp)
            pi1_norm_path = '/data/gc/rl_adv/rl_adv_valuediff/MuJoCo/agent-zoo/baselines/KickAndDefend-v0_1_MLP_MLP_1_const_-1_const_0_const_False/{}/checkpoints/{}/obs_rms.pkl'.format(seed,ckp)
            log = '/data/gc/rl_adv/rl_adv_valuediff/MuJoCo/src/eval_results/KickAndDefend/{}-victim-{}.log'.format(seed, i)
            fk = 'eval.py --pi0_path={} --pi0_norm_path={} --pi1_path={} --pi1_norm_path={} --log={}'.format(pi0_path, pi0_norm_path, pi1_path, pi1_norm_path, log)
            os.system('/data/gc/anaconda3/envs/mujoco_base/bin/python {}'.format(fk))
#            os.system('/data/gc/anaconda3/bin/python {}'.format(fk))
