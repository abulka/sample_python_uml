class RequestCheck:

    async def __call__(self, request, name):
        data = await as_coroutine(request.body_data())
        assert(data['method'] == name)
        return True


def server(callable=None, **params):
    return wsgi.WSGIServer(Site(), **params)
