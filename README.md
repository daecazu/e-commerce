
<h3 align="center">Omnilatam technical Test</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/daecazu/e-commerce.svg)](https://github.com/daecazu/e-commerce/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/daecazu/e-commerce.svg)](https://github.com/daecazu/e-commerce/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> A company requires a relational database to manage users, products, orders,
payments, and shipments. Please refer only to the minimum needed attributes for an e-
commerce flow.
    <br> 
</p>

## 📝 Table of Contents

- [Considerations](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 Considerations <a name = "about"></a>

- A user can purchase products as part of an order.
- A payment can apply to one or more orders and an order can be paid by one or
more payments.
- An order can delivered by one or more shipments.
- A notification to the purchasers (users) should be sent when a shipment is sent/re-
ceived.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

- docker
- updated versión of docker compose at least 1.25

### Installing

rename/copy the development example file to base directory

- 'cp .env.example .env'

for installing you need to run the following commands

- 'docker-compose build'
- 'docker-compose up'



## 🔧 Running the tests <a name = "tests"></a>

if you want to run the automated tests for this system.

- docker-compose run --rm django sh -c 'pytest'
- docker-compose run --rm django sh -c 'flake8'

### Break down into end to end tests

implemented tests so far

- test extended user model
- test admin
- test users


## 🎈 Usage <a name="usage"></a>

Add notes about how to use the system.

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>

- [Postgresql](https://www.postgresql.org/) - Database
- [Python](https://www.python.org/) - Languaje
- [Django](https://www.djangoproject.com/) - framework
- [Celery](https://docs.celeryproject.org/) - Async task queue
- [Redis](https://redis.io/) - Broker and cache

## ✍️ Authors <a name = "authors"></a>

- [@daecazu](https://github.com/daecazu) - author
