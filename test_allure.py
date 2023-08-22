import allure
from allure import attachment_type
from allure_commons.types import Severity
from selene import be, browser, by, have
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "IvanKhokhlov")
@allure.feature("Github Issues")
@allure.story("Пользователь видит созданные Issues")
@allure.link("https://github.com", name="Testing")
def test_if_issue_is_visible(browser_settings):
    with allure.step('Открыть главную страницу GitHub'):
        browser.open('https://github.com/')

    with allure.step('Поиск репозитория'):
        s('.header-search-button').click()
        s('#query-builder-test').type('eroshenkoam/allure-example').press_enter()

    with allure.step('Перйти по ссылке в репозиторий'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Перейти во вкладку issues'):
        s('#issues-tab').click()

    with allure.step('Проверить налачие задачи с номером 76'):
        browser.all('[aria-label=Issues][role=group]').element_by(
            have.text('#76')
        ).should(be.visible)
        allure.attach.file(browser.save_screenshot(), name='last_page_screenshot', attachment_type=attachment_type.PNG)
