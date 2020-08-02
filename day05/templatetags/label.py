from . import register

@register.inclusion_tag('show_tags.html')
def labes_view(persion):
    item = [
        {
          'name':'zjf',
          'age':18,
        }
    ]
    return {
        'item':item,
        'persion':persion,
    }