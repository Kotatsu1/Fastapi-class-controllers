from fastapi import APIRouter

class BaseController:
    def __init__(self, prefix: str):
        self.router = APIRouter(prefix=prefix)
        self._setup_routes()

    def _setup_routes(self):
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if callable(attr) and hasattr(attr, "__is_route_handler__"):
                route_method = getattr(attr, "__route_method__")
                route_path = getattr(attr, "__route_path__")
                route_dependencies = getattr(attr, "__route_dependencies__", [])
                getattr(
                    self.router, 
                    route_method.lower()
                )(route_path, dependencies=route_dependencies)(attr)

class router:
    @staticmethod
    def get(path: str, dependencies: list = []):
        def decorator(func):
            func.__is_route_handler__ = True
            func.__route_method__ = "GET"
            func.__route_path__ = path
            func.__route_dependencies__ = dependencies
            return func
        return decorator

    @staticmethod
    def post(path: str, dependencies: list = []):
        def decorator(func):
            func.__is_route_handler__ = True
            func.__route_method__ = "POST"
            func.__route_path__ = path
            func.__route_dependencies__ = dependencies
            return func
        return decorator

    @staticmethod
    def put(path: str, dependencies: list = []):
        def decorator(func):
            func.__is_route_handler__ = True
            func.__route_method__ = "PUT"
            func.__route_path__ = path
            func.__route_dependencies__ = dependencies
            return func
        return decorator

    @staticmethod
    def delete(path: str, dependencies: list = []):
        def decorator(func):
            func.__is_route_handler__ = True
            func.__route_method__ = "DELETE"
            func.__route_path__ = path
            func.__route_dependencies__ = dependencies
            return func
        return decorator
