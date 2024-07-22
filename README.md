# Dynamic SQLModel Class Generator

## Overview

This project dynamically generates an SQLModel class based on a JSON schema definition. It allows you to define your table schema in a JSON file and have the corresponding SQLModel class created programmatically.

## Features

- **Dynamic Model Creation**: Generate SQLModel classes based on JSON schema definitions.
- **Primary Key Handling**: Automatically set the `id` field as the primary key.
- **Flexible Schema Definition**: Define your schema in a JSON file.

## Prerequisites

- Python 3.7+
- SQLModel

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Ezhilarasan14/dynamic-sqlmodel-generator.git
   cd dynamic-sqlmodel-generator


2. **Create a Virtual Environment (optional but recommended)**

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


3. **Install Dependencies**

pip install sqlmodel

4.** Run the script with:**

python generate_model.py



