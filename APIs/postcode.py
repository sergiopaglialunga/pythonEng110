import requests

# postcode, country, region, admin_district, parish
# The Postcode object will be initialised by passing in a dictionary

class Postcode:
    def __init__(self, result_dict):
        self.postcode = result_dict['postcode']
        self.country = result_dict['country']
        self.region = result_dict['region']
        self.admin_district = result_dict['admin_district']
        self.parish = result_dict['parish']


