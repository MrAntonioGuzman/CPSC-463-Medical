from django.test import TestCase
from django.urls import reverse


class PatientTests(TestCase):
    '''
        START TESTING LOGIN AND SIGNUP VIEW
    '''

    # TESTING STATUS CODE (SHOULD BE 200)
    def test_login_view_status_code(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    # TESTING STATUS CODE (SHOULD BE 200)
    def test_sign_up_view_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    print('TESTING LOGIN AND SIGNUP PAGE COMPLETE')

    '''
        END TESTING LOGIN AND SIGNUP VIEW
    '''