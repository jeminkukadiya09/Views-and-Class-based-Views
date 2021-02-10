import json
import requests

URL = "http://localhost:8000/studentapi/"

                  # GET METHOD

def get_data(id = None):
	data = {}
	if id is not None:
		data = {'id' : id}
	json_data = json.dumps(data)
	headers = {'content-Type' : 'application/json'}
	r = requests.get(url = URL, headers=headers, data = json_data)
	data = r.json()
	print(data)

#get_data()
   
                   # POST METHOD

def post_data():
	data = {
	 'name' : 'rohan',
	 'roll' : 198,
	 'city' : 'surat'
	}

	headers = {'content-Type' : 'application/json'}

	json_data = json.dumps(data)
	r = requests.post(url = URL, headers=headers, data = json_data)
	data = r.json()
	print(data)

#post_data()

                    # UPDATE METHOD

def update_data():
	data = {
	 'id' : 3,
	 'name' : 'jackY',
	 'city' : 'ranch',
	 'roll' : '99'
	}
	headers = {'content-Type' : 'application/json'}

	json_data = json.dumps(data)
	r = requests.put(url = URL, headers=headers, data = json_data)
	data = r.json()
	print(data)

update_data()
           
                        # DELETE METHOD

def delete_data():
	data = {'id' : 4}
	headers = {'content-Type' : 'application/json'}

	json_data = json.dumps(data)
	r= requests.delete(url = URL, headers=headers, data = json_data)
	data = r.json()
	print(data)

#delete_data()



