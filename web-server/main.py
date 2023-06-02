import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1, 2, 3, 4, 5]

@app.get('/contacts', response_class=HTMLResponse)
def get_contacts():
    return """
        <h1>Hola soy una pagina</h1>
        <p>Soy un parrafo</p>
"""

def run():
    store.get_categories()

if __name__ == '__main__':
    run()