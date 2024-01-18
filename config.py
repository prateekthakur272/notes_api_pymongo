from dotenv import dotenv_values

env_values = dotenv_values('.env')
mongo_password = env_values['MONGO_PASSWORD']
