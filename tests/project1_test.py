from project1 import project1_main
import pytest

# Test redact phone numbers
def test_redact_phones():
   str = "My phone number is 405111-2222"
   _,_,phone,_,_=project1_main.redact_names_phones_emails_genders(str)
   assert phone==1

# Test redact emails
def test_redact_email():
   str = "My email is jalal.saidi@ou.edu. Please email me at my work email jalal@google.com"
   _,_,_,email,_,=project1_main.redact_names_phones_emails_genders(str)
   assert email==2




test_redact_phones()
test_redact_email
