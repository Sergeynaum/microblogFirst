from app import app, dbfrom app.models import UserModel, PostModel

@app.shell_context_processor
def make_shell_context():
    return { 'db': db, 'UserModel': UserModel, 'PostModel': PostModel }

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)