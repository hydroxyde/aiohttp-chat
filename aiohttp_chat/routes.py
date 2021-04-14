from aiohttp_chat.views import index

def setup_routes(app):
    app.router.add_get('/', index)

def setup_static_routes(app):

    # add_static should be used only for development,
    # in production: process static content with web servers (nginx, apache, etc..)

    app.router.add_static('/static/',
                          path=str('./aiohttp_chat/static/'),
                          name='static')    