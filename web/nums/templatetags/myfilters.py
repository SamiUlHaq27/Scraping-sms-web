from django import template
from datetime import datetime

register = template.Library()

@register.simple_tag()
def showTime(time:datetime):
    time = time.replace(tzinfo=None)
    nowTime = datetime.now()
    newTime = nowTime - time
    str_time = str(newTime.seconds) + " seconds ago"
    if(newTime.seconds > 59):
        str_time = str(int(newTime.seconds/60 )) + " minutes ago"
        if(newTime.seconds/60 > 59):
            str_time = str(int(newTime.seconds/(3600))) + " hours ago"
            if(newTime.seconds/(3600) > 24):
                str_time = str(int(newTime.seconds/(3600*24))) + " days ago"
                    
    return str_time