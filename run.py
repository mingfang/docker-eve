import json
import os

from eve import Eve
from eve_swagger import get_swagger_blueprint
from flask_swagger_ui import get_swaggerui_blueprint

app = Eve()

# Swagger

swagger = get_swagger_blueprint()
app.register_blueprint(swagger)

# Swagger UI

with open("swagger-info.json", "r") as jsonfile:
    app.config['SWAGGER_INFO'] = json.load(jsonfile)
swaggerui = get_swaggerui_blueprint(
    '/swagger',
    '/api-docs',
    config={'validatorUrl': None}
)
app.register_blueprint(swaggerui)

# main

host = '0.0.0.0'
port = int(os.environ.get('PORT', '5000'))

if __name__ == '__main__':
    app.run(host=host, port=port)
