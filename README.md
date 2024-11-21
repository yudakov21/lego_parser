# LEGO Parser Project Description

LEGO Parser App is a Django-based web application designed for parsing and displaying information about discounts on LEGO toys. The program collects data from certain sites, saves it to a PostgreSQL database and provides a convenient web interface for viewing.

The application supports asynchronous processing of tasks using Celery and Redis, and uses Nginx to process requests and serve static files.

## Main features

Data parsing: Automatically collect information about LEGO toys (e.g. price, discount, number of parts, rating).

Asynchronous processing: Uses Celery to perform parsing in the background.

Data storage: Uses PostgreSQL database to store the information.

Web Interface: User-friendly web interface for viewing product data.

Scalability: Configured using Docker for easy deployment and scaling.

## Technology Stack

Backend: Python, Django

Frontend: HTML, CSS (with Bootstrap for basic design)

Asynchrony: Celery, Redis

Database: PostgreSQL

Web server: Nginx

Docker: Containerization of all components

Parsing: Selenium (using Firefox WebDriver)
