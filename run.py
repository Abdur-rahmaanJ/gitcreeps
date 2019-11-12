from gitcreeps import (
                    get_clean_data, 
                    to_json_file, 
                    merge_names, 
                    days, 
                    hour, 
                    date, 
                    day_i,
                    plot_user)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

clean_data = get_clean_data('iris_firefox.txt')
to_json_file(clean_data, 'iris_firefox.json')

#names = ["Abdur-Rahmaan Janhangeer", "Abdur-RahmaanJ", "arj"]
#merge_names(clean_data, names, default="Abdur-RahmaanJ")


plot_user(clean_data, "Serhii Pronoza")
