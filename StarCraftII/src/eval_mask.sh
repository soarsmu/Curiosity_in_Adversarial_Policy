python -m bin.evaluate_vs_rl --mask_victim=True --model_path='./model/baseline_model/checkpoint-1200000' > our_base_T_log 2>&1 &
python -m bin.evaluate_vs_rl --mask_victim=False --model_path='./model/baseline_model/checkpoint-1200000' > our_base_F_log 2>&1 &
