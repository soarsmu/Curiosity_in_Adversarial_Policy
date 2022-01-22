## Intro

This is the codebase for 'Curiosity-Driven and Victim-Aware Adversarial Policies'.

## Project structure

The structure of this project is as follows：
```
MuJoCo
    -- src
        -- adv_train.py ------------------ train the adversarial agents using our approach.
        -- victim_train.py ------------------ retrain the victim agents.
        -- test_masked_victim.py ------------------ play the adversarial agent with a regular victim agent or mask victim agent.
        -- generate_activations.py ------------------ collect the victim activations when playing against different opponents.
        -- rnd_result
            -- calnon_loss.py ------------------ obtain the non-loss rates of adversarial agents.
            -- plot2.py ------------------ visualize the performance of adversarial agents.
            -- retrain_win
                -- calnon_loss.py ------------------ obtain the non-loss rates of retrained victim agents.
                -- retrain_plot.py ------------------ visualize the performance of retrained victim agents.
    -- our agent
        -- attack ------------------ the policy network weights of adversarial agents.
        -- retrained ------------------ the policy network weights of retrained victim agents.
    -- adv-agent
        -- baseline ------------------ the policy network weights of adversarial agents trained by baseline approach.
        
StarCraft II
    -- src
        -- bin
            -- advtrain_ppo.py ------------------ train the adversarial agents using our attack.
            -- advtrain_baseline.py ------------------ train the adversarial agents using baseline attack.
            -- adv_mixretrain_rnd.py ------------------ retrain the victim agents.
            -- evaluate_vs_rl.py ------------------ play against an adversarial agent with a regular victim agent or a masked victim agent.
            -- generate_activations.py ------------------ collect the victim activations when playing against different opponents.
            -- plot_tsne.py ------------------ generate the results of t-SNE visualization.
        -- our_plot.py ------------------ visualize the performance of adversarial agents or retrained victim agents.
        -- model
            -- baseline_model ------------------ the policy network weights of adversarial agents using baseline approach.
            -- our_attack_model ------------------ the policy network weights of adversarial agents using our approach.
            -- retrain_model ------------------ the policy network weights of retrained victim agents.
    -- normal-agent ------------------ the initial parameters of adversarial agents.
            
```

## How to run

⚠️ The commands for running each code scripts and replicate our experiments can be found in `README.md` under each subfolder. 
