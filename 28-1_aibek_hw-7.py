import sqlite3

# Создаем подключение к базе данных
connection_to_db = sqlite3.connect('hw.db')

# Создаем курсор
cursor = connection_to_db.cursor()

# Создаем таблицу products
cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  product_title TEXT VARCHAR(200) NOT NULL,
                  price DOUBLE(10,2) NOT NULL DEFAULT 0.0,
                  quantity INTEGER NOT NULL DEFAULT 0
                  )''')

# Добавляем 15 товаров
def add_products():
    products = [('Банное мыло', 99.99, 100),
                ('Жидкое мыло с запахом ванили', 49.99, 50),
                ('Мыло для душа с глицерином', 34.99, 75),
                ('Мыло туалетное с серой', 24.99, 150),
                ('Мыло с экстрактом ромашки', 10.99, 200),
                ('Мыло детское  с экстрактом череды', 2.99, 500),
                ('Item 7', 5.99, 300),
                ('Item 8', 15.99, 100),
                ('Item 9', 7.99, 250),
                ('Item 10', 19.99, 75),
                ('Item 11', 29.99, 50),
                ('Item 12', 14.99, 175),
                ('Item 13', 39.99, 25),
                ('Item 14', 89.99, 10),
                ('Item 15', 4.99, 400)]
    cursor.executemany('''INSERT INTO products (product_title, price, quantity)
                           VALUES (?, ?, ?)''', products)
    connection_to_db.commit()

# Меняем количество товара по ID
def update_quantity(quantity, id):
    cursor.execute('''UPDATE products SET quantity = ? WHERE id = ?''', (quantity, id))
    connection_to_db.commit()

# Меняем цену товара по ID
def update_price(price, id):
    cursor.execute('''UPDATE products SET price = ? WHERE id = ?''', (price, id))
    connection_to_db.commit()

# Удаляем товар по ID
def delete_product(id):
    cursor.execute('''DELETE FROM products WHERE id = ?''', (id,))
    connection_to_db.commit()

# Получаем все товары из БД
def get_all_products():
    cursor.execute('''SELECT * FROM products''')
    products = cursor.fetchall()
    for p in products:
        print(p)

# Ищем товары по названию
def search_products_by_title(keyword):
    cursor.execute('''SELECT * FROM products WHERE product_title LIKE ?''', ('%' + keyword + '%',))
    products = cursor.fetchall()
    for p in products:
        print(p)

# Выбираем все товары дешевле 100 сомов и количество которых больше 5
def get_products_cheaper_than_100_and_quantity_more_than_5():
    cursor.execute('''SELECT * FROM products WHERE price < 100 AND quantity > 5''')
    products = cursor.fetchall()
    for p in products:
        print(p)

# Добавляем 15 товаров
add_products()

# Меняем количество товара по ID
update_quantity(50, 1)

# Меняем цену товара по ID
update_price(119.99, 2)

# Удаляем товар по ID
delete_product(3)

# Получаем все товары из БД
get_all_products()

# Ищем товары по названию
search_products_by_title('мыло')

# Выбираем все товары дешевле 100 сомов и количество которых больше 5
get_products_cheaper_than_100_and_quantity_more_than_5()

# Закрываем подключение к базе данных
connection_to_db.close()