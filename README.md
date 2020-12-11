# spiri_command
＃run takeoff
step 1: put the test.py and spiri.py in same folder

step 2: change /otp/ros/.../mavros/launch px4_spiri.launch    gcs_url   = your IP port

step 3: change test.py  Drone(127.0.0.1:14550) to Drone(your IP port)

step 4: open a new terminal run    roslauch mavros px4_spiri.launch

step 5: connect your Qgroundcontrol.

step 6: open another terminal run   python test.py


#run point mission

step 1: put the mission.py mission_upload.py, mission.txt and spiri.py in same folder

step 2: change /otp/ros/.../mavros/launch px4_spiri.launch    gcs_url   = your IP port

step 3: change mission.py mission_upload.py Drone(127.0.0.1:14550) to Drone(your IP port)

step 4: open a new terminal run    roslauch mavros px4_spiri.launch

step 5: run python mission_upload.py.

step 5: connect your Qgroundcontrol.

step 6: open another terminal run   python mission.py
