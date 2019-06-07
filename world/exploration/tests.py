from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class ShardhavenTest(APITestCase):

    def test_shardhaven(self):
        """Tests Shardhaven Map Editor"""
        url = reverse('exploration:get_haven_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
