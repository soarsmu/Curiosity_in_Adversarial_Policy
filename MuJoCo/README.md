
# MuJoCo Tasks

## Training Clean agents:

- Please run 
```
cd src
python mujoco_cql.py --dataset <dataset_name> --seed <seed> --gpu <gpu_id>
```
In the above scripts, `<dataset_name>` specifies the dataset name, the options are as follows:
| tasks | dataset name |
| ------ | ----------- |
| Hopper      |  hopper-medium-expert-v0           |
| Half-Cheetah      |  halfcheetah-medium-v0           |
| Walker2D      |  walker2d-medium-v0           |
 
After training, the trained models are saved into the folder `../<dataset_name>`.

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



