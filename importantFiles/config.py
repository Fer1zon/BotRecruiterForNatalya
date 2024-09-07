import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ['TOKEN']
TEST_TOKEN = os.environ.get('TEST_TOKEN')

RECIPIENT_APPLICATIONS = os.environ["RECIPIENT_APPLICATIONS"]

adminId = []


dataBasePath = os.path.dirname(__file__) + '/dataBase/data_base.db'