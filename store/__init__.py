# Este archivo nos permite convertir la carpeta en un modulo
import pymysql

# This line is neccesary to avoid the error:
# mysqlclient 1.3.13 or newer is required; you have 0.9.3
pymysql.version_info = (1, 3, 13, "final", 0)

pymysql.install_as_MySQLdb()