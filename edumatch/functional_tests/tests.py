from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time 
import unittest
from edu.models import Tutor 

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_match_for_one_user(self):
        
        #set up database 
        first_tutor = Tutor()
        first_tutor.name = 'Mark'
        first_tutor.save()

        second_tutor = Tutor()
        second_tutor.name = 'Ploy'
        second_tutor.save()

        #Mark is a student at some university. 
        #He feel very stressed about upcomming midterm exam.
        #His friend suggest a tutor-finder online app. So he goes
        # to check out its homepage.
         
        self.browser.get(self.live_server_url)

        #He notices the page title and header mention edumatch
        self.assertIn('edumatch',self.browser.title)

        #He see textbox with "Subject".So he enter subject that he
        #want to learn straight away.
        #He types "Signal and System" into a text box
        inputbox = self.browser.find_element_by_id('user_select_subject')  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your "Subject" that you need help!!!'
        )


        #After that he could see a list of tutor user that agree
        #to teach with that subject that he enter.
        table = self.browser.find_element_by_id('user_list_table')
        rows = table.find_elements_by_tag_name('td')
        self.assertTrue(
            any(row.text == 'Tutor: Ploy' for row in rows),
           f"Tutor: Ploy did not appear in table. Content were: \n{table.text}"
        )
        time.sleep(1)
        #He select ploy to be his tutor.
        #He click on a ploy's match button.

        button = table.find_element_by_name('Ploy')
        button.send_keys(Keys.ENTER)
    
        #The page will show that tutor ploy is match for him.
        result = self.browser.find_element_by_id('match_result')
        self.assertEqual(result.text,'match!!!')
        
        self.fail('finist the test !!')
        

       
