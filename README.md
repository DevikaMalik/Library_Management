# Library Management System in Python
Library Management System in python(tkinter) GUI based project in python using tkinter and Sqlite DB.
Functionalities provided by this project includes:
- Adding books
- Sorting books
- Searching books
- Adding members
- Issuing books
- Summary calculation
===========================================================================================
importlib/sqlite3/ tkinter /ttk
importlib===
    import_module("")
===========================================================================================
pack()===
The pack() method works by organizing widgets into horizontal or vertical boxes, with the ability to control their positioning and alignment. It takes various options to customize the layout, including:

fill: Determines whether the widget expands to fill the available space.

expand: Specifies whether the widget should grow if there is extra space.

side: Indicates the alignment of the widget within the box (TOP, BOTTOM, LEFT, or RIGHT).

ipadx: Sets the internal horizontal padding for the widget.

ipady: Sets the internal vertical padding for the widget.


==========================================================================================
con=sqlite3.connect("lms.db")
cur=con.cursor():-The cursor object is used to execute SQL queries and fetch data from a database. It is an object that represents a cursor on a database result set. It can be used to iterate over the results of a query, or to update or delete data in a database.
