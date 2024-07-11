from pathlib import Path
from blog.models import post
import json
from django.contrib.auth.models import User

def create_posts():
    posts_file = Path(__file__).resolve().parent.parent / 'posts.json'

    with open(posts_file) as json_file:
        posts = json.load(json_file)
        
        
    for post_ in posts:
        post.objects.create(
            title=post_['title'],
            content=post_['content'],
            author =User.objects.get(id=post_['user_id'])
        )