from datetime import datetime
schemas = ["utslist.txt"]      #--- change this file with list of object
# job=["job.txt"]
# schemas = ["cadsname.txt"]
Subsystem='DB2A'
LOCATION='UKLGDB2A'
REMOTE='UKLGDBFN'
start = datetime.now()
for schema in schemas:
    c = '1'
    with open(schema) as name:
        names = name.readlines()
    with open("unload.txt") as letters:   #----------change the job file here with the sample job
    # with open("rename.txt") as letters:
        letter = letters.read()
    for table in names:
        next_table= table.strip()
        mail1 = letter.replace("NAME" , next_table)
        # mail1 = letter.replace("DATASET", next_table)
        mail2 = mail1.replace("i", c)
        mail3 = mail2.replace("LOCATION", LOCATION)
        mail4 = mail3.replace("REMOTE", REMOTE)
        final_mail = mail4.replace("SSN", Subsystem)
        with open(f"job_{schema}", mode="a") as final_job:
            final_job.write(final_mail)
        w = int(c) + 1
        c = str(w)
# with open(f"job_{schema}") as cmd:
#     cmd1 = cmd.readlines()
#     for row in cmd1:
#         with open(f"job.txt", mode='a') as ready_job:    #--output will be in job.txt
#             ready_job.write(row)

end =  datetime.now()
print(f"Execution Time is: {(end - start).total_seconds()} Seconds")

