# MuJoCo Games

## Install MuJoCo Environment

XXX

## Training Curiosity-Driven and Victim-Aware Adversarial Policies

- Our attack: Run the ``` python adv_train.py --env <env_id> --vic_agt_id <vic_agt_id> --vic_coef_init 1 --adv_coef_init -1 --explore <explore> --algorithm rnd_policy```.
- Baseline attack: ``` python adv_train.py --env <env_id> --vic_agt_id <vic_agt_id> --vic_coef_init 1 --adv_coef_init -1 --algorithm regular```.
- 'env' specifies the game environment, 'vic_agt_id' specifies the victim policy under attacking (The exact choices for each game are shown in ```adv_train.py```). ```adv_train.py``` also gives the descriptions and default values for other hyper-parameters.
- After training, the trained model and tensorboard logs are saved into the fold ``` ../agent-zoo/XXX ```, where XXX is the name of environments.
- Visualization of tensorboard logs: ``` tensorboard --logdir=XXX ```, where XXX is the fold of tensorboard logs.

## Retraining of Victim Agents:

- We put the adversarial model used for the retraining in the ```../our agent/attack/``` folder. The weights of the policy network are named as ```model.pkl```, the mean and variance of the observation normalization as ```obs_rms.pkl```.
- Run the ```python victim_train.py --env <env_id> --vic_agt_id <vic_agt_id> --adv_path <path-to-trained-advesaries-model> --adv_obs_normpath <path-to-trained-adversaries-observation-normalization> --vic_coef_init 1 --adv_coef_init -1 --is_rnd Ture ```. It is noticed that the choice of 'vic_agt_id' should be kept the same with that in ```adv_train.py```.
- After training, the trained model and tensorboard logs are saved into the fold ``` ../victim-agent-zoo/XXX ```, where XXX is the name of environments.

## Evaluation

- Playing the adversarial agent with a regular victim agent: ``` python test_masked_victim.py --env <env_id> --opp_path <path-to-the-opponent-model> --norm_path <path-to-the-opponent-observation-normalization> --vic_path <path-to-the-victim-model> --vic_mask <False> ```.
- Playing the adversarial agent with a masked victim agent: ``` python test_masked_victim.py --env <env_id> --opp_path <path-to-the-opponent-model> --norm_path <path-to-the-opponent-observation-normalization> --vic_path <path-to-the-victim-model> --vic_mask <True> ```.

## Visualizing the winning and non-loss rate of the adversarial agents/retrained victim agents:

- Run ``` python calnon_loss.py``` in ```./rnd_result``` fold to obtain the non-loss rates.
- Run ```python plot.py```.

## Visualizing the t-SNE:

- Run ```python generate_activations.py --env <env_id> --opp_path <path-to-the-opponent-model> --vic_path <path-to-the-victim-model> --norm_path <path-to-the-opponent-observation-normalizations> --opp_type <type-of-the-opponent> --out_dir <output folder>``` to collect the victim activations when playing against different opponents.
- Run ```python plot_tsne.py --dir <path-to-victim-activations> --output_dir <output-folder>``` to generate the results of t-SNE visualization.



