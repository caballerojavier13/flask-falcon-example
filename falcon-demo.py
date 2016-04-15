# sample.py
import falcon
import json

class JSONTranslator(object):
    def process_request(self, req, resp):
        if req.content_length in (None, 0):
            return

        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body',
                                        'A valid JSON document is required.')

        try:
            req.context['doc'] = json.loads(body.decode('utf-8'))

        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(falcon.HTTP_753,
                                   'Malformed JSON',
                                   'Could not decode the request body. The '
                                   'JSON was incorrect or not encoded as '
                                   'UTF-8.')

    def process_response(self, req, resp, resource):
        if 'result' not in req.context:
            return

        resp.body = json.dumps(req.context['result'])


class JSONInfoResource:
    def on_post(self, req, resp):
        data = req.context['doc']
        data['keys'] = [key for key in data]

        req.context['result'] = data

    def on_get(self, req, resp):
        resp.body = "POST a JSON body to get it's keys"
 
api = falcon.API(middleware=[JSONTranslator()])
api.add_route('/', JSONInfoResource())
