from app import app


@app.get('/')
def test():
    return {"message": "Testeando mi app"}