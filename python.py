import scratchattach as sa 
import os
from dotenv import load_dotenv

load_dotenv()

SESSION_ID = os.getenv("SESSION_ID")
PROJECT_ID = os.getenv("PROJECT_ID")

if SESSION_ID is None or PROJECT_ID is None:
    print("No session id/project id in .env")
    exit(1)

session = sa.login_by_id(SESSION_ID, username="superjolt")
cloud = session.connect_cloud(PROJECT_ID)
client = cloud.requests()

@client.request
def follow_me(username):
    print("Got follow request")
    try:
        user = session.connect_user(username)
        user.follow()
        return "done"
    except Exception as e:
        raise e

@client.event
def on_ready():
    print("Ready request handlers")

client.start(thread=True)
