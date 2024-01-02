insert into Cellphone(cellphone_id, brand, model)
values
	(0, 'Samsung', 'Galaxy A10'),
	(1, 'Samsung', 'Galaxy J6 Plus'),
	(2, 'Samsung', 'Galaxy S12'),
	(3, 'Apple', 'iPhone 6'),
	(4, 'Apple', 'iPhone 6 Pro'),
	(5, 'OnePlus', '9 Pro');
	
	
insert into	Users(user_id, age, gender, profession)
values
	(0, 23, 'Male', 'Manager'),
	(1, 30, 'Female', 'IT'),
	(2, 24, 'Female', 'IT'),
	(3, 40, 'Male', 'Manager'),
	(4, 20, 'Female', 'Sales');

insert into Characteristic(cellphone_id, os, internal_memory, ram, main_camera, selfie_camera, battery_size)
values
	(0, 'Android', 64, 6, 50, 12, 3000),
	(1, 'Android', 32, 4, 30, 10, 2500),
	(2, 'Android', 128, 8, 64, 32, 4000),
	(3, 'IOS', 64, 4, 20, 10, 2000),
	(4, 'IOS', 64, 4, 20, 15, 2450),
	(5, 'Android', 32, 4, 45, 20, 3500);
	
insert into Rating(user_id, cellphone_id, grade)
values
	(0, 4, 6),
	(0, 1, 1),
	(0, 3, 7),
	(1, 5, 8),
	(1, 1, 1),
	(2, 2, 9),
	(3, 0, 3),
	(4, 5, 2);