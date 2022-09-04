
# MuJoCo Games

All the code files you need to replicate our experiments are released in the folder `src`.

## Environment Installation (for conda)

* Create a virtual evironments: `conda create -n rnd_attack python==3.6` (python 3.7 also works)
* Activate this environment: `conda activate rnd_attack`
* Install scikit-learn package: `pip install -U scikit-learn`
* Install tensorflow package: `pip install tensorflow==1.14`
* Install openmpi pacage: `sudo apt-get update && sudo apt-get install cmake libopenmpi-dev zlib1g-dev`
* Please run: `pip install -r requirments.txt` (It is noticed that you will encounter an error about a conflict of the required version of the gym. Please just ignore this error. It wouldn't impede the running. )
* Move `gym_compete.zip` in this folder into `anaconda3/envs/mujoco/lib/python3.X/site-packages/`
* Run `unzip gym_compete.zip`. After that You will find two folders `gym_compete` and `gym_compete-0.0.1.dist-info` in `anaconda3/envs/mujoco/lib/python3.X/site-packages/`.

It is noticed that the version of Mujoco is 1.3.1.

## Training Curiosity-Driven and Victim-Aware Adversarial Policies:

- Our attack: please run 
```
cd src
python adv_train.py --env <env_id> --vic_agt_id <vic_agt_id> --explore <explore> --algorithm rnd_policy
```
e.g., `python adv_train.py --env 4 --vic_agt_id 1 --explore 0.5 --algorithm rnd_policy`
- Baseline attack: please run
```
python adv_train.py --env <env_id> --vic_agt_id <vic_agt_id> --algorithm regular
```
In the above scripts, `<env_id>` specifies the game environment, the options are as follows:
| env_id | env |
| ------ | ----------- |
| 0      |  RunToGoalAnts-v0           |
| 1      |  RunToGoalHumans-v0           |
| 2      |  YouShallNotPassHumans-v0           |
| 3      |  KickAndDefend-v0           |
| 4      | SumoAnts-v0            |
| 5      |  SumoHumans-v0           |

`<vic_agt_id>` specifies the victim policy under attacking (The exact choices for each game are shown in ```adv_train.py```). ```adv_train.py``` also gives the descriptions and default values for other hyper-parameters.
 
After training, the trained models and tensorboard logs are saved into the folder `../agent-zoo/<env>`, where `<env>` is the name of environments corresponding to the `<env_id>`.

## Retraining of Victim Agents:

The adversarial model used for the retraining experiments in the `../our agent/attack/` folder. The weights of the adversarial policy networks are named as ```model.pkl```, and the mean and variance of the observation normalization is named as `obs_rms.pkl`.

For retraining:
```
python victim_train.py --env <env_id> --vic_agt_id <vic_agt_id> --adv_path <path-of-advesaries-model> --adv_obs_normpath <path-of-adversaries-observation-normalization> --is_rnd Ture
```

It is noticed that the choice of `<vic_agt_id>` should be consistent with that in adversarial training.

After training, the trained models and tensorboard logs are saved into the folder `../victim-agent-zoo/<env>`, where `<env>` is the name of environments corresponding to the `<env_id>`.

## Evaluation:

Playing the adversarial agent with a regular victim agent: 
```
python test_masked_victim.py --env <env_id> --opp_path <path-of-the-opponent-agent> --norm_path <path-of-the-opponent-observation-normalization> --vic_path <path-of-the-victim-agent> --vic_mask False --is_rnd True
```

Playing the adversarial agent with a masked victim agent: 
```
python test_masked_victim.py --env <env_id> --opp_path <path-to-the-opponent-agent> --norm_path <path-to-the-opponent-observation-normalization> --vic_path <path-to-the-victim-agent> --vic_mask True --is_rnd True
```

## Visualizing the winning and non-loss rate of the adversarial agents/retrained victim agents:
 
To visualize the winning and non-loss rate of the adversarial agents:
```
cd ../rnd_result
python calnon_loss.py
python plot2.py
``` 

To visualize the winning and non-loss rate of the retrained victim agents:
```
cd ../rnd_result/retrain_win
python calnon_loss.py
python retrain_plot.py
```

## Visualizing the t-SNE:

To collect the victim activations when playing against different opponents:
```
python generate_activations.py --env <env_id> --opp_path <path-to-the-opponent-agent> --vic_path <path-to-the-victim-agent> --norm_path <path-to-the-opponent-observation-normalizations> --out_dir <output folder>
``` 

To generate the results of t-SNE visualization:
```
python plot_tsne.py --dir <path-to-victim-activations> --output_dir <output-folder>
```


