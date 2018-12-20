from django.test import TestCase
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User


# Testing creates test databases, so the main database is unaffected!
# 200 means GOOD, 302 means a REDIRECTION occurred
class DashboardTests(TestCase):
    '''
        START TESTING HOME PAGE
    '''
    # Testing if non authenticated users are redirected to login page
    def test_home_view_no_login_redirection(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertRedirects(response, '/?next=/home/')

    # Testing if authenticated user can access authenticated page
    def test_home_view_logged_in_status_code(self):
        # Create a user
        User.objects.create_user(username='Antonio', password='1qaz!QAZ')
        c = Client()
        c.login(username='Antonio', password='1qaz!QAZ')
        url = reverse('home')
        response = c.get(url)
        self.assertEquals(response.status_code, 200)

    # Testing if non authenticated users receive status code of 302
    def test_home_view_no_login_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    print('TESTING HOME PAGE COMPLETE')
    '''
        END TESTING HOME PAGE
    '''



    '''
        START TESTING INBOX PAGE
    '''

    # Testing if page gets correct status code when non authenticated user try
    def test_inbox_view_no_login_status_code(self):
        url = reverse('inbox')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    # Testing if non authenticated users are redirected to login page
    def test_inbox_view_no_login_redirection(self):
        url = reverse('inbox')
        response = self.client.get(url)
        self.assertRedirects(response, '/?next=/inbox/')

    # New Tests
    def test_inbox_view_logged_in_status_code(self):
        # Create a user
        User.objects.create_user(username='Antonio', password='1qaz!QAZ')
        c = Client()
        c.login(username='Antonio', password='1qaz!QAZ')
        url = reverse('inbox')
        response = c.get(url)
        self.assertEquals(response.status_code, 200)

    print('TESTING INDEX PAGE COMPLETE')

    '''
        END TESTING INBOX PAGE
    '''

    '''
        START TESTING SCHEDULE PAGE
    '''

    # Testing if page gets correct status code when non authenticated user try
    def test_schedule_view_no_login_status_code(self):
        url = reverse('schedule_appt')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    # Testing if non authenticated users are redirected to login page
    def test_schedule_view_no_login_redirection(self):
        url = reverse('schedule_appt')
        response = self.client.get(url)
        self.assertRedirects(response, '/?next=/schedule/')

    # Testing if authenticated user can access authenticated page via status codes!
    def test_schedule_view_logged_in_status_code(self):
        # Create a user
        User.objects.create_user(username='Antonio', password='1qaz!QAZ')
        c = Client()
        c.login(username='Antonio', password='1qaz!QAZ')
        url = reverse('schedule_appt')
        response = c.get(url)
        self.assertEquals(response.status_code, 200)

    print('TESTING SCHEDULE PAGE COMPLETE')
    '''
        END TESTING SCHEDULE PAGE
    '''

    '''
        START TESTING PROVIDER PAGE
    '''

    # Testing if page gets correct status code when non authenticated user try
    def test_provider_view_no_login_status_code(self):
        url = reverse('provider')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    # Testing if non authenticated users are redirected to login page
    def test_provider_view_no_login_redirection(self):
        url = reverse('provider')
        response = self.client.get(url)
        self.assertRedirects(response, '/?next=/provider/')

    # Testing if authenticated user can access authenticated page via status codes!
    def test_provider_view_logged_in_status_code(self):
        # Create a user
        User.objects.create_user(username='Antonio', password='1qaz!QAZ')
        c = Client()
        c.login(username='Antonio', password='1qaz!QAZ')
        url = reverse('provider')
        response = c.get(url)
        self.assertEquals(response.status_code, 200)

    print('TESTING PROVIDER PAGE COMPLETE')
    '''
        END TESTING PROVIDER PAGE
    '''


    '''
        START TESTING PRESCRIPTION INFO PAGE
    '''

    def test_presc_view_no_login_redirection(self):
        url = reverse('recipes')
        response = self.client.get(url)
        self.assertRedirects(response, '/?next=/recipes/')

    def test_presc_view_no_login_status_code(self):
        url = reverse('recipes')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_presc_view_login_status_code(self):
        User.objects.create_user(username='Antonio', password='1qaz!QAZ')
        c = Client()
        c.login(username='Antonio', password='1qaz!QAZ')
        url = reverse('recipes')
        response = c.get(url)
        self.assertEquals(response.status_code, 200)

    print('TESTING PRESCRIPTION PAGE COMPLETE')

    '''
        END TESTING PRESCRIPTION INFO PAGE
    '''

    '''
        START TESTING LOGOUT CONFIRMATION PAGE
    '''
    def test_logout_conf_view_no_login_redirection(self):
        url = reverse('b4-logout')
        response = self.client.get(url)
        self.assertRedirects(response, '/?next=/lgout/')

    def test_logout_conf_view_no_login_status_code(self):
        url = reverse('b4-logout')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_logout_conf_view_login_status_code(self):
        User.objects.create_user(username='Antonio', password='1qaz!QAZ')
        c = Client()
        c.login(username='Antonio', password='1qaz!QAZ')
        url = reverse('b4-logout')
        response = c.get(url)
        self.assertEquals(response.status_code, 200)

    print('TESTING LOGOUT CONFIRMATION PAGE COMPLETE')

    '''
        END TESTING LOGOUT CONFIRMATION PAGE
    '''
