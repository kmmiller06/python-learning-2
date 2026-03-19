print("Problem 1: Employee Payroll System with Polymorphism")
from abc import ABC, abstractmethod
from typing import Self

class Employee(ABC):
    def __init__(self, name, employee_id):
        self._name = name
        self._employee_id = employee_id

    @abstractmethod
    def calculate_pay(self):
        pass    

    @abstractmethod
    def description(self):
        pass

    def pay_stub(self):
        pay = self.calculate_pay()
        return f"{self._name} (ID: {self._employee_id}): ${pay:.2f}"    

    @staticmethod
    def validate_positive(value, name):
        if value <= 0:
            raise ValueError(f"{name} must be positive")
        return True


class SalariedEmployee(Employee):
    def __init__(self, name, employee_id, annual_salary):
        super().__init__(name, employee_id)
        self.validate_positive(annual_salary, "Annual salary")
        self._annual_salary = annual_salary

    def calculate_pay(self):
        return self._annual_salary / 24

    def description(self):
        return f"Salaried: {self._name}"


class HourlyEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.validate_positive(hourly_rate, "Hourly rate")
        self.validate_positive(hours_worked, "Hours worked")
        self._hourly_rate = hourly_rate
        self._hours_worked = hours_worked

    def calculate_pay(self):
        if self._hours_worked <= 40:
            return self._hourly_rate * self._hours_worked
        else:
            regular_pay = self._hourly_rate * 40
            overtime_hours = self._hours_worked - 40
            overtime_pay = self._hourly_rate * 1.5 * overtime_hours
            return regular_pay + overtime_pay

    def description(self):
        return f"Hourly: {self._name}"


class CommissionEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, sales, commission_rate):
        super().__init__(name, employee_id)
        self.validate_positive(base_salary, "Base salary")
        self.validate_positive(sales, "Sales")
        if not 0 <= commission_rate <= 1.0:
            raise ValueError("Commission rate must be between 0 and 1.0")
        self._base_salary = base_salary
        self._sales = sales
        self._commission_rate = commission_rate

    def calculate_pay(self):
        return self._base_salary + (self._sales * self._commission_rate)

    def description(self):
        return f"Commission: {self._name}"


class Payroll:
    def __init__(self):
        self._employees = []

    def add_employee(self, employee):
        self._employees.append(employee)

    def total_payroll(self):
        return sum(emp.calculate_pay() for emp in self._employees)

    def print_all_stubs(self):
        for emp in self._employees:
            print(emp.pay_stub())


# Test your code
if __name__ == "__main__":
    # Create employees
    alice = SalariedEmployee("Alice Johnson", "E001", 84000)
    bob = HourlyEmployee("Bob Smith", "E002", 25.00, 45)
    carol = CommissionEmployee("Carol Davis", "E003", 2000, 50000, 0.05)

    # Test individual employees
    print("Employee Descriptions:")
    for emp in [alice, bob, carol]:
        print(f" {emp.description()}")

    print("\nPay Stubs:")
    for emp in [alice, bob, carol]:
        print(f" {emp.pay_stub()}")

    # Test payroll (polymorphism!)
    payroll = Payroll()
    payroll.add_employee(alice)
    payroll.add_employee(bob)
    payroll.add_employee(carol)

    print(f"\nTotal Payroll: ${payroll.total_payroll():.2f}")

    # Test validation
    print("\nTesting validation:")
    try:
        bad = SalariedEmployee("Bad", "E999", -50000)
    except ValueError as e:
        print(f" Caught: {e}")

    try:
        bad = CommissionEmployee("Bad", "E999", 1000, 5000, 1.5)
    except ValueError as e:
        print(f" Caught: {e}")