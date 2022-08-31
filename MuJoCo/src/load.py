from zoo_utils import load_from_file, load_from_model
import tensorflow as tf
param1 = load_from_model(param_pkl_path='./models/model_baseline.pkl')
adv_agent_varibles = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope='model')
print(adv_agent_varibles)
