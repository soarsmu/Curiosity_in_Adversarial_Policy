
# MuJoCo Games

All the code files you need to replicate our experiments are released in the folder `src`.

## Environment Installation (for conda)

* Create a virtual environment: `conda create -n rnd_attack python==3.6 --channel conda-forge` (python 3.7 also works)
* Activate this environment: `conda activate rnd_attack`
* Install Scikit-learn package: `pip install -U scikit-learn`
* Run `pip install tensorflow==1.14 mujoco-py==0.5.7 pyparsing==2.4.7`
* Install openmpi package: `sudo apt-get update && sudo apt-get install cmake libopenmpi-dev zlib1g-dev`
* Install OpenGL package: 
```
sudo apt-get install build-essential libgl1-mesa-dev libglew-dev libsdl2-dev libsdl2-image-dev libglm-dev libfreetype6-dev libglfw3-dev libglfw3 libglu1-mesa-dev 
```
* Run `git config --global url."https://".insteadOf git://`
* Run `pip install git+git://github.com/HumanCompatibleAI/baselines.git@f70377#egg=baselines`
* Run `pip install git+git://github.com/HumanCompatibleAI/baselines.git@906d83#egg=stable-baselines`
* Run `pip install git+git://github.com/HumanCompatibleAI/gym.git@1918002#wheel=gym`
(It is noticed that you will encounter an error about a conflict of the required version of the gym. Please just ignore this error. It wouldn't impede the running.)
* Move `gym_compete.zip` in this folder into `<your-conda-path>/envs/rnd_attack/lib/python3.X/site-packages/` (e.g., if your python version is 3.7, the path will be `<your-conda-path>/envs/rnd_attack/lib/python3.7/site-packages/`).
* Run `unzip gym_compete.zip`. After that You will find two folders `gym_compete` and `gym_compete-0.0.1.dist-info` in `anaconda3/envs/rnd_attack/lib/python3.X/site-packages/`

It is noticed that the version of MuJoCo is 1.3.1. For the installation of MuJoCo, pls run:
```
cd ~
wget https://www.roboti.us/download/mjpro131_linux.zip
mkdir ~/.mujoco
mv mjpro131_linux.zip ~/.mujoco/
cd ~/.mujoco 
unzip mjpro131_linux.zip 
wget https://www.roboti.us/file/mjkey.txt
cp mjkey.txt mjpro131
```

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

We release model parameters of adversaril policies and retrained victims in folder `our agent`. Readers can play the adversarial agent with a regular victim agent: 
```
python test_masked_victim.py --env <env_id> --opp_path <path-of-the-opponent-agent> --norm_path <path-of-the-opponent-observation-normalization> --vic_path <path-of-the-victim-agent> --vic_mask False --is_rnd True
```
```
python test_masked_victim.py --env <env_id> --opp_path <path-to-the-opponent-agent> --norm_path <path-to-the-opponent-observation-normalization> --vic_path <path-to-the-victim-agent> --vic_mask True --is_rnd True
```
```
Winner: Agent 0, Scores: [63, 30], Total Episodes: 93
-----Episode 94-----
Winner: Agent 0, Scores: [64, 30], Total Episodes: 94
-----Episode 95-----
Winner: Agent 0, Scores: [65, 30], Total Episodes: 95
-----Episode 96-----
Winner: Agent 0, Scores: [66, 30], Total Episodes: 96
-----Episode 97-----
Winner: Agent 1, Scores: [66, 31], Total Episodes: 97
-----Episode 98-----
Winner: Agent 1, Scores: [66, 32], Total Episodes: 98
-----Episode 99-----
Winner: Agent 0, Scores: [67, 32], Total Episodes: 99
-----Episode 100-----
Winner: Agent 1, Scores: [67, 33], Total Episodes: 100
```
The scores [67, 33] indicates that player 1 and player 2 win 67 and 33 times in the 100 rounds. So, the winning rate of player 1 is 67%, and 33% for player 2.
Playing the adversarial agent with a masked victim agent: 


## Visualizing the winning rate of the adversarial agents/retrained victim agents:
 
To visualize the winning and non-loss rate of the adversarial agents, please open the tensorboard logs saved into the folder `../agent-zoo/` and execute `tensorboard --logdir=<tensorboard file>`. This repository presents examples of tensorboard logs in the folder `tensorboard_records`. We list a part of them as follows: 
![images](https://github.com/2019ChenGong/Curiosity_in_Adversarial_Policy/blob/main/MuJoCo/tensorboard_records/images/github_images.jpg)
Please interested readers refer to the folder `tensorboard_records` for more examples.

## Visualizing the t-SNE:

To collect the victim activations when playing against different opponents:
```
python generate_activations.py --env <env_id> --opp_path <path-to-the-opponent-agent> --vic_path <path-to-the-victim-agent> --norm_path <path-to-the-opponent-observation-normalizations> --out_dir <output folder>
``` 

To generate the results of t-SNE visualization:
```
python plot_tsne.py --dir <path-to-victim-activations> --output_dir <output-folder>
```


An attacker can manipulate the victim agent's observation by taking uncommon actions to lead the game into unfamiliar states, and as a result making the victim exhibit undesired sub-optimal behaviours. Pls readers go into the folder `video` for more videos.
![images](https://github.com/2019ChenGong/Curiosity_in_Adversarial_Policy/blob/main/MuJoCo/video/kick_adv.gif)
