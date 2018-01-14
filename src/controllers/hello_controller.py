from src import app


@app.route('/local/hello/', methods=['GET'])
def test():
    return 'Hello'
