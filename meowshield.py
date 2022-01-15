# Loads env file
# Don't use .env on Replit
import os
secrets = { }
if ("REPL_SLUG" in os.environ and "REPLIT_DB_URL" in os.environ and "REPL_ID" in os.environ and "REPL_IMAGE" in os.environ and "REPL_LANGUAGE" in os.environ and "REPL_OWNER" in os.environ and "REPL_PUBKEYS" in os.environ and "REPL_SLUG" in os.environ) or os.environ.get("force-os-env") is "yes":
  print("Using os.environ for env.")
  secrets = os.environ
else:
  print("Using .env file for env.")
  from dotenv import dotenv_values
  try:
    secrets = dotenv_values(".env")
  except:
    print("Loading .env file failed, using os.environ")
    secrets = os.environ
if not ( "SCRATCH_USERNAME" in secrets and "SCRATCH_PASSWORD" in secrets ):
  raise Exception("Username not found.")
# Import dependency
from scratchclient import ScratchSession
from datetime import datetime
from time import sleep

# Main code
print("Meowshield 0.1.1 ALPHA")

print("logging in")
session = ScratchSession(secrets['SCRATCH_USERNAME'], secrets['SCRATCH_PASSWORD'])
print("connecting to cloud")
cloud1 = session.create_cloud_connection(612229554)
cloud1s = "28" # this is what to set cloud1 to - the "s" means "set"
print("connected")
def targetv():
  while True:
    # thanks to @kccuber-scratch on github (@kccuber on scratch.mit.edu) for the idea of this "ov" system (my variable names are bad too)
    # ov = online variable (probably, i forgot)
    try:
      ov = str(cloud1.get_cloud_variable("ONLINE"))
    except:
      ov = cloud1s
    if not ov == cloud1s:
      print(datetime.now().strftime("%H:%M:%S") + f": INFO: Setting ONLINE to {cloud1s} for 612229554 - if griffpatch is online, shut down the script; automatic detection of this is one of our goals.")
      cloud1.set_cloud_variable("ONLINE", cloud1s)
    sleep(0.05)
targetv()
