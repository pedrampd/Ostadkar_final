from django.shortcuts import render
from api.forms import MainForm,OtherForm
from api.models import Main,OtherField
from pymongo import MongoClient
from Ostadkar_final.settings import HOST_NAME,DATABASE_NAME
import json


def main(request):
    mform = MainForm()
    oform = OtherForm()
    if request.method == 'POST':
        mform = MainForm(request.POST)
        oform = OtherForm(request.POST)
        oobj = OtherField()
        mobj = Main()
        mobj.sender = mform['sender'].value()
        mobj.datetime = mform['datetime'].value()
        mobj.priority = mform['priority'].value()
        mobj.description = mform['description'].value()
        oobj.other = oform['other'].value()
        if oobj.other:
            oobj.save()
            mobj.other_fk_id = oobj.id


        print(mobj.other_fk_id)
        if mform.is_valid() and oform.is_valid():
            # Connection
            myclient = MongoClient(HOST_NAME)
            mydb = myclient[DATABASE_NAME]
            mycol = mydb["api_otherfield"]

            if oobj.other:
                try :
                    jsonfile = json.loads(oobj.other)
                    jsonfile['id'] = oobj.id
                    mobj.other_fk_id = oobj.id
                    mycol.delete_one({"id":oobj.id})
                    mycol.insert_one(jsonfile)
                except:
                    print("Could not load json")

            mobj.save()
    return render(request,'api/main.html', context={'form1':mform,'form2':oform})



