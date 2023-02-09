import psycopg2


conn = psycopg2.connect(
    host = 'localhost',
    user = 'postgres', 
    database = 'postgres',
    password = 'timezone',
    client_encoding="UTF8"
)


cursor = conn.cursor()


with open("C:\\THINGS\\githup project\\finalQ.txt", 'r', encoding='utf-8') as qus:
 
    quest = qus.readlines()
    # Remove the newline character from each name
    quest = [name.strip() for name in quest]
    

with open("C:\\THINGS\\githup project\\finalA.txt", 'r', encoding='utf-8') as ans:

    answer = ans.readlines()
    # Remove the newline character from each gender
    answer = [gender.strip() for gender in answer]
    
    # Zip the names and genders together to create pairs
    data = zip(quest, answer)
    

    for quest, answer in data:

        cursor.execute("INSERT INTO bots (qus, ans) VALUES (%s, %s)", (answer, quest))


conn.commit()


cursor.close()
conn.close()