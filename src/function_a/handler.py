import __pex__  # noqa: F401 # pants: no-infer-dep
from azure.functions import HttpRequest


def handler(req: HttpRequest) -> str:
    return "Hello from A!"
