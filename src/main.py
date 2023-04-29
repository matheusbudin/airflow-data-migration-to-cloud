import os
import psycopg2

conn = psycopg2.connect(
    database=os.environ.get('DB_NAME'),
    host=os.environ.get('DB_HOST'), #IP da maquina, nome do servico no compose
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD'),
    port=os.environ.get('DB_PORT') #PORTA DO CONTAINER
  )

cursor = conn.cursor()

# cursor.execute("""

#   CREATE TABLE users(
#   id serial PRIMARY KEY,
#   username VARCHAR(50) NOT NULL
#   );

# """)


# cursor.execute("""

#   INSERT INTO users(
  
#   username
#   )VALUES('Rafael'), ('Matheus');
  

# """)

cursor.execute("""

 SELECT *
 FROM users
  

""")

result = cursor.fetchall();

for data in result:
    print(data)


cursor.close()
conn.commit()
print('deu certo!')