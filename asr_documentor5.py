from vosk import Model, KaldiRecognizer
from datetime import datetime
import pyaudio
import re
import os
import csv
import pandas as pd
import numpy as np








####TRIGGERS\/\/\/\/\/\/
DocumentTrigger= "document"
Create_new_document = "create new document"
Edit_document = "edit"


ListTrigger = "list"
ExitModeTrigger = (str("exit mode"))
trigger_phrase = (str())

####TRIGGERs/\/\/\/\//\/\

##############################################################



##############################################################
####Main Vars\/\/\/\/
triggerword = (str("israel"))
Current_Path = os.getcwd()
commands_file_location = Current_Path + "/command_list.csv"


#model_location = Current_Path + '/EN-Model/'
model = Model(r'/EN-Model/') ##########################################################Set location of EN-Model Folder!!!!!!!!!!!!!!!!!!!!!!!!
#model = Model(r model_location) #read model
recognizer = KaldiRecognizer(model, 16000)
cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

####Main Vars/\/\/\/\
##############################################################

####Document Vars\/\/\/\/
Document_body = (str(""))
Document_name = (str(""))

Document_test_location = open(Current_Path + "/List.txt", 'a+')

Document_default_location = (str(Current_Path + "/RecordedDocument/"))
Document_location = (str(""))
Document_mode = (str(""))
####Document vars/\/\/\/\#

##############################################################

##############################################################






############################################################################app_Launcher Var \/\/\/\/
csvReader = pd.read_csv(commands_file_location)
script = csvReader['script'].values
command = csvReader['command'].values
index = (str(np.where(command == 'test')))  
CMD_Trigger = (str("start"))
User_CMD = (str(""))
###########################################################################app_Launcher Var /\/\/\/\
#############################################################



now = datetime.now()
current_time_date = (str(now.strftime("%d/%m/%Y %H:%M:%S")))
clean_time_date = current_time_date.replace(":","_")
cleaner_time_date = clean_time_date.replace("/","_")
Document_location_name = (str(Current_Path + "/" + cleaner_time_date + "_"))
Document_file_location = ""	
Path_Set = False
print(Document_location_name)




###############################################################

while True:
	data = stream.read(8192)
	# ~ if len(data) == 0:
		# ~ break
		
#####################################Get date for file name		
	
#####################################Get date for file name			
	
	
	if recognizer.AcceptWaveform(data):
		# print(recognizer.Result())
		userData = (str(recognizer.Result()))
		userDataCleanse = userData.replace("text", '')
		userDataCleanse2 = userDataCleanse.replace('""', '')
		userDataCleanse3 = userDataCleanse2.replace ('"','')
		userDataCleanse4 = userDataCleanse3.replace ('"','')
		userDataCleanse5 = userDataCleanse4.replace ('{','')
		userDataCleanse6 = userDataCleanse5.replace ('}','').strip()
		
		userInput = userDataCleanse6.replace(':', '').strip()
		Document_mode = userInput.replace(triggerword, '').strip()
		print(userInput)
		print(Document_mode)
		
		if ExitModeTrigger in userInput :
			print("exiting " + Document_mode + " mode")
			Document_mode = (str(""))
			Path_Set = False
				 
		
			
		#Document_test_location.write(userInput)
		
################################################
##########List Actions\/\/\/\/\/\/\/\/
		if Document_mode == (str("List")):
			if Path_Set == False:
				Document_location_name = Document_location_name + Document_mode + ".txt"
				Path_Set = True
				Document_file_location = open (Document_location_name, "x")
				Document_file_location = open (Document_location_name, "a+")
			
			
	
			
			if (str("new entry")) in userInput:
				print("New Entry")
				now = datetime.now()
				current_time_date = (str(now.strftime("%d/%m/%Y %H:%M:%S")))
				NewEntry_userInput = userInput.replace('new entry','')
				Document_file_location.write(current_time_date + ":" + userInput)

##########List Action/\/\/\/\/\/\/\/\/
#################################################		
		 
################################################		
##########Documentation Actionn \/\/\/\/\/\/\/\/		
		if Document_mode == (str("Documentation")):
			if Path_Set == False:
				Document_location_name = Document_location_name + Document_mode + ".txt"
				Path_Set = True
				Document_file_location = open (Document_location_name, "x")
				Document_file_location = open (Document_location_name, "a+")
				 
			now = datetime.now()
			current_time_date = (str(now.strftime("%d/%m/%Y %H:%M:%S")))
			
			print(Document_file_location)
			Document_location = (str("Test.txt"))
			#Document_file_location = open (Document_location_name, "a+")
			Document_file_location.write(current_time_date + ":" + userInput)
			
			
##########Documentation Action /\/\/\/\/\/\/\/\/\			
#################################################
		
		else:
			
			
			
			######App Launcher\/\/\/\/################################################
			
			
			if CMD_Trigger in userInput:
				#print(userInput + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
				User_CMD = userInput.replace (CMD_Trigger, '')
				cleaned_user_cmd1 = User_CMD.replace (" ", '')
				cleaned_user_cmd2 = cleaned_user_cmd1.replace ("{", '')
				cleaned_user_cmd3 = cleaned_user_cmd2.replace ("}", '')
				
				
				Clean_User_CMD = (str(cleaned_user_cmd3.strip()))
				print(Clean_User_CMD+ "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
				print(Clean_User_CMD + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
				print(Clean_User_CMD + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

				if Clean_User_CMD in command:
					
									#   #
					#####################Clean up \/\/\/\/
					index2 = index.replace ('(','')
					index3 = index2.replace (')','')
					index4 = index3.replace ('array','')
					index5 = index4.replace ('[','')
					index6 = index5.replace (']','')
					index7 = index6.replace (',','')
					index8 = (int(index7)).strip()
					#####################Clean up /\/\/\/\
					results = script[index8]
			
					exec(open(results).read())
	
	
				else:
					print("not there")

  	
		#for row in csvReader:
        #print(row)
        
			else:
				print("CANT")       

			
			######App Launcher/\/\/\/\#################################################

		
			if triggerword in userInput:
				CompareTrigger = userInput.split()
##################This tells if you said the Document trigger\/\/\/\/\/\/
				#if DocumentTrigger in userInput:
				#if re.search(DocumentTrigger, userInput):
				
				for x in CompareTrigger:
					if x == DocumentTrigger:
						#print("Documention!!!!")
						Document_mode = (str("Documentation"))
						
						
						now = datetime.now()
						current_time_date = (str(now.strftime("%d/%m/%Y %H:%M:%S")))
						clean_time_date = current_time_date.replace
						
						
##################This tells if you said the Document trigger/\/\/\/\/\/\					
				
################This tells if you said the List trigger\/\/\/\/\/\/					
				#if ListTrigger in userInput:
				for x in CompareTrigger:
					if x == ListTrigger:
						print("Listing!!!!")
						Document_mode = (str("List"))
################This tells if you said the List trigger/\/\/\/\/\/\				

				
					if Create_new_document in userInput:
						print("create new document")
						if Edit_document in userInput: 
							print("attempting to make document" + userInput + "at location" + Document_default_location)
##################This tells if you said the List trigger/\/\/\/\/\/\	
						
					
					
