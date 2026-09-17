# API Testing: Swagger Petstore

## Цель

Проверка REST API Swagger Petstore с использованием Postman.

## Проверяемые операции

- создание животного;
- получение животного по ID;
- обновление животного;
- удаление животного;
- обработка несуществующего ID.

## Инструменты

- Postman
- REST API
- JSON
- JavaScript tests
- Swagger/OpenAPI

## Проверки

- HTTP status codes
- response body
- required fields
- data types
- positive scenarios
- negative scenarios

## Основной сценарий

1. Создать животное.
2. Получить животное по ID.
3. Проверить имя и статус.
4. Удалить животное.
5. Убедиться, что животное больше не находится.

## Результат

- Количество запросов: 7
- Успешно: 7
- Ошибки: 0