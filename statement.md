# Bakery Management System

## Problem Statement

Develop a **Bakery Management System** to help a bakery manage its products, customers, orders, inventory, and sales efficiently.

The system should allow the bakery staff to maintain information about different bakery products such as cakes, pastries, breads, cookies, and other items. It should also provide functionality for managing customer orders and keeping track of available stock.

## Objectives

The main objectives of the system are:

- Maintain a list of bakery products.
- Store product details such as name, category, price, and quantity.
- Allow customers to place orders.
- Calculate the total cost of an order.
- Update product stock after a sale.
- Maintain customer information.
- Display available products and their prices.
- Identify products that are out of stock or running low.
- Maintain a record of completed orders.

## Functional Requirements

### 1. Product Management

The system should allow the bakery staff to:

- Add new products.
- View all available products.
- Update product information.
- Remove products.
- Search for a particular product.
- Check product availability.

Each product may contain:

- Product ID
- Product Name
- Category
- Price
- Quantity Available

### 2. Customer Management

The system should maintain basic customer information, including:

- Customer ID
- Customer Name
- Phone Number
- Email Address

The system should allow staff to add, view, update, and search customer records.

### 3. Order Management

Customers should be able to place orders by selecting one or more products.

For each order, the system should store:

- Order ID
- Customer ID
- Products ordered
- Quantity of each product
- Order date
- Total amount
- Order status

The system should automatically calculate the total bill based on the selected products and quantities.

### 4. Inventory Management

The system should keep track of product stock.

Whenever an order is completed:

- The ordered quantity should be deducted from the available stock.
- The system should prevent customers from ordering more than the available quantity.
- Products with low stock should be identifiable.

### 5. Billing

The system should calculate the bill using:

**Total Amount = Σ (Product Price × Quantity)**

The bill should display:

- Order ID
- Customer details
- Products purchased
- Quantity
- Individual prices
- Subtotal
- Total amount

## Non-Functional Requirements

The system should be:

- **Easy to use** — Staff should be able to operate it without extensive training.
- **Reliable** — Product, customer, and order information should be stored accurately.
- **Efficient** — Common operations such as searching and placing orders should be quick.
- **Maintainable** — The code should be organized into logical modules.
- **Secure** — Only authorized staff should be able to modify important bakery records.

## Example

Suppose the bakery has the following products:

| Product | Price | Available Quantity |
|---|---:|---:|
| Chocolate Cake | ₹500 | 10 |
| Bread | ₹40 | 25 |
| Cookies | ₹120 | 15 |
| Pastry | ₹80 | 20 |

A customer orders:

- 1 Chocolate Cake
- 2 Pastries
- 3 Bread

The system should calculate:

```text
Chocolate Cake = 1 × ₹500 = ₹500
Pastry         = 2 × ₹80  = ₹160
Bread          = 3 × ₹40  = ₹120

Total = ₹780
```

The system should then update the inventory accordingly.

## Expected Outcome