from django.test import TestCase

from newspaper.forms import RedactorCreationForm


class RedactorFormsTest(TestCase):
    def test_cook_creation_form_with_years_of_experience_first_last_name(self):
        form_data = {
            "username": "new_user",
            "password1": "user123test",
            "password2": "user123test",
            "first_name": "Test first",
            "last_name": "Test last",
            "years_of_experience": 1,
        }
        form = RedactorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
