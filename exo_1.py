import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime


# database name is "db" contains "friends" table
def db_examples():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="testdb"
    )

    mycursor = mydb.cursor()
    # Create table Friends
    # mycursor.execute("create table friends(fname varchar(20),phone Bigint(10))")

    n = input("Enter name of friend")
    p = int(input("phone no"))

    sql = "insert into friends(fname,phone) values(%s,%s)"
    val = (n,p)

    mycursor.execute(sql,val)
    mydb.commit()

    mydb.close()

def nd_array_example():
    """Redhape array"""
    a = np.array([[10,20],[30,40],[50,60],[70,80]])
    print("printing the original array")
    print(a)
    print(a.shape)

    a=a.reshape(2,4)
    print("printing the reshaped array..")
    print(a.shape)

def transpose_numpy_array():
    """Transpose of a matrix"""
    b =[[1,2,3],[10,20,30],[100,200,300]]

    d = np.array(b)
    print(d)

    e=d.T
    print(e)

def broad_casting():
    """MAtrix manipulation"""
    a = np.array([[1,2,3,4],[2,4,5,6],[10,20,39,3]])
    b = np.array([2,4,6,8])
    print("\nprinting array a..")
    print(a)
    print(a.shape)


    print("\nprinting array b..")
    print(b)
    print(b.shape)

    print("\nAdding arrays a and b ..")
    c = a + b
    print(c)

    print("\nMultiplying arrays a*b ..")
    d=a*b
    print(d)

def sort_array():
    """Use sort in array"""
    dtype = [('name', 'S10'), ('height', float), ('age', int),('gender','S10')]
    values = [('Swati', 5.4, 28, 'F'), ('Aavya', 4.2, 19, 'F'),('Nidhi', 5.8, 37, 'F'),('Deep', 6.1, 46,
            'M')]
    x=np.array(values, dtype=dtype)
    print(x)

    print("\n Sort by age")
    y=np.sort(x, order='age')
    print(y)

    z=np.sort(x, order=['age','height'])
    print(z)
    
def panda_library():
    """Panda series and Dataframe"""

    # name = np.array(['s','w','a','t','i'])
    # a = pd.Series(name)
    # print(a)

    # a.index=["1.1","1.2","1.3","1.4","1.5"]
    # print(a)

    dict = {"country": ["India", "Russia", "Australia", "United Kingdom",
    "South Africa"], "area": [9.516, 17.10, 3.286, 9.597, 12.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]}

    print("Dictionary")
    a = pd.DataFrame(dict)
    print(a)
    
    print("Index")
    a.index=["IN","RU","AUS","UK","SA"]
    print(a)

def create_scatter_bar_plot():
    """Data frame matplotlib"""
    df = pd.DataFrame({
        'name':['john','scott','jerry','james','bill','patrik','mike'],
        'age': [23,78,12,19,45,33,20],
        'gender':['M','F','M','M','M','F','M']
    })

    # a scratter plot
    df.plot(kind='scatter',x='age',y='gender',color='red')
    plt.show()

    # a bar plot
    df.plot(kind='bar',x='name',y='age')
    plt.show()

def show_table():
    """Show table"""
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="testdb"
    )

    mycursor = mydb.cursor()
    mycursor.execute("Show tables;")
    myresult = mycursor.fetchall()

    for tables in myresult:
        for field in tables:
            print(field)

def box_plot():
    """Use random randint in dataframe"""
    df = pd.DataFrame(np.random.rand(20,5),columns = ['A','B','C','D','E'])
    print(df)

    df.plot.box()
    plt.show()

def print_day_of_the_week_given_date():
    given_date = datetime(2020,6,1)

    return given_date.strftime('%A')

def current_time():
    now = datetime.now().time()
    return now

    

       









if __name__=='__main__':
    # nd_array_example()
    # transpose_numpy_array()
    # broad_casting()
    # sort_array()
    # panda_library()
    # create_scatter_bar_plot()
    # db_examples()
    # show_table()
    # box_plot()
    # print(print_day_of_the_week_given_date())
    print(current_time())
