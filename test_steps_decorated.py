import allure
from allure_commons.types import Severity
from selene import be, browser, by, have
from selene.support.shared.jquery_style import s


@allure.step('Открыть главную страницу GitHub')
def open_main_page():
    browser.open('https://github.com/')


@allure.step('Поиск репозитория {repo}')
def search_repo(repo):
    s('.header-search-button').click()
    s('#query-builder-test').type(repo).press_enter()


@allure.step('Перйти по ссылке в репозиторий {repo}')
def dive_into_repo(repo):
    s(by.link_text(repo)).click()


@allure.step('Перейти во вкладку issues')
def open_issues_tab():
    s('#issues-tab').click()


@allure.step('Проверить налачие задачи с номером {number}')
def check_if_issue_is_visible(number):
    s('#issues-tab').click()
    browser.all('[aria-label=Issues][role=group]').element_by(
        have.text(number)
    ).should(be.visible)


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "IvanKhokhlov")
@allure.feature("Github Issues")
@allure.story("Пользователь видит созданные Issues - decorated")
@allure.link("https://github.com", name="Testing")
def test_if_issue_is_visible(browser_settings):
    open_main_page()
    search_repo('eroshenkoam/allure-example')
    dive_into_repo('eroshenkoam/allure-example')
    open_issues_tab()
    check_if_issue_is_visible('76')
