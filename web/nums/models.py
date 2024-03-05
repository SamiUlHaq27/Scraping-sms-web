from django.db import models

# 1 hour ago
# 2 hours ago
# 1 min ago
# 2 mins ago
# 1 day ago
# 2 days ago


class Country(models.Model):
    
    name = models.CharField(max_length=50)
    link = models.URLField()
    numbers = models.IntegerField(default=0)
    slug_id = models.CharField(max_length = 50, default="oops")
    updated_at = models.DateTimeField(auto_now=True)
    flag = models.CharField(max_length=10, default="au")
    
    def __str__(self):
        return self.name

class Number(models.Model):
    
    number = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    active_since = models.CharField(max_length=20)
    sms = models.IntegerField(default=0)
    link = models.URLField()
    slug_id = models.CharField(max_length = 50, default="oops")
    updated_at = models.DateTimeField(auto_now=True)
    country_flag = models.CharField(max_length=10, default="au")
    country_slug = models.CharField(max_length=50, default="/")
    
    def __str__(self) -> str:
        return self.number

class Message(models.Model):
    
    number = models.CharField(max_length=50)
    at_time = models.CharField(max_length=20)
    from_sndr = models.CharField(max_length=20)
    text = models.TextField()
    
    def __str__(self) -> str:
        return f"[{self.from_sndr} : {self.at_time}]"

