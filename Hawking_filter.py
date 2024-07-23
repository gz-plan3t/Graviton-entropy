import os
import pandas as pd
import numpy as np
import scipy.interpolate as spi
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
while True:
    print("WELCOME TO HAWKING FILTER!\nCopyright(c) Gazillo, R.G. (2024)\n\n")
    print("#     #  # # # #  #     #  #     #   # # # #   #     #  # # # #\n#     #  #     #  #     #  #   #        #      # #   #  #\n# # # #  # # # #  #  #  #  # #          #      #  #  #  #   # #\n#     #  #     #  # # # #  #   #        #      #   # #  #     #\n#     #  #     #  #     #  #     #   # # # #   #     #  # # # #\n\n")
    print(
    "# # # #  # # # #  #       # # # #  # # # #  # # # #\n#           #     #          #     #        #     #\n# # #       #     #          #     # # #    # # #\n#           #     #          #     #        #    #\n#        # # # #  # # # #    #     # # # #  #      #\n\n")
    print("\nHawking filter is a software that contains a mathematical algorithm to process gravimetric data in a novel way. This is an experiment that manipulates data from gravimetric real surveys and uses Bekenstein-Hawking Entropy formula to calculate gravitational entropies considering that each gravimetric measurement corresponds to a hypothetical value of surface gravity of an individual Schwarzschild black hole in Planck units. The algorithm reads the original dataframe from gravimetric surveys in 'csv' format and then perform the 'filtering' calculations using gravitational entropy formulas generating as output a 2D map plot of interpolated values of Log(Entropy) in Planck units versus specified X and Y space coordinates. Also, the program generates the same map with another perspective as entropy in Planck units corresponds to bits of gravitational holographic information which is in the orders of 'Giga-Googolbytes' of space-time storage capacity! A corresponding file containing the generated dataframe for entropy values is created as output so the user can import it to other data visualization softwares for customization. This approach transforms Bouguer anomaly maps into Hawking Entropy maps. This gives a new unusual visualization of gravimetric data in a tentative approach to apply theoretical physics in a highly complex scenario such as quantum gravity to real-world applications in a novel way.\nGOOD MATHEMATICAL ENDEAVOURS!!\n")
    input_file_path = filedialog.askopenfile()
    if not input_file_path:
         break
    print("\nGRAVITATIONAL ENTROPY CALCULATOR ACTIVATED\n")
    def calculate_entropy(g_value_02):
        entropy = 3.14159265 * (1/(2 * g_value_02 * 1.82e-57))**2
        log_s = np.log10(entropy)
        return log_s
    def calc_pure_entropy(g_v):
        entropy = 4 * 3.14159265 * (1/(2 * g_v * 1.82e-57))**2
        googolbyte = entropy/1.6e+109
        return googolbyte
    df_02 = pd.read_csv(input_file_path)
    third_column_02 = df_02.iloc[:, 2]
    average = np.average(third_column_02)
    ratio = round(average)
    positive_value = abs(ratio)
    g_value_02 = ((9.80665 * ratio) + third_column_02)
    radius_interp = np.average(1/(2 * g_value_02 * 1e-5))
    entropy_values = calculate_entropy(g_value_02)
    pure_entropy = calc_pure_entropy(g_value_02)
    df_02['Entropy'] = entropy_values
    df_02['GGgB'] = pure_entropy
    output_folder_02 = filedialog.askdirectory()
    if not output_folder_02:
         break
    output_filename_02 = 'Entropy_data.csv'
    output_file_path_02 = os.path.join(output_folder_02, output_filename_02)
    print("\nFile 'entropy_data.csv' created and saved in the specified folder.\n")
    df_02.to_csv(output_file_path_02, index=False)
    new_df_02 = pd.read_csv(output_file_path_02)
    x_2 = new_df_02.iloc[:, 0]
    y_2 = new_df_02.iloc[:, 1]
    z_2 = new_df_02.iloc[:, 3]
    interpolation_radius_02 = 4 * radius_interp
    xi_2, yi_2 = np.meshgrid(np.arange(x_2.min(), x_2.max(), interpolation_radius_02),
                        np.arange(y_2.min(), y_2.max(), interpolation_radius_02))
    zi_2 = spi.griddata((x_2, y_2), z_2, (xi_2, yi_2), method='cubic')
    plt.figure(figsize=(16, 12))
    c_2 = plt.pcolormesh(xi_2, yi_2, zi_2, cmap='rainbow')
    plt.colorbar(c_2, label='Log(S) (Planck Area)', orientation='vertical')
    plt.xlabel('X - Easting')
    plt.ylabel('Y - Northing')
    plt.title('Hawking Entropy Map')
    figure_filename_02 = 'Entropy_map.png'
    figure_file_path_02 = os.path.join(output_folder_02, figure_filename_02)
    plt.savefig(figure_file_path_02, dpi=300, bbox_inches='tight')
    print("\nFile 'Entropy_map.png' created and saved in the specified folder.\n")
    plt.show()
    x_3 = new_df_02.iloc[:, 0]
    y_3 = new_df_02.iloc[:, 1]
    z_3 = new_df_02.iloc[:, 4]
    xi_3, yi_3 = np.meshgrid(np.arange(x_3.min(), x_3.max(), interpolation_radius_02),
                        np.arange(y_3.min(), y_3.max(), interpolation_radius_02))
    zi_3 = spi.griddata((x_3, y_3), z_3, (xi_3, yi_3), method='cubic')
    plt.figure(figsize=(16, 12))
    c_3 = plt.pcolormesh(xi_3, yi_3, zi_3, cmap='viridis')
    plt.colorbar(c_3, label='Giga-Googolbyte (GGgB)', orientation='vertical')
    plt.xlabel('X - Easting')
    plt.ylabel('Y - Northing')
    plt.title('Googolbyte Distribution Map')
    figure_filename_03 = 'Googolbyte_map.png'
    figure_file_path_03 = os.path.join(output_folder_02, figure_filename_03)
    plt.savefig(figure_file_path_03, dpi=300, bbox_inches='tight')
    print("\nFile 'Googolbyte_map.png' created and saved in the specified folder\n")
    plt.show()
    print('The average Schwarzschild radius is:',radius_interp, 'meters\n')
    sentence = str(input("Exit the program (y/n)? "))
    if sentence == 'y':
	    break