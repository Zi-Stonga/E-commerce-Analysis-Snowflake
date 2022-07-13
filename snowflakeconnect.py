import snowflake.connector

cnn = snowflake.connector.connect(
    user = 'xxxxxxxx',
    password='xxxxxxxxxx',
    account='xxxxxxxxx'
    )
cs = cnn.cursor()
try:
    cs.execute('Select current_version()')
    row = cs.fetchone()
    print(row[0])
    print('creating warehouse..')
    sql = "CREATE WAREHOUSE IF NOT EXISTS store_warehouse"
    cs.execute(sql)
    print('creating database..')
    sql = "CREATE DATABASE IF NOT EXISTS store_database"
    cs.execute(sql)
    print('using database..')
    sql = "USE DATABASE store_database"
    cs.execute(sql)
    print('creating schema..')
    sql = "CREATE SCHEMA IF NOT EXISTS store_schema"
    cs.execute(sql)
finally:
    cs.close()
cnn.close()
    
    
