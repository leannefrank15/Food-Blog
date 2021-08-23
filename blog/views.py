from django.shortcuts import render
from datetime import date
all_posts=[
    {
        "slug": "gluten-free-donuts",
        "image": "donuts.jpg",
        "author": "Leanne",
        "date": date(2021,8,23),
        "title": "Gluten-Free Cinnamon Donuts",
        "excerpt" : "Donuts that are gluten-free AND low calorie??? You've got to try these!!",
        "content" : """ 
           Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem ratione, veniam 
           maiores a vero eligendi odit accusantium incidunt esse excepturi sit beatae mollitia.
           Ipsam dolorem mollitia, cupiditate ullam esse quia!

           Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem ratione, veniam 
           maiores a vero eligendi odit accusantium incidunt esse excepturi sit beatae mollitia.
           Ipsam dolorem mollitia, cupiditate ullam esse quia!

           Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem ratione, veniam 
           maiores a vero eligendi odit accusantium incidunt esse excepturi sit beatae mollitia.
           Ipsam dolorem mollitia, cupiditate ullam esse quia!
        """
    },
    {
        "slug": "keto-pizza",
        "image": "pizza.jpg",
        "author": "Leanne",
        "date": date(2021, 8, 19),
        "title": "Cauliflower Crust Keto Pizza",
        "excerpt": "Delicious Keto Pizza which is low in carbs but a 10/10 in taste.",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "chocolate-chip-cookies",
        "image": "cookies.jpg",
        "author": "Leanne",
        "date": date(2021, 8, 23),
        "title": "Moist Chocolate-Chip Cookies",
        "excerpt": "Make these cookies with ingredients available at home. Check it out!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts=sorted(all_posts, key=get_date)
    latest_posts=sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts" : all_posts
    })


def post_detail(request, slug): #imp
    single_post = next(post for post in all_posts if post['slug']==slug)
    return render(request, "blog/post-detail.html",{
        "single_post" : single_post
    })
