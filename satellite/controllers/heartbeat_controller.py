from satellite import app


@app.route('/')
def index():
    app.logger.warning('A warning occurred (%d evx)', 1)
    app.logger.error('An error occurred')
    app.logger.info('Info')
    return "satellite in orbit..."
