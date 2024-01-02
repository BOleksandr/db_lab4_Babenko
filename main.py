import psycopg2

username = 'Babenko'
password = 'postgres'
database = 'db_lab3'
host = 'localhost'
port = '5432'

query_1 = '''
select trim(model) as model, round(avg(grade), 0) as grade_avg from cellphone, rating
where cellphone.cellphone_id = rating.cellphone_id
group by cellphone.cellphone_id
order by model;
'''
query_2 = '''
select trim(brand) as brand, count(*) as number_phone from Cellphone
group by brand;
'''
query_3 = '''
select ram, round(avg(grade), 2) as grade_avg from rating natural join characteristic
group by ram
order by ram;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()
    print('1. Average rating of each phone by users\n')
    cur.execute(query_1)

    for row in cur:
        print(row)


    print('\n2. Number of phones of each brand\n')
    cur.execute(query_2)
    for row in cur:
        print(row)

    print('\n3. Average rating of phones with the same RAM\n')
    cur.execute(query_3)
    for row in cur:
        print(row)