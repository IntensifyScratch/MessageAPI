import os
import time
import scratchconnect
login = scratchconnect.ScratchConnect("-IntensifyServer-", "Intens1!")
print("Logged In!")
project = login.connect_project(project_id=599331245)
print("Connected Project!")
variables = project.connect_cloud_variables()
print("Connected Cloud Variables!")
while True:
  print("Checking...")
  try:
     request = variables.get_cloud_variable_value(variable_name='Request', limit=5)[0]
     if request != '0':
       user = str(variables.decode(request))
       try:
         count = variables.encode(str(login.connect_user(user.strip()).messages_count()))
       except:
         count = variables.encode('No User')
       #print(user)
       variables.set_cloud_variable(variable_name="Count", value=count)
       variables.set_cloud_variable(variable_name="Request", value=0)
  except BrokenPipeError:
       variables = project.connect_cloud_variables()
       print("Reconnecting...")
  except Exception as e:
       print(e)
  time.sleep(1)