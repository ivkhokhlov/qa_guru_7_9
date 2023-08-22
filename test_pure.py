import allure
from allure_commons.types import Severity
from selene import be, browser, by, have
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "IvanKhokhlov")
@allure.feature("Github Issues")
@allure.story("Пользователь видит созданные Issues - pure selene")
@allure.link("https://github.com", name="Testing")
def test_if_issue_is_visible(browser_settings):
    browser.open('https://github.com/')
    s('.header-search-button').click()
    s('#query-builder-test').type('eroshenkoam/allure-example').press_enter()
    s(by.link_text('eroshenkoam/allure-example')).click()
    s('#issues-tab').click()
    browser.all('[aria-label=Issues][role=group]').element_by(
        have.text('#76')
    ).should(be.visible)
