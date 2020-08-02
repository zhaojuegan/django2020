import datetime
from .import  register
# 自定义过滤器
@register.filter
def myuper(value,*args):
    return value.upper()
@register.filter()
def mylower(value,*args):
    return value.lower()
# register.filter(name='mylower',filter_func=mylower)
# 自定义标签
@register.simple_tag()
def show_name(name):
    return name
@register.simple_tag()
def time1(format_str):
    return datetime.datetime.now().strftime(format_str)