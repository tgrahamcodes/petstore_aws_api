import requests

expected = list([{'id': 1, 'type': 'dog', 'price': 249.99}, 
				 {'id': 2, 'type': 'cat', 'price': 124.99}, 
				 {'id': 3, 'type': 'fish', 'price': 0.99}
				 ])

expectedPet = {'id': 3, 'type': 'fish', 'price': 0.99}
newPet = {'id': 4, 'type': 'wolf', 'price': 99.99}

API_url = "https://x.execute-api.us-west-1.amazonaws.com/Initial/pets"

def call_get():
	response = requests.get(API_url)
	return response.json()

def call_get_by_id():
	pet = requests.get("https://x.execute-api.us-west-1.amazonaws.com/Initial/pets" + str(3))
	pet = pet.json()
	return pet

def test_GETs():
	assert call_get() == expected, f"Expected {expected}, but got {call_get()}"
	assert call_get_by_id() == expectedPet, f"Expected {expectedPet}, but got {call_get_by_id()}"

def test_POST():
	response = requests.post("https://x.execute-api.us-west-1.amazonaws.com/Initial/pets/", newPet)
	return response

def test_OPTIONS():
	pass

if __name__ == "__main__":
	test_GETs()
	print(call_get)

# newPet = {
# 	id: 4,
# 	'type': 'wolf',
# 	'price': 200
# }

# newResponse = requests.post(API_url, newPet)

# print('\nPOST:', newResponse.json(), '\n')


