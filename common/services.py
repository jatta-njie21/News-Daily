def get_all(object):
    return object.all()

def get_item(object,**kwargs):
    return object.get(**kwargs)

def filter_item(object,**kwargs):
    return object.filter(**kwargs)