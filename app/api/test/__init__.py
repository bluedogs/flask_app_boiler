from flask_restx import Namespace, Resource, fields

api = Namespace('test', description='TEST related operations')

testserver = api.model(
    "TEST Server",
    { 
        "id": fields.String(required=True, description="Server ID"),
        "name": fields.String(required=True, description="Server Name"),
        "address": fields.String(required=True, description="Server Address")
    },
)

SERVERS = [
    {"id": "test01", "name": "test01.net.windwave.tc", "address": "10.255.5.10"},
]


@api.route("/")
class TESTServerList(Resource):
    @api.doc("list_servers")
    @api.marshal_list_with(testserver)
    def get(self):
        return SERVERS
