#WELCOME TO HAWKING ENTROPY CALCULATOR, Copyright(c) Gazillo Neto, R. (2024)
import os
import pandas as pd
import numpy as np
import scipy.interpolate as spi
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
while True:
    print("WELCOME TO HAWKING ENTROPY!\nCopyright(c) Gazillo Neto, R. (2024)\n\n")
    print("#     #  # # # #  #     #  #     #   # # # #   #     #  # # # #\n#     #  #     #  #     #  #   #        #      # #   #  #\n# # # #  # # # #  #  #  #  # #          #      #  #  #  #   # #\n#     #  #     #  # # # #  #   #        #      #   # #  #     #\n#     #  #     #  #     #  #     #   # # # #   #     #  # # # #\n\n")
    print("# # # #  #     #  # # # #  # # # #   # # # #  # # # #  #     #\n#        # #   #     #     #     #   #     #  #     #   #   #\n# # #    #  #  #     #     # # #     #     #  # # # #    # #\n#        #   # #     #     #    #    #     #  #           # \n# # # #  #     #     #     #      #  # # # #  #           #\n\n")
    print("\nHawking entropy is a software that contains a mathematical algorithm to process gravimetric data in a novel way. This is an experiment that manipulates data from gravimetric real surveys and uses Bekenstein-Hawking Entropy formula to calculate gravitational entropies considering that each gravimetric measurement corresponds to a hypothetical value of surface gravity of an individual Schwarzschild black hole in Planck units. The algorithm reads the original dataframe from gravimetric surveys in 'csv' format and then perform the 'filtering' calculations using gravitational entropy formulas generating as output a 2D map plot of interpolated values of Log(Entropy) in Planck units versus specified X and Y space coordinates. Also, the program calculates the entropy in Planck units corresponding to bits of gravitational holographic information which is in the orders of 'Googolbytes' of space-time storage capacity! A corresponding file containing the generated dataframe for entropy values is created as output so the user can import it to other data visualization softwares for customization. This approach transforms Bouguer anomaly maps into Hawking Entropy maps. This gives a new unusual visualization of gravimetric data in a tentative approach to apply theoretical physics in a highly complex scenario such as quantum gravity to real-world applications in a novel way.\nGOOD MATHEMATICAL ENDEAVOURS!!\n")
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
        googolbyte = entropy/1.6e+100
        return googolbyte
    df_02 = pd.read_csv(input_file_path)
    third_column_02 = df_02.iloc[:, 2]
    g_value_02 = (third_column_02)
    radius_interp = np.average(1/(2 * g_value_02 * 1e-5))
    entropy_values = calculate_entropy(g_value_02)
    pure_entropy = calc_pure_entropy(g_value_02)
    df_02['Entropy'] = entropy_values
    df_02['GgB'] = pure_entropy
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
    print('The average Schwarzschild radius is:',radius_interp, 'meters\n')
    interpolation_radius_02 = float(input("Enter the interpolation radius: "))
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
    z_3 = new_df_02.iloc[:, 4]
    total_sum = np.sum(z_3)
    text_googol = 'Bit_number.txt'
    file_text = os.path.join(output_folder_02, text_googol)
    with open(file_text, 'w') as filetxt:
         filetxt.write(f"The total bits of gravitational entropy are: {total_sum} Googolbytes!\n")
         filetxt.write(f"The average Schwarzschild radius is: {radius_interp} meters")
    sentence = str(input("Exit the program (y/n)? "))
    if sentence == 'y':
	    break