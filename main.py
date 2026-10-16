import sqlite3
import pandas as pd  # type: ignore[reportMissingModuleSource]

# ==========================================
# Part 1: Connecting to the Data
# ==========================================

# STEP 1A & 1B: Connect to the database
conn = sqlite3.connect("data.sqlite")

# Reference view of employee data
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")


# ==========================================
# Part 2: Basic Select Filtering
# ==========================================

# STEP 2: Assign employee number and last name to df_first_five
df_first_five = pd.read_sql(
    """
    SELECT employeeNumber, lastName 
    FROM employees
""",
    conn,
)


# STEP 3: Last name first, then employee number
df_five_reverse = pd.read_sql(
    """
    SELECT lastName, employeeNumber 
    FROM employees
""",
    conn,
)


# ==========================================
# Part 3: Aliasing in Select
# ==========================================

# STEP 4: Alias employee number column as 'ID'
df_alias = pd.read_sql(
    """
    SELECT lastName, employeeNumber AS ID 
    FROM employees
""",
    conn,
)


# ==========================================
# Part 4: CASE Function
# ==========================================

# STEP 5: Bin job titles into 'Executive' or 'Not Executive'
df_executive = pd.read_sql(
    """
    SELECT *,
           CASE 
               WHEN jobTitle = 'President' 
                 OR jobTitle = 'VP Sales' 
                 OR jobTitle = 'VP Marketing' THEN 'Executive'
               ELSE 'Not Executive'
           END AS role
    FROM employees
""",
    conn,
)


# ==========================================
# Part 5: Built-In Functions - Strings
# ==========================================

# STEP 6: Length of the last name for all employees
df_name_length = pd.read_sql(
    """
    SELECT LENGTH(lastName) AS name_length 
    FROM employees
""",
    conn,
)


# STEP 7: First two letters of each person's job title
df_short_title = pd.read_sql(
    """
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title 
    FROM employees
""",
    conn,
)


# ==========================================
# Part 6: Built-In Functions - Numerics
# ==========================================

# Reference view of order details data
order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")

# STEP 8: Total amount for all orders (sum of rounded total prices)
sum_total_price = list(
    pd.read_sql(
        """
    SELECT ROUND(priceEach * quantityOrdered) AS total_price
    FROM orderDetails
""",
        conn,
    ).sum()
)


# STEP 9: Format order date into separate day, month, and year columns
df_day_month_year = pd.read_sql(
    """
    SELECT orderDate,
           SUBSTR(orderDate, 9, 2) AS day,
           SUBSTR(orderDate, 6, 2) AS month,
           SUBSTR(orderDate, 1, 4) AS year
    FROM orders
""",
    conn,
)

# ==========================================
# Close the connection
# ==========================================
conn.close()