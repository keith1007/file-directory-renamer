import os, time, sys
from datetime import datetime

main_folder = str(sys.argv[1])
new_folder = str(sys.argv[2])

for sub_folder in os.listdir(main_folder):
    if os.path.isdir(os.path.join(main_folder, sub_folder)):
        name_incrementor = 1
        old_name_list = []
        dates_mod_list = []

        for file in os.listdir(os.path.join(main_folder, sub_folder)):
            old_name = os.path.join(main_folder, sub_folder, file)

            time_mod_float = os.path.getmtime(old_name)

            old_name_list.append(old_name)
            dates_mod_list.append(time_mod_float)

        names_dates_dict = dict(zip(old_name_list, dates_mod_list))
        sorted_names_dates_dict = {k: v for k, v in sorted(names_dates_dict.items(), key=lambda item: item[1])}

        # [print(time.ctime(values)) for values in sorted_names_dates_dict.values()]

        for key in sorted_names_dates_dict:
            subfolder_todate = (datetime.strptime(sub_folder, '%B %d, %Y')).strftime("%m-%d-%Y")
            #new_name = os.path.join(main_folder, sub_folder, sub_folder + " - " + str(name_incrementor) + "." + key.split(".")[-1])
            new_name = os.path.join(new_folder, subfolder_todate + " - " + str(name_incrementor) + "." + key.split(".")[-1])
            os.rename(key, new_name)
            name_incrementor += 1

print("Renamed everything successfully!")