from .views import front


def setup_routes(app):
    app.router.add_route('GET', '/', front.index)
