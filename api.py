import json
import falcon

import tracer

tracer.init_tracer('service')


images = [
    {'key': '123', 'value': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'},
    {'key': '456', 'value': '/images/7f2f6ef1-1eaf-4ecc-a8d5-6e8adba7cc0e.png'},
]


@tracer.span
def get_images(req, resp, key):
    if key == '123':
        import time, random

        time.sleep(random.random())

    try:
        payload = (
            [img for img in images if img.get('key', None) == key][0] if key else images
        )
        resp.text = json.dumps(payload)
    except:
        resp.status = falcon.HTTP_404


@tracer.span
def format_response():
    import time

    time.sleep(0.1)


class Resource:
    @tracer.span
    def on_get(self, req, resp, key=None):
        get_images(req, resp, key)

        format_response()


from middleware import Middleware

app = application = falcon.App(
    middleware=Middleware(),
)

resource = Resource()
app.add_route('/', resource)
app.add_route('/{key}', resource)
