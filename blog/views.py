from django.shortcuts import render
from datetime import date
from copy import deepcopy

all_posts = [
    {
        "slug": "dota2",
        "image": "dota2.jpg",
        "author": "Özgür",
        "date": date(2021, 7, 22),
        "title": "Dota2 Review",
        "excerpt": "Defence of the ancients review",
        "content": """Lorem ipsum dolor, sit amet consectetur adipisicing elit.
                Nam quam fuga fugit, accusantium dolorum tempora animi 
                magnam ad doloremque facilis voluptatibus natus? Numquam 
                nisi reiciendis reprehenderit quam modi incidunt aut?
                """,
    },
    {
        "slug": "cyberpunk",
        "image": "cyberpunk.jpg",
        "author": "Özgür",
        "date": date(2022, 6, 11),
        "title": "Cyberpunk Review",
        "excerpt": "Cyberpunk review",
        "content": """Lorem ipsum dolor, sit amet consectetur adipisicing elit.
                Nam quam fuga fugit, accusantium dolorum tempora animi 
                magnam ad doloremque facilis voluptatibus natus? Numquam 
                nisi reiciendis reprehenderit quam modi incidunt aut?
                """,
    },
    {
        "slug": "darkest-dungeon-2",
        "image": "darkest_dungeon2.jpg",
        "author": "Özgür",
        "date": date(2020, 7, 16),
        "title": "Darkest Dungeon 2",
        "excerpt": "Darkest Dungeon 2 is review",
        "content": """Lorem ipsum dolor, sit amet consectetur adipisicing elit.
                Nam quam fuga fugit, accusantium dolorum tempora animi 
                magnam ad doloremque facilis voluptatibus natus? Numquam 
                nisi reiciendis reprehenderit quam modi incidunt aut?
                """,
    }
]
# Create your views here.

def index(request):
    post_list = deepcopy(all_posts)
    post_list.sort(key=lambda post: post.get("date"))
    posts = post_list[-3:]
    return render(request, "blog/index.html", {"posts": posts})

def posts(reqests):
    post_list = deepcopy(all_posts)
    post_list.sort(key=lambda post: post.get("date"))
    return render(reqests, "blog/posts.html", {"posts": post_list})

def post_detail(request, slug):
    selected_post = next(post for post in all_posts if post.get("slug") == slug)
    return render(request, "blog/post-detail.html", {"post": selected_post})
