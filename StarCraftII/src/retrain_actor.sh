for i in $(seq 0 20);
    do python -m bin.adv_mixretrain_ppo --job_name=actor --save_dir='./retrain_actor' --learner_ip localhost &
done;
