import allure
from data import URLs, ORDER_INFO
import json
import requests


class OrderMethods:

    @allure.step('Инизиализация предварительно подготовленных данных по заказу в виде словаря.')
    def __init__(self):
        self.order_data = ORDER_INFO
        self.user_access_token = ''

    @allure.step('Выполнение POST-запроса для создания закза.')
    def post_create_order(self):
        headers = {"Content-type": "application/json"}
        if self.user_access_token:
            headers["Authorization"] = self.user_access_token

        response = requests.post(URLs.ORDERS_URL, data=json.dumps(self.order_data), headers=headers)
        return response

    @allure.step('Последовательное выполнение POST-запросов для создания закзов в количестве N штук.')
    def create_n_orders(self, n):
        for i in range(n):
            self.post_create_order()

