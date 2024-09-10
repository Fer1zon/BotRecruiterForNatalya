import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ['TOKEN']
TEST_TOKEN = os.environ.get('TEST_TOKEN')

RECIPIENT_APPLICATIONS = os.environ["RECIPIENT_APPLICATIONS"]

adminId = [5530562487, 6836588559]


dataBasePath = os.path.dirname(__file__) + '/dataBase/data_base.db'