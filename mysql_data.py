import datetime


import yaml
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


yaml_file_path = "config/basic.yml"
my_config = None
with open(yaml_file_path, encoding='utf-8') as f:  # demo.yaml内容同上例yaml字符串
    my_config = yaml.safe_load(f)

t_start = datetime.datetime.now()

engine = create_engine(
    "mysql+pymysql://" + my_config["mysql"]['username'] + ":" + my_config['mysql']['password']
    + "@" + my_config['mysql']['hostname'] + ":3306/tt",
    echo=True
)

session = sessionmaker(bind=engine)()

def createAll(objs):
    session.bulk_save_objects(objs)
    session.commit()