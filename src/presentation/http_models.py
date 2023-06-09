from typing import Dict

class HttpRequest:
    """Class to HttpRequest representation"""
    def __init__(
            self,
            header: Dict = None,
            body: Dict = None,
            query: Dict = None,
            form: Dict = None,
            files: Dict = None
        ):
        self.header = header
        self.body = body
        self.query = query
        self.form = form
        self.files = files

    def __repr__(self) -> str:
        return f"HttpRequest (header={self.header}, body={self.body}, query={self.query})"


class HttpResponse:
    """Class to HttpResponse representation"""

    def __init__(self, status_code: int, body: any):
        self.status_code = status_code
        self.body = body

    def __repr__(self) -> str:
        return f"HttpResponse (status_code={self.status_code}, body={self.body})"
