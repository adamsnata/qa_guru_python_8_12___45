import allure

from tests.registration_page import RegistrationPage
from users_data.user1_data import Vitalii_Sharov


def test_submit_student_registration_form_by_high_steps():
    student = Vitalii_Sharov
    registration_page = RegistrationPage()
    with allure.step('Open registrations form'):
        registration_page.open_form()
    with allure.step('Fill form'):
        registration_page.submit_form(student)
    with allure.step("Check form results"):
        registration_page.should_have_registrated_user(student)

