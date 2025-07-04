import os
from functools import wraps

import requests


class Router:
    __url = os.getenv('TOPICO_API_URL')
    __token = os.getenv('TOPICO_API_TOKEN')
    url = 'http://127.0.0.1:8000'

    @staticmethod
    def build_header() -> dict:
        return {
            "accept": "application/json"
        }

    @staticmethod
    def get(path: str, response_model, awaiting_status=200):
        def route_decorator(func):
            @wraps(func)
            def wrapped(**kwargs):
                formatted_path = path.format_map(kwargs)
                response = requests.get(f"{Router.url}{formatted_path}")
                if response.status_code == awaiting_status:  # 201 Created
                    return response_model.model_validate(response.json())
                else:
                    response.raise_for_status()

            return wrapped
        return route_decorator

    @staticmethod
    def post(path: str, response_model, awaiting_status=200):
        def route_decorator(func):
            @wraps(func)
            def wrapped(**kwargs):
                response = requests.post(f"{Router.url}{path}", json=kwargs, headers=Router.build_header())
                if response.status_code == awaiting_status:  # 201 Created
                    return response_model.model_validate(response.json())
                else:
                    response.raise_for_status()
            return wrapped

        return route_decorator