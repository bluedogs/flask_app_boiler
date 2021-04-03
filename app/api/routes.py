def register_routes(api, app, root="api"):
    from api.test import register_routes as attach_test

    attach_test(api, app)
