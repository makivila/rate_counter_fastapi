## Установка и запуск

Убедитесь в том, что у Вас установлен и запущен Docker. Также, если сервис запускается на Windows, необходимо установить make.

Далее:

```sh
git clone https://github.com/makivila/rate_counter_fastapi.git
cd rate_counter_fastapi
make build
make run

```

По умолчанию приложение запускается на 8000 порту, PostgreSQL на 5432. Это можно изменить в файле .env перед запуском.

## Использование

Загрузка тарифов:
```
POST /tariffs

Example request body:
{
  "2020-06-01": [
    {
      "cargo_type": "glass",
      "rate": 0.5
    },
    {
      "cargo_type": "other",
      "rate": 0.1
    }
  ],
  "2020-07-01": [
    {
      "cargo_type": "glass",
      "rate": 0.3
    },
    {
      "cargo_type": "other",
      "rate": 0.2
    }
  ]
}
```

Получение тарифа по объявленной стоимости, типу груза и дате:
```
GET /cost?declared_value=100&cargo_type=glass&date=2020-06-01
```


## Доступные команды
Доступ к логам:

```sh
make logs

```

Остановить сервис:

```sh
make stop

```
