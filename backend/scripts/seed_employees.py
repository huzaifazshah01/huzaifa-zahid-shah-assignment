import random
from datetime import date, timedelta

from app.core.database import SessionLocal
from app.models.employee import Employee


FIRST_NAMES = [
    "Rahul", "Ananya", "Karan", "Priya", "Neha", "Amit", "Sneha",
    "Rohit", "Pooja", "Arjun", "Simran", "Vikram", "Isha", "Manish",
    "Aarav", "Kavya", "Nikhil", "Riya", "Siddharth", "Meera"
]

LAST_NAMES = [
    "Sharma", "Verma", "Mehta", "Singh", "Gupta", "Malhotra",
    "Bansal", "Kapoor", "Chopra", "Agarwal"
]

DEPARTMENTS = {
    "Engineering": ["Software Engineer", "Senior Engineer", "Tech Lead"],
    "HR": ["HR Executive", "HR Manager"],
    "Finance": ["Financial Analyst", "Account Manager"],
    "Marketing": ["Marketing Executive", "Marketing Lead"],
    "Operations": ["Operations Analyst", "Operations Manager"],
}

COMPANIES = [
    "techforge.io",
    "peoplecore.co",
    "finbridge.in",
    "marketloop.co",
    "cloudnest.ai",
]


def random_joining_date():
    start = date(2018, 1, 1)
    end = date(2024, 12, 31)
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))


def seed_employees(count=50):
    db = SessionLocal()

    try:
        # Prevent duplicate seeding
        if db.query(Employee).first():
            print("Employees already exist. Skipping seeding.")
            return

        employees = []

        for i in range(count):
            first = random.choice(FIRST_NAMES)
            last = random.choice(LAST_NAMES)
            department = random.choice(list(DEPARTMENTS.keys()))
            designation = random.choice(DEPARTMENTS[department])
            company = random.choice(COMPANIES)

            email = f"{first.lower()}.{last.lower()}{i}@{company}"

            employees.append(
                Employee(
                    name=f"{first} {last}",
                    email=email,
                    department=department,
                    designation=designation,
                    date_of_joining=random_joining_date(),
                )
            )

        db.add_all(employees)
        db.commit()
        print(f"Seeded {count} employees successfully.")

    except Exception as e:
        db.rollback()
        print("Error while seeding data:", e)

    finally:
        db.close()


if __name__ == "__main__":
    seed_employees()
