# ZataHub - Blockchain/Backend Developer Assignment

Welcome to ZataHub's Blockchain/Backend Developer Assignment! This document outlines the details of the task, providing you with an opportunity to demonstrate your skills in blockchain development. Your assignment will be pivotal in showcasing your technical abilities and problem-solving prowess. Thank you for your interest in joining ZataHub Company. We look forward to reviewing your submission.
This assignment is expected to require approximately **2 to 3 hours** for completion. However, the deadline for submission is set at **3 days** from the assignment distribution.

## Requirement

- There are two models in this project. Meeting and Note models. One Meeting might have multiple Note. Each Note belong to one Meeting. You can take a look on `app/models.py` to understand about this.

##### Task 1: Complete saving a Note API.

- Go to the file `app/views.py` and complete `# TODO` in `post` method. This method is the API of saving a Note. When a note is saved, we need to store note content into database and publish note content to blockchain network.
- You need to call `Ganache.publish_string(str)` to publish a content to blockchain network, this method will return a transaction_id for you. Then, you need to assign this transaction_id to note.publish_transaction_id then save the note to local database.
- The method `Ganache.publish_string(str)` might take about several seconds to complete. However API of saving note might be called many times within a second. Hence, multi-thread handling is required.
- This method will return HTTP_201_CREATED status for success case.

##### Task 2: Complete unit test

- Go to `app/tests/test_note_view.py` and complete `# TODO` there. This is only one unit test you need to complete. This unit test will test success case of the API in Task 1.

##### Note

- In order to save your time and effort, we have already set up the project. What you need to do is doing in `# TODO` only.
- You don't have to worries much about understanding requirement. The key important in this assignment is how you handle multi-thread and how you write unit test.
- Complete one unit test is enough for us to see your skill. You don't have to write more tests to cover 100% of API behaviours.
- There is nothing need to do with Meeting model. You can create mock records of Meeting model for testing purpose if you want.

## How to run the project

##### If you are using MacOS, Linux or Ubuntu

1. `cd` into the project folder and then run `virtualenv venv`
2. Run `source venv/bin/activate`
3. Run `pip install -r requirements.txt`
4. Run Ganache by `python ganache.py start`
5. Run `python manage.py migrate`
6. (optional) Run `python manage.py createsuperuser`
7. Run `python manage.py runserver`
8. (optional) When you stop working, you should run `python ganache.py stop` to quit Ganache

##### If you are using Windows

1. `cd` into the project folder and then run `virtualenv venv`
2. If Windows, run `venv\Scripts\activate`
3. Run `pip install -r requirements_windows.txt`
4. Run Ganache by `python ganache_windows.py start`
5. Run `python manage.py migrate`
6. (optional) Run `python manage.py createsuperuser`
7. Run `python manage.py runserver`
8. (optional) When you stop working, you should run `python ganache_windows.py stop` to quit Ganache

## Submission

After you complete this assignment, please compress the source code and then send it back to recruiter. We will review and get back to you within 2 working days.
