from django.test import TestCase
from rest_framework.test import APIClient
import random

TEST_COUNT = 1
while True:
    client = APIClient()
    data = {"id":random.randint(10**9,10**10),"unix_ts":random.randint(10**9,10**10),"user_id":random.randint(10**9,10**10),"event_name":list(random.choices(["login", "logout"], weights=[0.5,0.5]))[0]}
    response = client.post('/log/', data, format='json')
    print(f"Testcase {TEST_COUNT}")
    TEST_COUNT += 1

