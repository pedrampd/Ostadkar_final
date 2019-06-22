from django.shortcuts import render
from api.forms import MainForm,OtherForm
from api.models import Main,OtherField
from pymongo import MongoClient
from Ostadkar_final.settings import HOST_NAME,DATABASE_NAME
from .serializers import MainSerializer as ms
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


        print(mobj.other_fk_id)
        if mform.is_valid() and oform.is_valid():
            # Connection
            myclient = MongoClient(HOST_NAME)
            mydb = myclient[DATABASE_NAME]
            maincol = mydb["api_test"]
            mainjson = ms(mobj)


            if oobj.other:
                try :
                    jsonfile = json.loads(oobj.other)
                    # maincol.insert_one(mainjson)

                    mainjson['other'] = jsonfile
                    maincol.insert(mainjson)
                except:
                    mainjson["other"] = oobj.other
                    maincol.insert(mainjson)
                    print("Could not load json")
            else:
                maincol.insert(mainjson)

    return render(request,'api/main.html', context={'form1':mform,'form2':oform})



