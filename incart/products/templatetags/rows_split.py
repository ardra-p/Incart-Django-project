from django import template

register = template.Library()

@register.filter(name='rows_split')
def rows_split(list_data,row_size):
    i=0
    row = []
    for x in list_data:
        row.append(x)
        i = i+1
        if i == row_size:
            yield row
            i=0
            row=[]
    if row:
        yield row
