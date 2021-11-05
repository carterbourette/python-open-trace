import logging
import functools
import opentracing
from jaeger_client import Config


def init_tracer(service):
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
        },
        service_name=service,
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()


def span(func):
    name = func.__name__

    @functools.wraps(func)
    def _span(*args, **kwargs):
        span = opentracing.tracer.start_span(name)

        with opentracing.tracer.scope_manager.activate(span, True) as scope:
            _func = func(*args, **kwargs)
            return _func

    return _span
