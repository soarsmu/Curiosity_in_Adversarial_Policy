## Intro

This is the codebase for 'Curiosity-Driven and Victim-Aware Adversarial Policies'.

## Project structure

The structure of this project is as follows：
```
MuJoCo
    -- src
        -- adv_train.py ------------------ train the adversarial agents using our approach.
        -- victim_train.py --------------- retrain the victim agents.
        -- test_masked_victim.py --------- play the adversarial agent with a regular victim agent or mask victim agent.
        -- generate_activations.py ------- collect the victim activations when playing against different opponents.
        -- rnd_result
            -- calnon_loss.py ------------ obtain the non-loss rates of adversarial agents.
            -- plot2.py ------------------ visualize the performance of adversarial agents.
            -- retrain_win
                -- calnon_loss.py -------- obtain the non-loss rates of retrained victim agents.
                -- retrain_plot.py ------- visualize the performance of retrained victim agents.
    -- our agent
        -- attack ------------------------ the policy network weights of adversarial agents.
        -- retrained --------------------- the policy network weights of retrained victim agents.
    -- adv-agent
        -- baseline ---------------------- the policy network weights of adversarial agents trained by baseline approach.
    -- tensorboard_records ------------------ the curves recorded in tensorboard files during training adversarial policies.
    -- video ------------------ the game videos show adversarial policies and regular agents aginst with victim agents, respectively.
        
StarCraft II
    -- src
        -- bin
            -- advtrain_ppo.py ----------- train the adversarial agents using our attack.
            -- advtrain_baseline.py ------ train the adversarial agents using baseline attack.
            -- adv_mixretrain_rnd.py ----- retrain the victim agents.
            -- evaluate_vs_rl.py --------- play against an adversarial agent with a regular victim agent or a masked victim agent.
            -- generate_activations.py --- collect the victim activations when playing against different opponents.
            -- plot_tsne.py -------------- generate the results of t-SNE visualization.
        -- our_plot.py ------------------- visualize the performance of adversarial agents or retrained victim agents.
        -- model
            -- baseline_model ------------ the policy network weights of adversarial agents using baseline approach.
            -- our_attack_model ---------- the policy network weights of adversarial agents using our approach.
            -- retrain_model ------------- the policy network weights of retrained victim agents.
    -- normal-agent ---------------------- the initial parameters of adversarial agents.
    -- training_records ---------------------- the training logs recorded during training adversarial policies.
            
```

## How to run

⚠️ The configurations and scripts for replicating our experiments can be found in `README.md` under each subfolder. 

## Contact

- If you have any problems, please feel free to contact Chen Gong (ChenG_abc@outlook.com), Zhou Yang (zyang@smu.edu.sg), or Yunpeng Bai (baiyunpeng2020@ia.ac.cn).

## Acknowledgement

- The codes for training the adversarial policies are based on the [Adversarial Policy](https://github.com/psuwuxian/rl_adv_valuediff) and [Stable-Baselines](https://github.com/hill-a/stable-baselines).
