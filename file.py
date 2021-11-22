#Script to handle logfiles on server. Script is scheduled to run on a regular bases e.g. each month or so
import os, datetime, shutil
import logging

logging.basicConfig(filename='logging.log', filemode = 'a', level=logging.DEBUG, style="{" ,format = "{asctime} [{levelname:8}] {message}", datefmt="%d.%m.%Y, %H:%M:%S")

logging.info('Script executed!')
source_path = '/home/jarvis/Scripts/data/'
destination = '/home/jarvis/Scripts/archive/'

selector = datetime.datetime.now()
selector_final = (str(selector.month) + '-' + str(selector.year-2000) + '-log.txt')

if selector.day <10:
        day_value = '0'+str(selector.day)
else:
        day_value = str(selector.day)

logfile_2day = day_value + '-' + str(selector.month) + '-' + str(selector.year -2000) + '-log.txt'

# Container is the list of the different Month-Values that appear among the list of logfiles
container = []
# File_list is the list of log-files with .txt ending in the directory
file_list = []

list = os.listdir(source_path)

for files in list:
        if files.endswith('-log.txt'):
                file_list.append(files)
                value = (files[3:5])
                if value in container:
                        continue
                else:
                        container.append(value)
# loop to check if target directories for each month do exist or not!
for i in range(len(container)):
        folder_name = (container[i]+'_21')
        if os.path.exists(destination+folder_name) == True:
                continue
        else:
#                print('Create folder {}...'.format(destination+folder_name))
                os.mkdir(destination + folder_name)
                logging.info('Directory {} created'.format(folder_name))

# loop to copy files into correct folder
for element in container:
        for i in file_list:
                if i[3:5] == element:
                        if i == logfile_2day:
#                                print("File {} won't be copied!".format(i))
                        else:
                                place = destination + element + '_21'
                                try:
                                        shutil.move(os.path.join(source_path, i), os.path.join(place, i))
#                                        print('Move {} --> {}'.format(i, place))
                                        logging.info('Move {} --> {}'.format(i,place))
                                except:
#                                        print('Error happended!')
                                        logging.error('File could not be moved!')
                                        continue

logging.shutdown
