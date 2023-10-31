from selene import have, command
from selene.support.shared import browser

import resources
from users.users import User


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