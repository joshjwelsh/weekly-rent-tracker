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
			
			value = value.replace('\x00','')
			print_all = lambda x: print(repr(value))
			print("Hello ", print_all(value))
			v = int(value)
			
			new_val = v + 1
			f.truncate(0)
			f.write(str(new_val))
			value = new_val 



	strVal = str(value)
	zipCodeFilename = f"zip_set_{strVal}.txt"
	recordFilename = f"records_{strVal}.txt"
	fullPathJsonFilename = str(subPath) + str(jsonFilename)
	l_filenames = [fullPathJsonFilename, zipCodeFilename, recordFilename]
	print(l_filenames)
	data_formater.entry_point(l_filenames)
	print('Files ran')
	zm = zipcode_mapper.Mappr()
	zm.entry_point(fullPathJsonFilename)
	print('Run execute')

except Exception as e: 
	print("ERROR: something went wrong in main\n")
	print(e)