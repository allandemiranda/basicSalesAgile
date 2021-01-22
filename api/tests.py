import unittest
import json
import random
from app import app

# Config
header = {'content-type': 'application/json', 'Authorization': 'Bearer '}

# Auth
userAuth = {"password": ""}

# Global Words
user = {"user": {}}
sale = {"sale": {}}
product_id = {'ids': []}
sales_user = {'sales': []}
sales_ids = { 'ids':[]}
total_sales = { "total": 0.0 }

class TestApi(unittest.TestCase):  

    def __init__(self, *args, **kwargs):
        super(TestApi, self).__init__(*args, **kwargs)

    def setUp(self):
        self.app = app.test_client()

    def test_1_default(self):
        # Testing the test route
        respose = self.app.get('/api')

        # Checking if the route exists
        self.assertEqual(200, respose.status_code)
    
    def test_2_create_user(self):
        # Creating user data randomly
        name = ""
        for x in range(15):
            name += random.choice(['a', 'B', 'c', 'D', 'e', ' '])
        phone = "+" + str(random.randrange(0, 100, 2)) + " (" + str(random.randrange(0, 100, 2)) + ") " + str(random.randrange(0, 999999999, 2))
        user_name = ""
        for x in range(15):
            user_name += random.choice(['A', 'b', 'C', 'd', 'E', '_'])
        password = ""
        for x in range(15):
            password += random.choice(['A', 'b', 'C', 'd', 'E', '1', '2', '3'])

        # Preparing the request format
        body = {'name':name, 'phone':phone, 'user_name':user_name, 'password':password}
        respose = self.app.post('/api/user', data=json.dumps(body), headers=header)

        # Check if the response was successful
        self.assertEqual(201, respose.status_code)

        # Checks the parameters sent are the same as those returned
        self.assertEqual(name, json.loads(respose.data)['user']['name'])
        self.assertEqual(phone, json.loads(respose.data)['user']['phone'])
        self.assertEqual(user_name, json.loads(respose.data)['user']['user_name'])

        # Save the necessary information for the next tests
        user['user'] = json.loads(respose.data)['user']
        userAuth['password'] = password
        
    def test_3_auth_local(self):
        # Use the user data created for the login
        body = {'user_name': user['user']['user_name'], 'password': userAuth['password']}
        respose = self.app.post('/api/auth/local', data=json.dumps(body), headers=header)
        
        # Check if the response was successful
        self.assertEqual(200, respose.status_code)

        # Check if the created user is the same one who logged in
        self.assertEqual(user['user'], json.loads(respose.data)['user'])
        
        # Save the session token
        header['Authorization'] = header['Authorization'] + json.loads(respose.data)['token']
        
    def test_4_get_user_by_id(self):
        # Check if the logged user id returns the correct user
        respose = self.app.get('/api/user/' + str(user['user']['id']), headers=header)
        
        # Checks if the response was successful
        self.assertEqual(200, respose.status_code)

        # Check if the users are the same
        self.assertEqual(user, json.loads(respose.data))

    def test_5_create_products(self):
        # Create 10 products randomly
        for x in range(10):
            # Creating product data randomly
            name = ""
            for x in range(15):
                name += random.choice(['a', 'B', 'c', 'D', 'e', ' '])
            value = random.random() * random.randrange(1,1000, 2)

            # Preparing the request format
            body = {'name':name, 'value':value}
            respose = self.app.post('/api/product', data=json.dumps(body), headers=header)

            # Check if the response was successful
            self.assertEqual(201, respose.status_code)

            # Checks the parameters sent are the same as those returned
            self.assertEqual(name, json.loads(respose.data)['product']['name'])
            self.assertEqual(value, json.loads(respose.data)['product']['value'])

            # Save product id's created for use in other tests
            product_id['ids'].append(int(json.loads(respose.data)['product']['id']))

            # Open the product list
            old_response = respose.data
            respose = self.app.get('/api/products/', headers=header)

            # Check if the response was successful
            self.assertEqual(200, respose.status_code)

            # Check if the created product is in the list of all products
            self.assertIn(json.loads(old_response)['product'], json.loads(respose.data)['products'])
    
    def test_6_create_sales(self):        
        temp_total = 0

        # Create 10 sales randomly for the logged in user
        for x in range(10):
            # Choose a product id created and create too much data randomly
            id = random.choice(product_id['ids'])
            quantity = random.randrange(1,1000, 2)
            total = random.random() * random.randrange(1,1000, 2)

            # Preparing the request format
            body = {'product_id':id, 'quantity':quantity, 'total':total}
            respose = self.app.post('/api/sale', data=json.dumps(body), headers=header)

            # Check if the response was successful
            self.assertEqual(201, respose.status_code)

            # Checks the parameters sent are the same as those returned
            self.assertEqual(quantity, json.loads(respose.data)['sale']['quantity'])
            self.assertEqual(total, json.loads(respose.data)['sale']['total'])
            self.assertEqual(user['user'], json.loads(respose.data)['sale']['user'])

            # Save the information for use in other tests
            sales_user['sales'].append(json.loads(respose.data)['sale'])

            # Check if the sale made corresponds to the same one that was created
            old_response = respose.data
            respose = self.app.get('/api/sale/' + str(json.loads(respose.data)['sale']['id']), headers=header)
            
            # Check if the response was successful
            self.assertEqual(200, respose.status_code)

            # Make sure they are the same sale
            self.assertEqual(json.loads(old_response), json.loads(respose.data))

            # Open the sales list
            old_response = respose.data
            respose = self.app.get('/api/sales/', headers=header)

            # Check if the response was successful
            self.assertEqual(200, respose.status_code)

            # Check if the created sale is on the sales list
            self.assertIn(json.loads(old_response)['sale'], json.loads(respose.data)['sales'])
            
            # Add the total sale to check other tests
            temp_total += total           

        # Save the user's total sales information for use in other tests    
        total_sales['total'] = str(temp_total)
     
    def test_7_sales_by_userId(self):
        # Open the sales list of the logged in user
        respose = self.app.get(
            '/api/user/' + str(user['user']['id']) + '/sales/', headers=header)

        # Check if the response was successful
        self.assertEqual(200, respose.status_code)

        # Check that the list created in the previous test matches the list now
        self.assertEqual(sales_user['sales'], json.loads(respose.data)['sales'])

        # Add the total sales by checking if they all correspond to the logged in user
        temp_sale = 0
        for user_sale in json.loads(respose.data)['sales']:
            temp_sale += user_sale['total']
            self.assertEqual(user['user'],user_sale['user'])

        # Check if the total sales match
        self.assertEqual(total_sales['total'], str(temp_sale))

    def test_8_top_users(self):
        # Check if the top 5 route exists
        respose = self.app.get('/api/topUsers/', headers=header)
        self.assertEqual(200, respose.status_code)

    def test_9_get_users(self):   
        # Open the list of users    
        respose = self.app.get('/api/users/', headers=header)

        # Check if the response was successful
        self.assertEqual(200, respose.status_code)

        # Check if the logged in user is in the user list
        flag = False
        for user_info in json.loads(respose.data)['users']:
            if(user_info['user'] == user['user']):
                # Check that the total sales match to the previous test
                self.assertEqual(round(json.loads(str(total_sales['total'])),2), json.loads(str(user_info['sale'])))
                flag = True
        self.assertEqual(True, flag)

if __name__ == "__main__":
    unittest.main()
