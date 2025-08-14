from datetime import datetime
#*************************************************************************************************************#
#***********Enter the variables for the Job Requirement  ****************************************************#
#*************************************************************************************************************#
n = int(input("Enter the number of object_list you have: "))
object_list = []
for i in range(n):
    object = input(f"Enter the name of object_{i+1} text file where list of objects are saved: ")
    object_list.append(object)
    i += 1
schemas = object_list
statement = input ("enter the name test file where repeatable statement is written: ")
subsystem=input("Enter the name of target subsystem: ")
LOCATION=input("Enter the name of target location: ")
REMOTE=input("Enter the name of source location: ")
print("#####################################################################")
print("             ###########################################             ")
print("#####################################################################")
print("The input file with list of object is: ", object_list)
print("The repetable script is: ", statement)
print(f"subsystem= {subsystem}, LOCATION={LOCATION}, REMOTE={REMOTE}" )
#*************************************************************************************************************#
#*************************************************************************************************************#
#*************************************************************************************************************#
start = datetime.now()
for schema in schemas:
    c = '1'
    with open(schema) as name:
        names = name.readlines()
    with open(statement) as letters:    #----- update the sample script
        letter = letters.read()
    for table in names:
        next_table= table.strip()
        mail1 = letter.replace("NAME" , next_table)
        # mail1 = letter.replace("DATASET", next_table)
        mail2 = mail1.replace("i", c)
        mail3 = mail2.replace("LOCATION", LOCATION)
        mail4 = mail3.replace("REMOTE", REMOTE)
        final_mail = mail4.replace("SSN", subsystem)
        with open(f"job_{schema}", mode="a") as final_job:  #----output job
            final_job.write(final_mail)
        w = int(c) + 1
        c = str(w)
    print("#####################################################################")
    print(f"The output job is saved in file: job_{schema}")

end =  datetime.now()
print(f"Execution Time is: {(end - start).total_seconds()} Seconds")

