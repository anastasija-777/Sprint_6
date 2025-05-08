from locators.order_page_for_whom_locator import OrderPageForWhomLocators
from locators.order_page_rental_locator import OrderPageRentalLocators

class URL:
    basa_url = 'https://qa-scooter.praktikum-services.ru/'
    order_url = basa_url+'order'
    dzen_url = 'https://dzen.ru/'



class Data:
    expected_answer_0 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    expected_answer_1 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    expected_answer_2 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    expected_answer_3 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    expected_answer_4 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    expected_answer_5 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    expected_answer_6 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    expected_answer_7 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    data_set_for_whom_1 = {
        "surname": "Иванова",
        "address": "г. Москва, ул. Малая Бронная, д. 44",
        "metro_station": OrderPageForWhomLocators.STATION_LUBYANKA_LOCATOR,
        "phone_number": "89277777777",
    }
    data_set_for_whom_2 = {
        "name": "Ив",
        "surname": "Иванов",
        "address": "г. Москва",
        "metro_station": OrderPageForWhomLocators.STATION_SOKOLNIKI_LOCATOR,
        "phone_number": "+79277777777",
    }

    data_set_rental_1 = {
        "rental_data": OrderPageRentalLocators.DATE_FIVE_LOCATOR,
        "rental_period": OrderPageRentalLocators.RENTAL_PERIOD_SEVEN_LOCATOR,
        "color": OrderPageRentalLocators.COLOR_SCOOTER_GREY_LOCATOR,
        "metro_station": OrderPageForWhomLocators.STATION_SOKOLNIKI_LOCATOR,
        "comment": "Позвонить"
    }

    data_set_rental_2 = {
        "rental_data": OrderPageRentalLocators.DATE_FIVE_LOCATOR,
        "rental_period": OrderPageRentalLocators.RENTAL_PERIOD_SEVEN_LOCATOR,
        "color": OrderPageRentalLocators.COLOR_SCOOTER_GREY_LOCATOR,
        "metro_station": OrderPageForWhomLocators.STATION_SOKOLNIKI_LOCATOR,
        "comment": "Позвонить"
    }