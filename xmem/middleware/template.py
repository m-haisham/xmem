from ..template import BaseTemplate


class Middleware(BaseTemplate):
    def __init__(self, template: BaseTemplate):
        self.template = template
