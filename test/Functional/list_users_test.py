from app import app 
import json


class TestListUsers:
    def test_get_all_users(self):
        #Arrange 
        UserFactory.create[{
            'name': "jorge",
            'apellido': "Gonzalez",
            'edad':34
        }]

        #Act
        
        response = app.test_client().get('/users')

        # Assert
        
        assert response.status_code==200
        parsed_data = json.load(response.data.decode('utf-8'))
        assert parsed_data == [{
            'name': "jorge",
            'apellido': "Gonzalez",
            'edad':34
        }]
