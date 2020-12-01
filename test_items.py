def test_items(browser):

    button = browser.find_elements_by_class_name("btn-add-to-basket")
    assert button, "Кнопка ДОБАВИТЬ В КОРЗИНУ не найдена"




