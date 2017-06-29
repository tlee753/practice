# from an old homework


def create_db(file_name):
    """Creates a local SQLite database using the sqlite3 module and then creates a table called
    Inventory in the database. The table should be populated from a csv file. There will be three
    columns: item_name, Price, and Quantity. The composite key of the table will be (item_name, value).
    Price and Quantity will both be stored as integers in the database.

    Parameters:
    file_name: String -- the name of the csv file that contains the inventory

    Return:
    a connection the the created database
    """
    import csv
    import sqlite3

    csv_file = file_name
    with open("{}".format(csv_file), "r" ) as file:
        connection = sqlite3.connect("{}.sqlite3".format("data"))
        cursor = connection.cursor()
        cursor.execute("""DROP TABLE IF EXISTS Inventory""")
        cursor.execute("""CREATE TABLE Inventory( item_name not null, Price integer not null, Quantity integer, primary key (item_name, Price))""")
        reader = csv.reader(file)
        aList = [row for row in reader if row[0] != "Item Name"]

        for row in aList[1:]:
            # cursor.execute("INSERT INTO Inventory VALUES ({}, {}, {})".format(row[0], row[1], row[2]))
            cursor.execute("insert into Inventory values (?, ?, ?)", row)

    connection.commit()
    return sqlite3.connect("{}.sqlite3".format("data"))
