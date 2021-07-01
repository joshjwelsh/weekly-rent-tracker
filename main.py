import datetime
import os
import data_formater
import zipcode_mapper


SUPPORT_FOLDER = 'temp/'

time_now  = datetime.datetime.now().strftime('%m-%d-%Y') 
jsonFilename = f"House-{time_now}.json"
subPath = "getRent/getRent/spiders/"

value = 0
try: 
	
	if not os.path.isdir(SUPPORT_FOLDER):
		os.mkdir(SUPPORT_FOLDER)
		with open('temp/count.txt', 'w') as f:
			f.write('1')
	else:
		with open('temp/count.txt', 'r+') as f:

			value = f.read()
			print('Value = ', value)
			v = int(value)
			new_val = v + 1
			f.truncate()
			f.write(str(new_val))



	strVal = str(value)
	zipCodeFilename = f"zip_set_{strVal}.txt"
	recordFilename = f"records_{strVal}.txt"
	fullPathJsonFilename = str(subPath) + str(jsonFilename)
	l_filenames = [fullPathJsonFilename, zipCodeFilename, recordFilename]
	print(l_filenames)
	data_formater.entry_point(l_filenames)
	print('Files ran')
	exec(open('zipcode_mapper.py').read())
	print('Run execute')

except Exception as e: 
	print("ERROR: something went wrong in main\n")
	print(e)