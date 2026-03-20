# Customer Order Management System

## Project Description
This project is a Python-based automation tool designed for a distribution company to manage customer orders efficiently.

It transitions manual spreadsheet or paper based records into a structured digital system that registers clients, products and orders, while automatically calculating totals and generating daily sales reports.

## System Architecture
The system follows a **modular architecture** where each business functionality is isolated into specific modules to ensure reusability and maintainability.

It operates via a terminal based interface.

### Key Modules:
* CLients Managements: Handles the registration  of client data (ID, Name, Email) using dictionaries.
* Product Management: Manages the catalog of available items using inmutable tuples.
* Order processing: Links clients and products to create orders and calculate total cost.
* Financials: Calculates the total revenue generated during the workday.
* Reporting: Generates a consolidated summary of daily operations.

## Data  structures
In compliance with the project's technical restrictions, **lists are strictly prohibited**.

The system uses:
**Dictionaries:** Used for storing and retrieving registered clients and orders due to their key-value efficiency.
**Tuples:** Used for representing inmutable products informartion, such as (product_id, product_name, unit_price)

## Funtional Features
The application includes six main funtionalities developed collaboratively:
1. **Client  Registration:** Store ID, name and emails.
2. **Product Registration:** Store product details in tuples.
3. **Order creation:** Associate clients with products and quantities.
4. **Order query:** Visualize all registered orders with detailed totals.
5. **Daily income calculation:** Sum of all orders processed during the session.
6. **Final report generation:** Summary of total orders, total revenue, orders  per client, and products sold.

## How to run the program
1. Ensure you have **Python3** installed.
2. Clone the repository from Github.
3. Open your terminal or command prompt.
4. Navigate to the project folder.
5. Run the main script:
    ```bash
    python main.py

## Development Process
This project was managed using **Agile practices** and **Github Issues**.
* User Story: "As a commercial operations manager, I want to register and process customer orders to maintain structured control and obtain consolidated reports".
* Task Management: All features were registered as task in the Product Backlog and assigned to team members for progress tracking.

## Team Credits
Developed by a team of 7 members, following the RIWI development challenge guidelines.

ºMenu -> Shelbymaz (coder)

ºUser Story <Communication (Azure and Discord)-> DereckDLR29 (Devops)

ºFt. User Registration -> Spideychill777 (Coder-Scrum M.)

ºFt. Products Registration -> BruhBx (Coder)

ºFt. Create Order -> Lejo33607 (Coder)

ºFt. Search Order -> Lejo33607 (Coder)

ºDebug and Fix errors -> CoderKing498 (QA)

ºFt. Daily Incomes -> DereckDLR29 and Ya7733 (Coders position)

ºFt. General Report. ->  Jgmez9 and danielbaneado ( Coder and Floor support)

ºDocumentation -> Spideychill (Scrum position).

ºFlowchart -> Rsofia28 and CoderKing498 (Project Designers).
