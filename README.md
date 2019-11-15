Test Case: Simple Web-site.

Steps before deploy:
1. Clone git repository
2. cd test_case && pip install -r requirements.txt
3. flask db init && flask db migrate -m "users table" && flask db upgrade
4. flask run
