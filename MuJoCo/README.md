
# MuJoCo Games

All the code files you need to replicate our experiments are released in the folder `src`.

For configuration, please run:
```
pip install -r requirments.txt
```

## Training Curiosity-Driven and Victim-Aware Adversarial Policies:

- Our attack: please run 
```
cd src
python adv_train.py --env <env_id> --vic_agt_id <vic_agt_id> --explore <explore> --algorithm rnd_policy
```
- Baseline attack: please run
```
python adv_train.py --env <env_id> --vic_agt_id <vic_agt_id> --algorithm regular
```
In the above scripts, `<env_id>` specifies the game environment, the options are as follows:
| env_id | Environment |
| ------ | ----------- |
| 0      |  RunToGoalAnts-v0           |
| 1      |  RunToGoalHumans-v0           |
| 2      |  YouShallNotPassHumans-v0           |
| 3      |  KickAndDefend-v0           |
| 4      | SumoAnts-v0            |
| 5      |  SumoHumans-v0           |

`<vic_agt_id>` specifies the victim policy under attacking (The exact choices for each game are shown in ```adv_train.py```). ```adv_train.py``` also gives the descriptions and default values for other hyper-parameters.
 
After training, the trained models and tensorboard logs are saved into the folder `../agent-zoo/<env_id>`.

## Retraining of Victim Agents:

The adversarial model used for the retraining experiments in the `../our agent/attack/` folder. The weights of the adversarial policy networks are named as ```model.pkl```, and the mean and variance of the observation normalization is named as ```obs_rms.pkl```.
- Run the ```python victim_train.py --env <env_id> --vic_agt_id <vic_agt_id> --adv_path <path-of-advesaries-model> --adv_obs_normpath <path-of-adversaries-observation-normalization> --is_rnd Ture ```. It is noticed that the choice of 'vic_agt_id' should be consistent with that in adversarial training.
- After training, the trained models and tensorboard logs are saved into the folder ``` ../victim-agent-zoo/XXX ```, where XXX is the name of environments.

## Evaluation:

- Playing the adversarial agent with a regular victim agent: ``` python test_masked_victim.py --env <env_id> --opp_path <path-of-the-opponent-agent> --norm_path <path-of-the-opponent-observation-normalization> --vic_path <path-of-the-victim-agent> --vic_mask False --is_rnd True```.
- Playing the adversarial agent with a masked victim agent: ``` python test_masked_victim.py --env <env_id> --opp_path <path-to-the-opponent-agent> --norm_path <path-to-the-opponent-observation-normalization> --vic_path <path-to-the-victim-agent> --vic_mask True --is_rnd True```.

## Visualizing the winning and non-loss rate of the adversarial agents/retrained victim agents:
Visualizing the winning and non-loss rate of the adversarial agents:
- Run ``` python calnon_loss.py``` in ```../rnd_result``` folder to obtain the non-loss rates of adversarial agents.
- Run ```python plot2.py```.

Visualizing the winning and non-loss rate of the retrained victim agents:
- Run ``` python calnon_loss.py``` in ```../rnd_result/retrain_win``` folder to obtain the non-loss rates of the retrained victim agents.
- Run ```python retrain_plot.py```.

## Visualizing the t-SNE:

- Run ```python generate_activations.py --env <env_id> --opp_path <path-to-the-opponent-agent> --vic_path <path-to-the-victim-agent> --norm_path <path-to-the-opponent-observation-normalizations> --out_dir <output folder>``` to collect the victim activations when playing against different opponents.
- Run ```python plot_tsne.py --dir <path-to-victim-activations> --output_dir <output-folder>``` to generate the results of t-SNE visualization.



