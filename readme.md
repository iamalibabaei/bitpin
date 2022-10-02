to run project first install project requirements using ```pip install -r requiremenets.txt```. then run ```python manage.py migrate``` to run migrations and then 
```python manage.py runserver``` to start project.

Also, you can create users using ```python manage.py createsuperuser```.

Then on ```/admin``` create posts. You can see list of posts at ```/api/posts```
and you can score for a post at ```/api/posts/{post_id}/score/```.
You should log in if you want to score.

This project is very simple and due to time shortage, there is no tests or makefile for you.

Just consider functionality.

As you said there are a lot of scores for a post, scores data are stored in post model as redundancy to improve performance. 