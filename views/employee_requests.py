import sqlite3
import json
from models import Employee, Location

EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis",
        "status": "New Hire"
    },
    {
        "id": 2,
        "name": "Marty Josedk",
        "status": "Old Hire"
    }
]

def get_all_employees():
    '''docstring'''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id,
            l.name location_name,
            l.address location_address
        FROM Employee a
        JOIN Location l
            ON l.id = a.location_id
                """)
        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:

            # Create an animal instance from the current row
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])

            # Create a Location instance from the current row
            location = Location(row['id'], row['location_name'], row['location_address'])

            # Add the dictionary representation of the location to the animal
            employee.location = location.__dict__

            # Add the dictionary representation of the animal to the list
            employees.append(employee.__dict__)

    return employees

def get_single_employee(id):
    '''docstring'''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id
        FROM employee a
        WHERE a.id = ?
        """, ( id, ))
        data = db_cursor.fetchone()
        employee = Employee(data['id'], data['name'], data['address'], data['location_id'])

        return employee.__dict__

def create_employee(employee):
    '''docstring'''
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee

'''
def delete_employee(id):
    employee_index = -1
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)
'''
def update_employee(id, new_employee):
    '''docstring'''
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break

def get_employee_by_location(location_id):
    '''docstring'''
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.location_id
        from Employee c
        WHERE c.location_id = ?
        """, ( location_id, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
            employees.append(employee.__dict__)

    return employees

def delete_employee(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM employee
        WHERE id = ?
        """, (id, ))
