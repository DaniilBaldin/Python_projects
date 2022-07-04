import sqlite3

# создать базу данных (произвольное имя)
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Создать таблицу people с атрибутами id (обязательно),
# имя (обязательно), фамилия (обязательно), пол (обязательно),
# зарплата, должность, email, возраст (обязательно)
data = cursor.execute("""
create table IF NOT EXISTS people(
    id int primary key not null,
    first_name text not null,
    last_name text not null,
    sex text not null,
    salary int,
    position text,
    email text,
    age int not null);
""")

# Сгенерировать 20 записей
cursor = connection.cursor()
cursor.execute("""
    INSERT INTO people VALUES
    (1, 'Steven', 'King', 'male', abs(random()%10000 + 5000), 'CEO', 'sking@gmail.com', abs(random()%10)+50),
    (2, 'Neena', 'Kochhar', 'female', abs(random()%10000 + 4000), 'HR', 'ncochhar@gmail.com', abs(random()%10)+40),
    (3, 'Lex', 'Haan', 'male', abs(random()%10000 + 4000), 'chief accountant', 'lhaan@gmail.com', abs(random()%10)+40),
    (4, 'Alexander', 'Hunold', 'male', abs(random()%10000 + 4000), 'chief accountant', 
    'ahunold@gmail.com', abs(random()%10)+30),
    (5, 'Bruce', 'Ernst', 'male', abs(random()%10000 + 4000), 'programmer', 'bernst@gmail.com', abs(random()%10)+30);
""")

cursor.execute("""
    INSERT INTO people (id, first_name, last_name, sex, salary, position, age) VALUES
    (6, 'David', 'Austin', 'male', abs(random()%100), 'programmer', abs(random()%10));
""")

cursor.execute("""
    INSERT INTO people (id, first_name, last_name, sex, salary, position, age) VALUES
    (7, 'Valli', 'Pataballa', 'female', abs(random()%100), 'accountant', abs(random()%10));    
""")

cursor.execute("""
    INSERT INTO people (id, first_name, last_name, sex, salary, position, age) VALUES
    (8, 'Diana', 'Lorentz', 'female', abs(random()%100), 'manager', abs(random()%10));    
""")

cursor.execute("""
    INSERT INTO people (id, first_name, last_name, sex, salary, position, age) VALUES
    (9, 'Nancy', 'Greenberg', 'female', abs(random()%100), 'manager', abs(random()%10));    
""")

cursor.execute("""
    INSERT INTO people (id, first_name, last_name, sex, salary, position, age) VALUES
    (10, 'Daniel', 'Faviet', 'male', abs(random()%100), 'manager', abs(random()%10));    
""")

cursor.execute("""
    INSERT INTO people (id, first_name, last_name, sex, salary, position, age) VALUES
    (11, 'John', 'Chen', 'male', abs(random()%100), 'accountant', abs(random()%10));    
""")

cursor.execute("""
    INSERT INTO people (id, first_name, last_name, sex, salary, position, age) VALUES
    (12, 'Sigal', 'Tobias', 'male', abs(random()%100), 'accountant', abs(random()%10));    
""")

cursor.execute("""
    INSERT INTO people (id, first_name, last_name, sex, position, age) VALUES
    (13, 'Ismael', 'Sciarra', 'male', 'accountant', abs(random()%10));    
""")

cursor.execute("""
    INSERT INTO people (id, first_name, last_name, sex, position, age) VALUES
    (14, 'Guy', 'Himuro', 'male', 'accountant', abs(random()%10));    
""")

cursor.execute("""
    INSERT INTO people (id, first_name, last_name, sex, position, age) VALUES
    (15, 'Karen', 'Colmenares', 'female', 'clerk', abs(random()%10));    
""")

cursor.execute("""
    INSERT INTO people (id, first_name, last_name, sex, position, age) VALUES
    (16, 'Valli', 'Sciarra', 'male', 'accountant', abs(random()%10));    
""")

cursor.execute("""
    INSERT INTO people (id, first_name, last_name, sex, position, age) VALUES
    (17, 'Luis', 'Popp', 'male', 'clerk', abs(random()%10));    
""")

cursor.execute("""
    INSERT INTO people (id, first_name, last_name, sex, position, age) VALUES
    (18, 'Den', 'Raphaely', 'male', 'accountant', abs(random()%10));    
""")

cursor.execute("""
    INSERT INTO people (id, first_name, last_name, sex, position, age) VALUES
    (19, 'Alexander', 'Khoo', 'male', 'clerk', abs(random()%10));    
""")

cursor.execute("""
    INSERT INTO people (id, first_name, last_name, sex, position, age) VALUES
    (20, 'Shelli', 'Baida', 'female', 'accountant', abs(random()%10));    
""")


# Додати два записи для Laurence Wachowski та Andrew Wachowski стать чоловік інші дані довільні
cursor.execute("""
    INSERT INTO people (id, first_name, last_name, sex, age) VALUES
    (21, 'Laurence', 'Wachowski', 'male', 35);    
""")

cursor.execute("""
    INSERT INTO people (id, first_name, last_name, sex, age) VALUES
    (22, 'Andrew', 'Wachowski', 'male', 35);    
""")

# Змінити стать для Laurence Wachowski та Andrew Wachowski на жінка
cursor.execute('UPDATE people SET sex = "female" where last_name = "Wachowski";')

# Змінити ім'я для Laurence Wachowski на Lana
cursor.execute('UPDATE people SET first_name = "Lana" where first_name = "Laurence" and last_name = "Wachowski";')

# Змінити ім'я для Andrew Wachowski на Lilly
cursor.execute('UPDATE people SET first_name = "Lilly" where first_name = "Andrew" and last_name = "Wachowski";')

# додати для всіх записів в яких немає email
cursor.execute('UPDATE people SET email = first_name || "." || last_name || "@gmail.com" where email is null;')

# Вивести всіх людей з зарплатою більще 10000
data_salary = connection.execute("""
    SELECT * from people where salary > 10000;
""")
for d in data_salary:
    print(d)
print('-------------')

# Вивести всіх людей з зарплатою 10000 віком старше 25
data_salary_age = connection.execute("""
    SELECT * from people where salary > 10000 and age > 25;
""")
for d in data_salary_age:
    print(d)
print('-------------')

# видалити всіх людей без посади
connection.execute('DELETE from people where position is null')

connection.commit()
connection.close()
