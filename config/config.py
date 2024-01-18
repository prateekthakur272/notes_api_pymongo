from dotenv import dotenv_values

env_values = dotenv_values('.env')
mongodb_password = env_values['MONGODB_PASSWORD']
