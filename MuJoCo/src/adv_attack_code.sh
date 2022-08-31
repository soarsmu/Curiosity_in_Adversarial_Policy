python eval.py --env 3 \ 
# pi0 is victim agent
--pi0_path /home/gc/attack_rl/rl_adv_valuediff/MuJoCo/retrained-victim/our_attack/KickAndDefend/20200818_124108-0/KickAndDefend-v0.npy \
--pi0_norm_path /home/gc/attack_rl/rl_adv_valuediff/MuJoCo/retrained-victim/our_attack/KickAndDefend/20200818_124108-0/KickAndDefend-v0.pkl \
# pi1 is adv agent
--pi1_path /home/gc/attack_rl/rl_adv_valuediff/MuJoCo/agent-zoo/KickAndDefend-v0_1_MLP_MLP_1_const_-1_const_0_const_False/20211019_141916-2/model.pkl
--pi1_norm_path /home/gc/attack_rl/rl_adv_valuediff/MuJoCo/agent-zoo/KickAndDefend-v0_1_MLP_MLP_1_const_-1_const_0_const_False/20211019_141916-2/obs_rms.pkl