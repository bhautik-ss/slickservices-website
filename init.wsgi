activate_this = '/home/slick/public_html/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
import sys
sys.path.insert(0,"/home/slick/")
from public_html import app as application
