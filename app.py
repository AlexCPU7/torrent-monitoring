from aiohttp import web


async def create_app():
    app = web.Application()
    # aiohttp_jinja2.setup(
    #     app,
    #     loader=jinja2.PackageLoader('demo', 'templates')
    # )
    # setup_routes(app)
    return app
