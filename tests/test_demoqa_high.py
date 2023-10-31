import allure
from selene import browser, have

from qa_guru import resources
#
from qa_guru.users.users import User
from qa_guru.users_data.user1_data import Vitalii_Sharov


def test_submit_student_registration_form_by_high_steps():
    student = Vitalii_Sharov
    registration_page = RegistrationPage()
    with allure.step('Open registrations form'):
        registration_page.open_form()
    with allure.step('Fill form'):
        registration_page.submit_form(student)
    with allure.step("Check form results"):
        registration_page.should_have_registrated_user(student)




class RegistrationPage:
    def open_form(self):
        browser.open('/automation-practice-form')
        return self

    def submit_form(self, user: User):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.all('[name=gender]').element_by(have.value(user.gender)).element('..').click()
        browser.element('#userNumber').type(user.number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(user.date_of_birth.year)
        browser.element('.react-datepicker__month-select').type(user.date_of_birth.strftime('%B'))
        browser.element(f'.react-datepicker__day--0{user.date_of_birth.day}').click()
        browser.element('#subjectsInput').type(user.subject).press_enter()
        browser.all('.custom-checkbox').element_by(have.exact_text(user.hobbies)).click()
        browser.element('#uploadPicture').send_keys(resources.path(user.picture))
        browser.element('#currentAddress').type(user.current_address)
        browser.element('#react-select-3-input').type(user.state).press_enter()
        browser.element('#react-select-4-input').type(user.city).press_enter().press_enter()

    def should_have_registrated_user(self, user: User):
        user.date_of_birth = f'{user.date_of_birth.day} {user.date_of_birth.strftime("%B")},{user.date_of_birth.year}'
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender,
                user.number,
                user.date_of_birth,
                user.subject,
                user.hobbies,
                user.picture,
                user.current_address,
                f'{user.state} {user.city}',
            )
        )