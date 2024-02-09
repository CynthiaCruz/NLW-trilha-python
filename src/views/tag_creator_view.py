from src.views.http_types.http_request import HttpRquest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
        responsabilidade para interagir com HTTP
    '''

    def validate_and_create(self, http_request: HttpRquest) -> HttpResponse:
        body = http_request.body
        product_code = body["product_code"]

        return HttpResponse(status_code=200, body={"hello": "word"})
