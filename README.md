## Intro

This is the codebase for 'Curiosity-Driven and Victim-Aware Adversarial Policies'. Our paper ......

## Project structure

The structure of this project is as follows：
```
MuJoCo
    -- src
        -- adv_train.py ------------------ train the adversarial policy.
        
```

## How to run

⚠️ The commands for running each code scripts and replicate our experiments can be found in `README.md` under each subfolder. 

⚠️ For the MuJoCo games, please use a docker container with `xxxx`, i.e.,
```
docker pull xxxxxx
```
⚠️ For the StarCraft games, please pull and install the repo from: https://github.com/Tencent/PySC2TencentExtension. Then, run 
```
pip install -r requirments.txt
```
in fold ```StarCraftII``` to install the required packages. It is noticed that the version of StarCraftII is SC2 4.6.2 (B69232).
