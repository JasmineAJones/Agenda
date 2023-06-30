import sqlite3
from datetime import datetime

con = sqlite3.connect('DailyTasks.db')
cur = con.cursor()

res = cur.execute("SELECT * FROM Tasks")
row = res.fetchall()
print(row)


res = cur.execute("INSERT INTO 'main'.'Tasks' ('TopicID', 'Task', 'Date') VALUES (1, 'Wait for response', '2023-06-29 00:00:00');")
con.commit()
id = cur.lastrowid
print(id)

#date = datetime.now()
#res = cur.execute("SELECT Date FROM Topic")
#row = res.fetchone()
#taskdate = row[0]
#taskdate = taskdate[:10]
#date = str(date)[:10]
#taskdate = datetime.strptime(taskdate,"%Y-%m-%d")
#date = datetime.strptime(date,"%Y-%m-%d")

#print(taskdate == date)



con.close()
#INSERT INTO "main"."Tasks"
#("TopicID", "Task", "Details")
#VALUES (1, 'Bug Fixes', 'Need to do extensive tests to find any bugs');