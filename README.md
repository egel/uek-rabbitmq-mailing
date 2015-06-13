# Wirtualizacja i przetwarzanie w chmurze

Prowadzący: [Jakub Kanclerz](https://github.com/jkanclerz)


## Instalacja

RabbitMQ + plugin

    wget https://github.com/rabbitmq/rabbitmq-server/releases/download/rabbitmq_v3_5_1/rabbitmq-server_3.5.1-1_all.deb
    sudo dpkg -i rabbitmq-server_3.5.1-1_all.deb

RabbitMQ plugin:

    rabbitmq-plugins enable rabbitmq_management

Instalacja pozostałych pakietów:

> Mocno zalecane jest wykorzystanie przy tworzeniu środowiska [wirtualenvwrapper'a](https://virtualenvwrapper.readthedocs.org/en/latest/), chodź nie jest to obowiązkowe.

    sudo apt-get install python python-pip
    [sudo] pip install pika mandrill flask



## Obsługa

Uruchomić: `./postOffice/index.py` oraz `./postman/postman.py`

Pod adresem [http://127.0.0.1:5000/](http://127.0.0.1:5000/) można otrzowyć prosty formularz do wysyłki e-mail.

> RabbitMQ plugini management można po instalacji otworzyć pod adresem [http://127.0.0.1:15672/](http://127.0.0.1:15672/)
>
> login: guest<br/>
> hasło: guest
