import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='', database='python_mk10')
mycursor = mydb.cursor()


def display_name():
    mycursor.execute('SELECT namapelajar FROM pelajar')
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x[0])


def main():
    display_name()
    nama = input("sila masukkan nama palajar : ")
    sql = 'INSERT INTO pelajar (namapelajar) VALUES (%s)'
    mycursor.execute(sql, (nama,))
    mydb.commit()
    display_name()


if __name__ == '__main__':
    main()
