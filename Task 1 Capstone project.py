import sqlite3
db = sqlite3.connect('data/ebookstore_db')
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE books(id INTEGER PRIMARY KEY, Title TEXT,
                        Author TEXT, Qty INTEGER)
''')
db.commit()

cursor = db.cursor()
id1 = 3001
Title1 = 'A Tale of Two Cities'
Author1 = 'Charles Dickens'
Qty1 = 30


id2 = 3002
Title2 = 'Harry Potter and the Philosophers Stone'
Author2 = 'J.K.Rowling'
Qty2 = 40


id3 = 3003
Title3 = 'The Lion , the Witch and the Wardrobe'
Author3 = 'C.S.Lewis'
Qty3 = 25

id4 = 3004
Title4 = 'The Lord of the Rings'
Author4 = 'J.R.R Tolkien'
Qty4 = 37

id5 = 3005
Title5 = 'Alice Wonderland'
Author5 = 'Lewis Carroll'
Qty5 = 12
cursor.execute('''INSERT INTO books(id, name, grade)
                  VALUES(?,?,?,?)''', (id1, Title1, Author1, Qty1))
print('First user inserted')


cursor.execute('''INSERT INTO books(id , name, grade)
                  VALUES(?,?,?,?)''', (id2, Title2, Author2, Qty2))
print('Second user inserted')


cursor.execute('''INSERT INTO books(id ,name, grade)
                  VALUES(?,?,?,?)''', (id3, Title3, Author3, Qty3))
print('Third user inserted')


cursor.execute('''INSERT INTO books(id ,name, grade)
                  VALUES(?,?,?,?)''', (id4, Title4, Author4, Qty4))
print('Fourth user inserted')

cursor.execute('''INSERT INTO books(id ,name, grade)
                  VALUES(?,?,?,?)''', (id5, Title5, Author5, Qty5))
print('Fifth user inserted')

db.commit()

#The MENU THAT WILL BE DISPLAYED 
user_choice = 0
while user_choice != 5:
    user_choice = int(input("""(1Enter Book
                              2Select Book
                              3Delete Book
                              4Upload Book
                              5Exit)""")
if user_choice=1:
    INSERT_Book()
elif user_choice=2:
    UPDATE_Book()
elif user_choice=3:
    delete_Book()
elif user_choice=4:
    SELECT_Book()

# 1.# Where user enters new book into the data base


def INSERT_Book():
    db_config=read_db_config()
    query=('''INSERT INTO books(id, Title, Author , Qty)
                  VALUES(?,?,?,?)''', (id, Title, Author, Qty))
    cursor=conn.cursor()
    cursor.execute(query, (' '))
    conn.commit()

# 2.#Where the user can change the ID or the Qty of the Book. This is where the user can update the entries.I chose either ID and Qty because these are the two parameters that can change


def UPDATE_Book():
    db_config=read_db_config()
    query=('''UPDATE book SET QTY=? WHERE id=?''' ,(Qty,id))
    cursor=conn.cursor()
    cursor.execute(query, (' '))
    conn.commit()

# 3.#User can delete any book with Title they enter of the book.


def delete_Book():
    db_config=read_db_config()
    query=('''DELETE FROM books WHERE id =?''', (id,))
    cursor=conn.cursor()
    cursor.execute(query, (' '))
    conn.commit()
# 4.#Search


def SELECT_Book():
    db_config=read_db_config()
    query=('''SELECT id,Author FROM books WHERE id =? ''' , (id,))
    cursor=conn.cursor()
    cursor.execute(query, (' '))
    conn.commit()


db.commit()
db.close()
print('Connection to database closed')
