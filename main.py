from flask import Flask, send_file
import random
import os

app = Flask(__name__)
facts_list = ["Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, de modo que pasemos el mayor tiempo posible viendo contenidos.", 
            "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.", 
            "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas.", 
            "El estudio de la adicción tecnológica es una de las áreas más relevantes de la investigación científica moderna."]

lanzamiento = ["Cara", "Sello"]
@app.route("/")
def index():
    return """
    <h1>Hola, en esta página puedes aprender un par de cosas interesantes sobre las dependecias tecnológicas.</h1>
    <h1>Dependencia tecnológica</h1>
    <p>Es un tipo de adicción en la que una persona no puede prescindir del uso de determinadas tecnologías y dispositivos. Esta adicción puede llevar a que uno pierda por completo la capacidad de funcionar sin estas tecnologías, lo que puede tener un grave impacto negativo en su calidad de vida.</p>

    <h2>¿Considera que se trata de un problema grave?</h2>

    <ul>
        <li>Redes sociales y mensajeros: Las personas pueden pasar demasiado tiempo en las redes sociales y los mensajeros, reduciendo el tiempo que pasan en el mundo real. Además, esto les lleva a depender de actualizaciones constantes de noticias y mensajes.</li>
        <li>Teléfonos inteligentes y tabletas: Los teléfonos inteligentes y las tabletas pueden convertirse en la principal forma de comunicarse con el mundo, y la gente puede volverse dependiente de comprobar constantemente las notificaciones, retuitear y navegar por las redes sociales y los mensajeros.</li>
        <li>Juegos y entretenimiento en línea: Los juegos y el ocio en línea pueden crear adicción y llevar a la gente a pasar demasiado tiempo en el mundo virtual en lugar de en la vida real.</li>
    </ul>

    <h2>¿Cómo combatir la dependencia tecnológica?</h2>

    <ul>
        <li>Establecer límites sobre el tiempo que pasas en línea/en tus dispositivos.</li>
        <li>Diversificar intereses y actividades más allá del uso de la tecnología.</li>
        <li>Buscar nuevas formas de conectar con el mundo que te rodea para reducir tu dependencia de las redes sociales y la mensajería.</li>
    </ul>

    <p>No tengas miedo de la tecnología, pero no olvides que debe ser una herramienta para mejorar tu vida y tu trabajo. La tecnología no debe sustituir tu vida.</p>
    
    <a href="/random_fact">¡Ver un hecho al azar!</a>
    <a href="/lanzamiento_moneda">¡Cara o sello!</a>
    <a href="/generar_password">¡Contraseña aleatoria!</a>
    <a href="/mostrar_imagen">¡Imagen aleatoria!</a>
    """

@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/lanzamiento_moneda")
def moneda():
    return f'<p>{random.choice(lanzamiento)}</p>'

@app.route("/generar_password")
def generador():
    password = random.randint(1000,10000)
    return f'<p>{password}</p>'

@app.route("/mostrar_imagen")
def imagen():
    img_name = random.choice(os.listdir('imagenes'))
    return send_file(f"imagenes/{img_name}",mimetype="image/jpeg")

app.run(debug=True)
