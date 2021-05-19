from django.db import models

# Create your models here.

class Event:
    id: int
    name: str
    img: str 
    desc: str 
    price: int 
    
    