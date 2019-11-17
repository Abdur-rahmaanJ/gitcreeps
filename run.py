from gitcreeps import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#clean_data = get_clean_data('data/cpython_log.txt')
#to_json_file(clean_data, 'data/cpython_log.json')

#names = ["Abdur-Rahmaan Janhangeer", "Abdur-RahmaanJ", "arj"]
#merge_names(clean_data, names, default="Abdur-RahmaanJ")


#plot_user(clean_data, "Tim Peters", alpha=0.05)

clean_data = get_clean_data('data/cpython_log.txt')
names = top_committers('data/cpython_log.txt', 30, return_names=True)
save_users_plot(clean_data, names, alpha=0.03)