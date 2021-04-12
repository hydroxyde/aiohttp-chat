import asyncio
import logging
import jinja2
import aiohttp_jinja2
from aiohttp import web
from aiohttp_chat.views import index
# import aioredis
from aiohttp_chat.routes import setup_routes, setup_static_routes

async def init_app():

    app = web.Application()
    setup_static_routes(app)
    setup_routes(app)
    app['websockets'] = {}

    # app['redis'] = await aioredis.create_pool(('localhost', 6379))
    app.on_shutdown.append(shutdown)

    aiohttp_jinja2.setup(
        app, loader=jinja2.PackageLoader('aiohttp_chat', 'templates'))


    return app

async def shutdown(app):
    for ws in app['websockets'].values():
        await ws.close()
    app['websockets'].clear()



def main():
    logging.basicConfig(level=logging.DEBUG)

    app = init_app()
    web.run_app(app)
    


if __name__ == '__main__':
    asyncio.run(main())