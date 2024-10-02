from selene import browser, be, have

def test_no_google_results(browser_settings):
    text = 'Sadasdsdsd222&&&'
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type(text).press_enter()
    browser.element('.card-section').should(have.text(f"На запрос {text} в поиске ничего не найдено"))