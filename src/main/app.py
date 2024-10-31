from flask import Flask
from opencensus.ext.azure.log_exporter import AzureLogHandler
import logging

app = Flask(__name__)

# Configure Application Insights
logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(connection_string='InstrumentationKey=<Your_Instrumentation_Key>'))

@app.route('/')
def hello():
    logger.info('Hello, IoT World!')
    return 'Hello, IoT World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)