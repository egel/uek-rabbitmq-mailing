# Wirtualizacja i przetwarzanie w chmurze

Pojekt na zajęcia z RabbitMQ

## Instalacja

RabbitMQ + plugin

    wget https://github.com/rabbitmq/rabbitmq-server/releases/download/rabbitmq_v3_5_1/rabbitmq-server_3.5.1-1_all.deb
    sudo dpkg -i rabbitmq-server_3.5.1-1_all.deb

RabbitMQ plugin:

    rabbitmq-plugins enable rabbitmq_management

Instalacja pozostałych pakietów:

> Mocno zalecane jest wykorzystanie przy tworzeniu środowiska [virtualenvwrapper'a](https://virtualenvwrapper.readthedocs.org/en/latest/), chodź nie jest to obowiązkowe.

    sudo apt-get install python python-pip
    [sudo] pip install pika mandrill flask


dla wirtualenvwrapper'a:

    sudo apt-get install python python-pip
    sudo pip install virtualenvwrapper

    mkvirtualenv uekpython27
    pip install -U pip
    pip install pika mandrill flask

> Poniższe programy odpalamy z wnętrza wirtualnego środowiska dla pythona tj.
>
>      $ workon uekpython27
>      (uekpython27) $ <your commands into vitrualenvwrapper>
>
> Wyjście z środowiska to wpisanie `deactivate`.

## Obsługa

Uruchomić: `./postOffice/index.py` oraz `./postman/postman.py`

Pod adresem [http://127.0.0.1:5000/](http://127.0.0.1:5000/) można otrzowyć prosty formularz do wysyłki e-mail.

> RabbitMQ plugini management można po instalacji otworzyć pod adresem [http://127.0.0.1:15672/](http://127.0.0.1:15672/)
>
> login: guest<br/>
> hasło: guest

