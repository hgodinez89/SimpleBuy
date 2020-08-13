import pymysql

# This line is neccesary to avoid the error:
# mysqlclient 1.4.0 or newer is required; you have 0.9.3
pymysql.version_info = (1, 4, 0, "final", 0)

pymysql.install_as_MySQLdb()