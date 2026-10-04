# Student Performance Prediction API

A cloud-deployed machine learning REST API that predicts a student's expected score based on study hours, attendance, and previous score.

## Features

- REST API using Flask
- Machine learning prediction using Scikit-learn
- Docker containerization
- Cloud deployment using Render
- Automated testing using Pytest
- Continuous Integration using GitHub Actions
- Four automated test cases

## Technologies

- Python
- Flask
- Scikit-learn
- Docker
- Pytest
- GitHub Actions
- Render

## Architecture

```text
Client
   |
   v
Render Cloud
   |
   v
Docker Container
   |
   v
Flask REST API
   |
   v
Machine Learning Model
   |
   v
Predicted Score
