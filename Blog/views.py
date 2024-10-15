from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(
        """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style> 
        body {
            background-color: blueviolet;
            color: white;
            }
    </style>
    <title>Document</title>
</head>
<body>
<h1> NOTICIAS NOTICIAS  </h1/>
<p>Esto es párrafo </p>
<ul>
    <li>1.  </li>
    <li>2.  </li>
    <li>3.  </li>
    <li>4.  </li>

</ul>
</body>

</html>
                         """
    )

