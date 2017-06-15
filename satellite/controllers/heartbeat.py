from satellite import app


@app.route('/')
def index():
    return "satellite is orbiting"
