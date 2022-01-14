for i in $(seq 0 20); 
    do python -m bin.advtrain_ppo --job_name=actor --vic_coef_init 1 --adv_coef_init -1 \
        --init_model_path '../normal-agent/checkpoint-100000' --save_dir './actor_model' --learner_ip localhost & 
done;
