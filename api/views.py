from django.shortcuts import render
from api.forms import MainForm,OtherForm
from api.models import Main,OtherField
from pymongo import MongoClient
import json
# Create your views here.
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
        oobj.save()
        mobj.other_fk_id = oobj.id
        print(mobj.other_fk_id)
        if mform.is_valid() and oform.is_valid():
            myclient = MongoClient("mongodb://localhost:27017/")
            mydb = myclient["Db"]
            mycol = mydb["api_otherfield"]
            jsonfile = json.loads(oobj.other)
            oobj.save()
            jsonfile['id'] = oobj.id
            mobj.other_fk_id = oobj.id
            mycol.delete_one({"id":oobj.id})
            mycol.insert_one(jsonfile)

            # mobj.other_fk_id = x.inserted_id


            mobj.save()


    return render(request,'api/main.html', context={'form1':mform,'form2':oform})

