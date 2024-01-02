-- 2.a Середня оцінка кожного телефону користувачами 
select trim(model) as model, round(avg(grade), 0) as grade_avg from cellphone, rating
where cellphone.cellphone_id = rating.cellphone_id
group by cellphone.cellphone_id
order by model;

-- 2.b Кількість телефонів кожного бренду
select trim(brand) as brand, count(*) as number_phone from Cellphone
group by brand;

-- 2.c Середня оцінка телефонів з однаковою оперативною пам'яттю
select ram, round(avg(grade), 2) as grade_avg from rating natural join characteristic
group by ram
order by ram;
