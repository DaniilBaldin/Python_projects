import sqlite3


class NewDatabase:
    def __init__(self, database):
        self.database = database

    def __enter__(self):
        self.connection = sqlite3.connect(self.database)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            error_name = str(exc_val)
            print(error_name)
            self.connection.rollback()
        else:
            self.connection.commit()
            self.connection.close()
        return True


with NewDatabase('database_new.db') as c:
    cursor = c.cursor()

    cursor.execute('''
        PRAGMA foreign_keys=ON;
    ''')

    cursor.execute('''
        CREATE table if not exists positions(
        id integer primary key autoincrement,
        prof_name);
    ''')

    cursor.execute('''
        INSERT into positions (prof_name) values
        ('CEO'),
        ('HR'),
        ('chief accountant'),
        ('manager'),
        ('programmer'),
        ('accountant'),
        ('clerk');
    ''')

    cursor.execute('''
        CREATE table if not exists genders(
        id integer primary key autoincrement,
        gen_name);
    ''')

    cursor.execute('''
        INSERT into genders (gen_name) values
        ('male'),
        ('female'),
        ('else');
        ''')

    cursor.execute('''
        CREATE table people(
        id int primary key not null,
        first_name text not null,
        last_name text not null,
        gender text,
        salary int,
        position text,
        email text,
        age int not null,
        foreign key(gender) references genders(id) on delete cascade on update cascade,
        foreign key(position) references positions(id) on delete set null on update cascade);
    ''')

    cursor.execute("""
        INSERT into people values
        (1, 'Steven', 'King', 1, abs(random()%10000 + 5000), 1, 'sking@gmail.com', abs(random()%10)+50),
        (2, 'Neena', 'Kochhar', 2, abs(random()%10000 + 4000), 2, 'ncochhar@gmail.com', abs(random()%10)+40),
        (3, 'Lex', 'Haan', 1, abs(random()%10000 + 4000), 3, 'lhaan@gmail.com', 
        abs(random()%10)+40), 
        (4, 'Alexander', 'Hunold', 1, abs(random()%10000 + 4000), 3, 
        'ahunold@gmail.com', abs(random()%10)+30),
        (5, 'Bruce', 'Ernst', 1, abs(random()%10000 + 4000), 5, 
        'bernst@gmail.com', abs(random()%10)+30);
    """)

    cursor.execute("""
        INSERT into people (id, first_name, last_name, gender, salary, position, age) values
        (6, 'David', 'Austin', 1, abs(random()%100), 5, abs(random()%20+10)),
        (7, 'Valli', 'Pataballa', 2, abs(random()%100), 6, abs(random()%20+10)),
        (8, 'Diana', 'Lorentz', 2, abs(random()%100), 4, abs(random()%20+10)),
        (9, 'Nancy', 'Greenberg', 3, abs(random()%100), 4, abs(random()%20+10)),
        (10, 'Daniel', 'Faviet', 1, abs(random()%100), 4, abs(random()%20+10))
    """)

    cursor.execute("""
        INSERT into people (id, first_name, last_name, position, age) values
        (11, 'John', 'Chen', 6, abs(random()%30)),
        (12, 'Sigal', 'Tobias', 6, abs(random()%30)),
        (13, 'Ismael', 'Sciarra', 6, abs(random()%30)),
        (14, 'Guy', 'Himuro', 6, abs(random()%30)),
        (15, 'Karen', 'Colmenares', 7, abs(random()%30)),
        (16, 'Valli', 'Sciarra', 6, abs(random()%30)),
        (17, 'Luis', 'Popp', 7, abs(random()%30)),
        (18, 'Den', 'Raphaely', 6, abs(random()%30)),
        (19, 'Alexander', 'Khoo', 7, abs(random()%30)),
        (20, 'Shelli', 'Baida', 6, abs(random()%30));
    """)

    cursor.execute('''INSERT into genders (gen_name) values ('transsexual');''')
    new_gender_id = cursor.lastrowid

    try:
        v = "(21, 'Hazel', 'Philtanker', 4, 6, 35)"
        cursor.execute(f'''INSERT into people (id, first_name, last_name, gender, position, age) 
        values {v};''')
    except sqlite3.IntegrityError as e:
        print(f'There is no position for {v}: {e}')

    cursor.execute(f'''UPDATE people SET gender = {new_gender_id} where id = abs(random()%20+1);''')

    print(f'---Persons with new gender = {new_gender_id}---')
    data = cursor.execute(f'SELECT * from people where gender = {new_gender_id};')
    for d in data:
        print(d)
    print('------')

    gender_new = "transsexual"
    cursor.execute(f'DELETE from genders where gen_name = "{gender_new}";')

    data = list(cursor.execute(f'SELECT * from people where gender = {new_gender_id};'))
    for d in data:
        print(d)
    if len(data) == 0:
        print(f'There is no {gender_new} persons in the table.')

    print('---JOIN---')
    data = cursor.execute('''
        SELECT
            people.id,
            people.first_name,
            people.last_name,
            genders.gen_name,
            positions.prof_name
        FROM people 
        JOIN genders on genders.id = people.gender
        JOIN positions on positions.id = people.position
        WHERE people.salary > 10000;
    ''')
    for d in data:
        print(d)

    print('---LEFT JOIN---')
    data = cursor.execute('''
        SELECT
            people.id,
            people.first_name,
            people.last_name,
            genders.gen_name,
            positions.prof_name
        FROM people
        JOIN genders on genders.id = people.gender 
        LEFT JOIN positions on positions.id = people.position
        WHERE people.salary > 10000;
    ''')
    for d in data:
        print(d)

    cursor.execute('''DELETE from positions where id = 7;''')

    data = cursor.execute('''
        SELECT
            people.id,
            people.first_name,
            people.last_name,
            genders.gen_name,
            positions.prof_name
        FROM people
        JOIN genders on genders.id = people.gender 
        LEFT JOIN positions on positions.id = people.position
        WHERE people.salary > 10000;
    ''')
    for d in data:
        print(d)
