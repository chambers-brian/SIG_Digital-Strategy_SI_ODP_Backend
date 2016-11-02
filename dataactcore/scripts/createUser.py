from dataactcore.interfaces.function_bag import createUserWithPassword
from flask_bcrypt import Bcrypt
from dataactbroker.app import createApp

with createApp().app_context():
    createUserWithPassword("email","defaultPass",Bcrypt(),7,"999")