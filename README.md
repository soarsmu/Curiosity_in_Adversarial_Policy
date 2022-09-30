## Intro

Replication Package for "Curiosity-Driven and Victim-Aware Adversarial Policies", ACSAC 2022.

## Overview

Recent years have witnessed great potential in applying Deep Reinforcement Learning (DRL) in various challenging applications, such as autonomous driving, nuclear fusion control, complex game playing, etc. 
However, recently researchers have revealed that deep reinforcement learning models are vulnerable to adversarial attacks: malicious attackers can train *adversarial policies* to tamper with the observations of a well-trained victim agent, the latter of which fails dramatically when faced with such an attack. Understanding and improving the adversarial robustness of deep reinforcement learning is of great importance in enhancing the quality and reliability of a wide range of DRL-enabled systems. 

In this paper, we develop *curiosity-driven* and *victim-aware* adversarial policy training, a novel method that can more effectively exploit the defects of victim agents. 
To be victim-aware, we build a surrogate network that can approximate the state-value function of a black-box victim to collect the victim's information. 
Then we propose a curiosity-driven approach, which encourages an adversarial policy to utilize the information from the hidden layer of the surrogate network to exploit the vulnerability of victims efficiently. 
Extensive experiments demonstrate that our proposed method *outperforms or achieves a similar level of performance as the current state-of-the-art* across multiple environments. We perform an ablation study to emphasize the benefits of utilizing the approximated victim information. 
Further analysis suggests that our method is harder to defend against a commonly used defensive strategy, which calls attention to more effective protection on the systems using DRL.

## Project structure

The structure of this project is as follows:
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
    -- multiagent-competition ------------ the agent zoo downloaded from the package (https://github.com/openai/multiagent-competition).
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
- The well trained agent zoo are provide by [OpenAI](https://github.com/openai/multiagent-competition).
