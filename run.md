# MuJoCo Games

## Install MuJoCo Environment

XXX

## Training Curiosity-Driven and Victim-Aware Adversarial Policies

- Our attack: Run the ``` python adv_train.py --env <env_id> --vic_agt_id <vic_agt_id> --vic_coef_init 1 --adv_coef_init -1 --explore <explore> --algorithm rnd_policy```.
- Baseline attack: ``` python adv_train.py --env <env_id> --vic_agt_id <vic_agt_id> --vic_coef_init 1 --adv_coef_init -1 --algorithm regular```.
- 'env' specifies the game environment, 'vic_agt_id' specifies the victim policy under attacking (The exact choices for each game are shown in ```adv_train.py```). ```adv_train.py``` also gives the descriptions and default values for other hyper-parameters.
- After training, the trained model and tensorboard logs are saved into the fold ``` ../agent-zoo/XXX ```, where XXX is the name of environments.
- Visualization of tensorboard logs: ``` tensorboard --logdir=XXX ```, where XXX is the fold of tensorboard logs.
