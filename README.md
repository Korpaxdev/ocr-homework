# Варианты запуска проекта:

- С помощью `docker-compose`. Нужно будет выкачать как минимум 4ГБ (ВМ + библиотеки CUDA). Автоматически установит все
  зависимости:
    - Команда - `docker-compose up -d`. По умолчанию проект доступен на порту `8501`
- Вручную:
    - Устанавливаем зависимости с помощью `pip install -r requirements.txt`. Установка около 1ГБ (библиотеки CUDA)
    - Осуществляем запуск скрипта с помощью команды `streamlit run main.py`

### Обратите внимание

- В режиме GPU может не хватит памяти для обработки изображения, в случае ошибки переключите режим работы в CPU
