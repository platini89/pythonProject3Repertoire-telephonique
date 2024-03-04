print('hello')# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sqlite3

conn = sqlite3.connect('contactele.db') #connexion db
cur = conn.cursor()
cur.execute(""" CREATE TABLE Contact(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT ,
             prenom TEXT, 
             numero INTERGER, 
             message TEXT )
              
            """)
cur.execute("INSERT INTO CONTACT ( id , nom , prenom , nuemro , message)"
            " VALUE (1,'NANA', 'robert', +237674527429 )")
conn.commit()
conn.close()



#  (n’oubliez pas le double point !)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
