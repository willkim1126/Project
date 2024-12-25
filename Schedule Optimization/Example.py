import pandas as pd
import random

# Example employee data
example_data = {
    'employee_id': [f'EMP{i:03}' for i in range(1, 16)],
    'name': [
        'Alice Smith', 'Bob Johnson', 'Charlie Brown', 'Diana Prince', 'Ethan Hunt',
        'Fiona Gallagher', 'George Lucas', 'Hannah Montana', 'Ivy League', 'Jack Sparrow',
        'Katy Perry', 'Leonardo DiCaprio', 'Mona Lisa', 'Noah Smith', 'Oliver Twist'
    ],
    'position': ['Lead'] * 5 + ['Staff'] * 10,
    # Randomized location preferences
    'location_preferences': [
        ','.join(random.sample(['The Trove', 'Seventh', 'ERC', 'CSC'], k=random.randint(2, 4)))
        for _ in range(15)
    ],
    # Complex availability patterns for preferred days
    'Monday': [random.choice(['09:00-11:00,13:00-15:00', '07:00-09:00,12:00-14:00']) for _ in range(15)],
    'Tuesday': [random.choice(['10:00-12:30', '', None]) for _ in range(15)],
    'Wednesday': [random.choice(['08:00-10:00,14:00-15:30', '', None]) for _ in range(15)],
    'Thursday': [random.choice(['07:30-09:30,13:00-15:30', '', None]) for _ in range(15)],
    'Friday': [random.choice(['13:00-15:30', '', None]) for _ in range(15)]
}

# Create DataFrame
example_df = pd.DataFrame(example_data)

# Save to Excel
example_df.to_excel('example_split_shifts.xlsx', index=False)
