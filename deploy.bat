cd backend
py -m venv venv
.\venv\Scripts\activate
py -m pip install -r requirements.txt
cd prj
py .\manage.py migrate