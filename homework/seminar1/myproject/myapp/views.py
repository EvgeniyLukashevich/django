from django.shortcuts import render
from django.http import HttpResponse
import logging

head_html = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Geologica:wght@100;200;300;400;500;600;700&family=Lato:wght@300;400;700;900&family=Montserrat:wght@100;200;300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0px;
            padding: 0px;
        }
        body {
            font-family: 'Geologica', sans-serif;
            font-family: 'Lato', sans-serif;
            font-family: 'Montserrat', sans-serif;
        }
        .center {
            padding-left: calc(50% - 512px);
            padding-right: calc(50% - 512px);
        }
        a {
            text-decoration: none;
        }
  </style>
    <title>Seminar1</title>
</head>
'''

header_html = '''
<header>
    <nav class="center" style="display: flex; gap: 16px">
        <a href="/">
            <h6>ГЛАВНАЯ</h6>
        </a>
        <a href="/about">
            <h6>ОБО МНЕ</h6>
        </a>
    </nav>
</header>
'''

index_html = f'''
{head_html}
<body>
    <br>{header_html}<br><br>
    <main>
        <section>
                <div class="center">
                    <h1>Framework Django</h1><br>
                    <h3>Seminar 1. Homework</h3><br>
                    <p>Главная страница приложения</p>
                    <p>Здесь могла бы быть какая-нибудь картинка</p>
                </div>
        </section>
    </main>
</body>    
'''

about_html = f'''
{head_html}
<body>
    <br>{header_html}<br><br>
    <main>
        <section>
                <div class="center">
                    <h1>Обо мне</h1><br>
                    <h3>Захватывающая история:</h3><br>
                    <p>Если параллельно углубляться в Python и в Java, в какой-то момент, 
                    <br>непроизвольно и без каких-либо причин начинает сниться Kotlin :)</p>
                </div>
        </section>
    </main>
</body>  
'''


def index(response):
    logging.info('Main page visited')
    return HttpResponse(index_html)


def about(response):
    logging.info('About page visited')
    return HttpResponse(about_html)
