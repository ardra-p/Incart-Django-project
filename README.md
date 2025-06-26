# 🛒 Simple E-Commerce Web App (Django)

This is a beginner-friendly e-commerce web application built using Django. It was created as a guided learning project to understand the core concepts of Django including views, models, authentication, and templates.

## 📌 Project Goal

To build a basic e-commerce site that supports:
- User registration and login
- Product listing and detail pages
- Shopping cart functionality
- Order checkout and order history

## 📚 What I Learned

- Django Models, Views, Templates (MVT)
- Handling POST requests and forms
- User authentication with decorators
- Managing related models (`User`, `Customer`, `Order`, `Product`, `OrderedItem`)
- Conditional rendering and message flashing
- Using `get_or_create()` for cart management
- Dynamic image loading in templates
- Reverse URLs and resolving `NoReverseMatch` issues

## 🧩 Features

- 🔐 User Authentication (Login required for checkout/cart)
- 🛍 Product Listing and Product Detail View
- 🛒 Add to Cart, Remove from Cart
- ✅ Order Checkout
- 📦 Order History (with images of ordered products)
- 🖼 Product images shown in orders
- 🔗 Dynamic routing using Django URL patterns
