🌱 Enfoque Ambiental - Blog de Noticias  
Este es un blog de noticias dedicado a temas ambientales, creado con **Django**. El proyecto busca informar y crear conciencia sobre la situación del medio ambiente.

**INFORMATORIO - 1° COHORTE 2024 - ETAPA 2 | COMISIÓN 5 - GRUPO 5:
INTEGRANTES:**

* Maldonado, Tania Elizabeth

* Misiaszek, Lucía

* Servin, Cecilia Beatriz

Profesor: Frias, Daniel

Mentor: Alves, Ramiro 

---

**Índice**  
- [Descripción](#Descripción)  
- [Funcionalidades](#Funcionalidades)
- [Diseño de interfaz](#Diseño-de-interfaz) 
- [Instalación](#Instalación)  
- [Uso](#Uso)  
- [Capturas de Pantalla](#Capturas-de-Pantalla)  
- [Tecnologías](#Tecnologías)  
- [Requisitos](#Contacto)   
- [Contacto](#Contacto)  

---

**Descripción**  
El blog permite que los usuarios lean, publiquen y comenten sobre noticias ambientales. Además, los usuarios autenticados con permisos de **staff** pueden crear, modificar y eliminar publicaciones.  

---

**Funcionalidades**  
- Registro e inicio de sesión de usuarios. 
- Roles de usuario: Administrador, Colaborador y Visitante.  
- Creación, edición y eliminación de publicaciones para usuarios con permisos de staff  
- Sistema de comentarios en las publicaciones.
- Interfaz utilizando HTML, CSS y JavaScript.
- Mappeo de URLs para la navegación interna.
- Integración con redes sociales y links a ONG ambientales

---

**Diseño de interfaz**
- [Figma](https://www.figma.com/design/819LLnvTPwKZ2cNNGIPrxf/Blog---TP-Final-Info?node-id=0-1&t=5xZc3NF7Czvc9LUv-1)

---

**Instalación**  
Sigue estos pasos para instalar y ejecutar el proyecto en tu máquina local:

1. **Clonar el repositorio:**
   ```bash
   git clone <URL-del-repositorio>
   cd <nombre-del-repositorio>
   ```

2. **Crear y activar un entorno virtual:**
   ```bash
   python -m venv entorno
   cd <nombre del directorio>/entorno/Scripts/activate 
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplicar migraciones:**
   ```bash
   python manage.py migrate
   ```

5. **Ejecutar el servidor:**
   ```bash
   python manage.py runserver
   ```

---

**Uso**  
1. Accede a `https://enfoque2024.pythonanywhere.com/` en tu navegador.  
2. Regístrate e inicia sesión para agregar comentarios.  
3. Los administradores o usuarios con permisos de staff podrán gestionar las publicaciones.  

---

**Capturas de la interfaz**  
- ![Página principal](/blog/media/media/home.png)
- ![Noticia individual](/blog/media/media/noticiaindividual.png)
- ![Inicio de sesión](/blog/media/media/login.png)
- ![Registro](/blog/media/media/registro.png)
- ![Contacto](/blog/media/media/contacto.png)


**¿Querés ver un poco más?** - [Te dejamos un video!](https://youtu.be/B8uVgEKQK7I?feature=shared)

---

**Tecnologías**  
- **Django (Backend)** 
- **Python (Lógica del servidor)** 
- **HTML/CSS/JavaScript (Frontend)** 
- **SQLite (Base de datos)** 
- **PythonAnywhere** 
- **Control de versiones:** Git
- **Figma (Diseño de interfaz)**

---

**Requisitos**  
- **asgiref==3.8.1** 
- **Python 3.12.4** 
- **Django 5.1.1** 
- **pillow==10.4.0** 
- **sqlparse==0.5.1**
- **tzdata==2024.1**

---

**Contacto**  
Cualquier duda o sugerencia, contáctanos en:  
📧 Email: contacto@enfoqueambiental.com  

---
