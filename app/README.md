# Test site about kiwies

# Author: Juls

# Description:
I like kiwies and programming. And i have made site about them!
--
What i used:

Flask

SQLAlchemy

SQLite

openpyxl

and etc/

You could see all in requirements.txt

## How diploy:
1. Clone repository
2. Make and activate virtual environment
'''commandline
python -m venv venv
source venv/Scripts/activate'
'''
3. Download  requirements
'''commandline
pip install -r requirements.txt
'''
4. Make file .env and notice settings of link to DB and another settings
'''commandline
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=YOUR_SECRET_KEY
'''
5. Source flask application
'''commandline
flask run
'''





