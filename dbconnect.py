import pymysql
def connection():
    conn = pymysql.connect(host="localhost",user = "root",passwd = "jigsaw123",db = "jigsaw")
    c = conn.cursor()
    return c, conn
		