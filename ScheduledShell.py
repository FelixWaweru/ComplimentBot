# Python script used to run the ScheduledRun.sh bash script
import subprocess

print ("Started scheduled run bash script")
subprocess.call("ScheduledRun.sh, shell=True")
print ("Ended scheduled run bash script")