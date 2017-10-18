import csv
import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#def get_csv():
#    csv_path = 'data.csv'
#    csv_file = open(csv_path, 'rb' )
#    csv_obj = csv.DictReader(csv_file)
#    srt = sorted(csv_obj, key=lambda row: row, reverse=True)#list sorted by lease amount in ascending order.
#    csv_list = list(srt)[:5]# [:5] display the first 5 items
#    return csv_list, csv_file

def get_csv():
    with open('data.csv', 'rb') as csv_file:
        csv_obj = csv.DictReader(csv_file) # here i suppose to replace white spaces for '_' and remove the '[]' in order to call each row at the frontend; if I cant, Im gonna change the data.csv, Property Name => Property_Name and [1] => 1
        srt = sorted(csv_obj, key=lambda row: row, reverse=True)#list sorted by lease amount in ascending order.
        csv_list = list(srt)[:5]# [:5] display the first 5 items
    return csv_list
#total rents
def total():
    csv_file = csv.reader(open("data.csv"))#try to get it from get_csv() instead
    dist = 0
    for row in csv_file:
        _dist = row[10]
        try: 
            _dist = float(_dist)
        except ValueError:
            _dist = 0

        dist += _dist
        print dist
    return dist
#toggle to desc order
@app.route("/toggle/", methods=['POST'])
def toggle_desc():
    with open('data.csv', 'rb') as csv_file:
        csv_obj = csv.DictReader(csv_file)
        srt = sorted(csv_obj, key=lambda row: row, reverse=False)#list sorted by lease amount in descending order.
        object_list = list(srt)[:5]
    col_sum = total()
    return render_template('home.html', object_list=object_list, col_sum=col_sum)


@app.route('/')
def index():
    template = 'home.html'
    object_list =  get_csv()#[0]
    col_sum = total()
    return render_template(template, object_list=object_list, col_sum=col_sum)
#write
@app.route('/write/', methods=['POST'])
def write():
    Property_Name = request.form['Property_Name']
    Property_Address_1 = request.form['Property_Address_1']
    Property_Address_2 = request.form['Property_Address_2']
    Property_Address_3 = request.form['Property_Address_3']
    Property_Address_4 = request.form['Property_Address_4']
    Unit_Name = request.form['Unit_Name']
    Tenant_Name = request.form['Tenant_Name']
    Lease_Start_Date = request.form['Lease_Start_Date']
    Lease_End_Date = request.form['Lease_End_Date']
    Lease_Years = request.form['Lease_Years']
    Current_Rent = request.form['Current_Rent']
    fieldnames=[
        'Property_Name',
        'Property_Address_1',
        'Property_Address_2',
        'Property_Address_3',
        'Property_Address_4',
        'Unit_Name',
        'Tenant_Name',
        'Lease_Start_Date',
        'Lease_End_Date',
        'Lease_Years',
        'Current_Rent']
    with open('data.csv','a') as inFile:
        writer = csv.DictWriter(inFile, fieldnames=fieldnames)
        writer.writerow({
            'Property_Name':Property_Name,
            'Property_Address_1':Property_Address_1,
            'Property_Address_2':Property_Address_2,
            'Property_Address_3':Property_Address_3,
            'Property_Address_4':Property_Address_4,
            'Unit_Name':Unit_Name,
            'Tenant_Name':Tenant_Name,
            'Lease_Start_Date':Lease_Start_Date,
            'Lease_End_Date':Lease_Years,
            'Current_Rent':Current_Rent
        })
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)