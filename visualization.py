import psycopg2
import matplotlib.pyplot as plt

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

    cur.execute(query_1)
    model = []
    average_grade = []

    for row in cur:
        model.append(row[0])
        average_grade.append(row[1])

    x_range = range(len(model))

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    bar = bar_ax.bar(x_range, average_grade, label='Average grade')
    bar_ax.bar_label(bar, label_type='center') 
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(model, rotation = 20, ha = 'right')
    bar_ax.set_xlabel('Моделі телефонів')
    bar_ax.set_ylabel('Оцінка')
    bar_ax.set_title('Середня оцінка кожного телефону')

    cur.execute(query_2)
    brand = []
    count = []

    for row in cur:
        brand.append(row[0])
        count.append(row[1])

    pie_ax.pie(count, labels=brand, autopct='%1.1f%%')
    pie_ax.set_title('Частка телефонів кожного бренду')

    cur.execute(query_3)
    ram = []
    average_grade = []

    for row in cur:
        ram.append(row[0])
        average_grade.append(row[1])

    mark_color = 'blue'
    graph_ax.plot(ram, average_grade, color=mark_color, marker='o')

    for rm, avg_gr in zip(ram, average_grade):
        graph_ax.annotate(avg_gr, xy=(rm, avg_gr), color=mark_color,
                          xytext=(7, 2), textcoords='offset points')    

    graph_ax.set_xlabel('Оперативна пам\'ять, GB')
    graph_ax.set_ylabel('Оцінка')
    graph_ax.set_title('Графік залежності середньої оцінки телефонів\nвід оперативної пам\'яті')    

mng = plt.get_current_fig_manager()
mng.resize(1400, 700)

plt.show()
