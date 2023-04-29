import psycopg2

conn = psycopg2.connect(
    database="banco_teste_python",
    host="db", #IP da maquina, nome do servico no compose
    user="budin",
    password="root",
    port=5432 #PORTA DO CONTAINER
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