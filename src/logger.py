import logging 
import os 
from datetime import datetime
LOGS=f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOGS)
os.makedirs(logs_path,exist_ok=True)
LOGS_PATH=os.path.join(logs_path,LOGS)
logging.basicConfig(
    filename=LOGS_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO

)

