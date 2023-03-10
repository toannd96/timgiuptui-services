# Timgiuptui services

<img src="./logo.png" alt="timgiuptui"
style="background-color: #fff; border-radius: 16px" width="96" height="96" />


Event-driven microservices for [timgiuptui.com](https://timgiuptui.com). All stacks are deployed on Google Cloud Platform.

## Tech stack

- Frameworks: FastAPI, Flask
- Database: Firestore
- Event handling: Cloud Pub/Sub
- Cronjob: Cloud Scheduler

## Installation

Each service has its own `README.md` file. Please refer to each service's `README.md` file for installation instructions.

Generally, you need to install the following:

- Python 3.8+
- Docker
- Docker Compose

For better development, you can install `shared` packages:

```bash
pip install -e shared/
```

## Diagrams

### System Design  

![image](https://user-images.githubusercontent.com/17960926/218121122-34a23910-a691-4c58-9fac-080184df2acf.png)

### Crawling Process  

![crawling-proccess](https://user-images.githubusercontent.com/17960926/216836847-6a86d51c-6784-496b-85ee-d0eef360801a.png)

### CI/CD Flow  

![cicd-flow](https://user-images.githubusercontent.com/17960926/216836862-a5dc2893-9477-4306-9389-0b53b238aa5e.png)

## Services

### gateway

- API gateway
- FastAPI

### crawler

- crawl news from different sources
- Flask

### articles

- CRUD articles
- FastAPI

### handler

- handle crawled news
- Flask

### platform

- manage analytic, configuration
- FastAPI

### search

- search articles
- FastAPI

### analytics

- analyze metrics from crawled news
- Flask
