from django.core import serializers
def MainSerializer(obj):
    dict = {}
    dict['sender'] = str(obj.sender)
    dict['datetime'] = str(obj.datetime)
    dict['priority'] = str(obj.priority)
    dict['description'] = str(obj.description)
    return dict
