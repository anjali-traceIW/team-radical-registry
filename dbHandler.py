from param import * 
import pysql

def select_many_query(query):
    try:
        connection = pymysql.connect(
            hostname,
            username,
            password,
            database_name,
            autocommit=True
        ) 
        with connection.cursor() as db:
        # Want another try?
            db.execute(query)
            results = db.fetchall()
    except Exception as e:
        print(e)
    finally:
        connection.close()
    return results