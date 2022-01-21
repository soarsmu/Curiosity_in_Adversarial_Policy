# StarCraft II Games

All the code files you need to replicate our experiments are released in the folder ```src```.

## Training Curiosity-Driven and Victim-Aware Adversarial Policies:

- Our attack: run ```python -m bin.advtrain_ppo --job_name learner --init_model_path '../normal-agent/checkpoint-100000' --save_dir <path-to-a-folder>``` to start the learner. Then run 
```
for i in $(seq 0 20); 
    do python -m bin.advtrain_ppo --job_name=actor \
       --init_model_path '../normal-agent/checkpoint-100000' --learner_ip localhost & 
done;
```
to start the actor, write the following instructions into a '.sh' file and run it. It is noticed that '20' refers to the number of actors.

- Baseline attack: run ```python -m bin.advtrain_baseline --job_name learner --init_model_path '../normal-agent/checkpoint-100000' --save_dir <path-to-a-folder>``` to start the learner. Then run 
```
for i in $(seq 0 20); 
    do python -m bin.advtrain_baseline --job_name=actor \
       --init_model_path '../normal-agent/checkpoint-100000' --learner_ip localhost & 
done;
```
to start the actor, write the following instructions into a '.sh' file and run it. It is noticed that '20' refers to the number of actors.

## Retraining of Victim Agents:
- We need to change the 52, 53, 84 lines of file ```bin/adv_mixretrain_rnd.py``` to assign the path of the adversarial agent, norm agent, and victim agent, respectively. 
- Run the ```python -m bin.adv_mixretrain_rnd --job_name learner --save_dir <path-to-a-folder> &``` to start the learner. Then run 
```
for i in $(seq 0 20); 
    do python -m bin.adv_mixretrain_rnd --job_name=actor --learner_ip localhost & 
done;
```
to start the actor, write the following instructions into a '.sh' file and run it. It is noticed that '20' refers to the number of actors.

## Evaluation:
- Playing an adversarial agent with a regular victim: run ```python -m bin.evaluate_vs_rl --model_path=<path-of-the-adversarial-agent> --victim_path=<path-of-the-victim-agent> --mask_victim=False``` to play against an adversarial agent with a victim to calcualte the winning and non-loss rates of adversarial agent.

- Playing an adversarial agent with a masked victim: run ```python -m bin.evaluate_vs_rl --model_path=<path-of-the-adversarial-model> --victim_path=<path-of-the-victim-model> --mask_victim=True``` to play against an adversarial with a masked victim.

## Visualizing the winning and non-loss rate of the adversarial agents/retrained victim agents:
- Put the results generated by the training ```Log.txt``` into a folder (e.g., ```../our_result```). 
- Change to line 6 in the file ```our_plot.py``` to assign the folder of results (e.g., ```../our_result```). Run ```python our_plot.py```.

## Visualizing the t-SNE:
- Run ```python -m bin.generate_activations --model_path=<path-of-the-opponent-agent> --victim_path=<path-of-the-victim-agent> --out_path=<output-folder>``` to collect the victim activations when playing against different opponents.
- Run ```python plot_tsne.py --dir <path-to-victim-activations> --output_dir <output-folder>``` to generate the results of t-SNE visualization.