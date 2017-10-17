import csv
from flask import Flask, render_template

app = Flask(__name__)

#def get_csv():
#    csv_path = 'data.csv'
#    csv_file = open(csv_path, 'rb' )
#    csv_obj = csv.DictReader(csv_file, delimiter=' ')
#    csv_list = list(csv_obj)
#    return csv_list

def get_csv():
    with open('data.csv', 'rb') as csv_file:
        csv_obj = csv.DictReader(csv_file)
        # here i suppose to replace white spaces for '_' and remove the '[]' in order to call each row at the frontend
        #if I cant, Im gonna change the data.csv, Property Name => Property_Name and [1] => 1
        csv_list = list(csv_obj)
    return csv_list

@app.route('/')
def index():
    template = 'home.html'
    object_list =  get_csv()
    return render_template(template, object_list=object_list)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)