import sqlite3
conn = sqlite3.connect('basedonne.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
 id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
 name TEXT,
 age INTERGER
)
""")
conn.commit()
cursor.execute("""
INSERT INTO users(name, age) VALUES(?, ?)""", ("olivier", 30))

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
