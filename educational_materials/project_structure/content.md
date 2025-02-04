# Структура проекта

## Мотивация

Структура проекта очень важна - от того как вы называете и размещаете код, документацию и другие 
важные для проекта файлы будет зависеть скорость с которой другие разразработкики смогут воспользоваться
вашим проектом. В другую сторону это так же работает, чем более стандартно устроен проект, тем 
быстрее вы сможете воспользоваться им. Будем хорошими разработчиками и сделаем наш проект понятным.

## Проект 

Давайте реализуем проект, который будет конвертировать одни единыцы в другие. В нем будут как 
стандартные единицы, так и более интересные - чтобы измерять удавов в попугаях. Наш проект будет
содержать две части саму библиотеку и приложение, которое позволит пользоваться функциями 
библиотеки онлайн. Это достаточно распространненая связка - и она удобна для пользователей
так как не требует установки всего что нужно для запуска в том числе самого языка программирования.
Для разработчика это может быть так же удобно так как можно собирать логи централизовано и 
обесбечивать быстрые обновления.

```
fancy-convert/
│
├── fancy-convert/              # Библиотека которая может быть использована отдельно
│   ├── fancy_convert/          # Исходный код (так же могут быть варианты с src/fancy_convert)
│   │   ├── __init__.py         # Всегда добавляет это чтобы Python  считал папку пакетом
│   │   ├── converters.py       # Функции для конвертирования
│   │   ├── utils.py            # Вспомогательные функции
|   ├── docs/                   # Документация по коду API (не путать с REST API) библиотеки 
│   ├── tests/                  # Тесты (обычно unit-тесты) для проверки корректности работы функций
│   ├── notebooks/              # Тетрадки с примерами использования библиотеки
│   ├── pyproject.toml          # Вся информация по зависимостям, установке и сборке c помощью poetry
                                # Альтернатива requirements.txt + setup.py
│   ├── README.md               # README к библотеки
│   ├── LICENSE                 # Лицензия (обычно open-source) для библиотеки
│
├── fancy-convert-api/          # Приложение на FastAPI
│   ├── app/                    # Исходный код приложения
│   │   ├── __init__.py         # Уже обсуждали
│   │   ├── main.py             # Точка входа для приложения (обычно всегда main.py)
│   │   ├── routes.py           # Модуль в котором собраны все "ручки" (endpoints)
│   │   ├── dependencies.py     # Dependency injection & configuration
│   │   ├── cli.py              # CLI client for the application
│   ├── tests/                  # Application-specific tests
│   ├── .env.example            # Example environment variables file
│   ├── pyproject.toml          # Poetry dependencies for the application
│   ├── LICENSE                 # Лицензия (обычно open-source) для приложения
│   ├── README.md               # API documentation
│
├── scripts/                    # Deployment and startup scripts
│   ├── install.sh              # Install library and application
│   ├── run_local.sh            # Start application locally
│   ├── build_docker.sh         # Build Docker container
│   ├── run_docker.sh           # Run application in Docker
│
├── docker-compose.yml          # Docker Compose for containerized deployment
├── .gitignore                  # Ignore unnecessary files
├── LICENSE                     # Root license file
├── README.md                   # High-level project documentation
```


Чтобы воспроизвести структуру Вы можете воспользоваться скриптом на bash сохраните его в файл 
`make_structure.sh` и дайте разрешение на запуск `chmod +x make_structure.sh`

```bash
#!/bin/bash

# Define project name
PROJECT_NAME="fancy-convert"

# Define directories
DIRECTORIES=(
    "$PROJECT_NAME/$PROJECT_NAME/fancy_convert"
    "$PROJECT_NAME/$PROJECT_NAME/tests"
    "$PROJECT_NAME/$PROJECT_NAME/use_cases"
    "$PROJECT_NAME/$PROJECT_NAME-api/app"
    "$PROJECT_NAME/$PROJECT_NAME-api/tests"
    "$PROJECT_NAME/scripts"
)

# Define files
FILES=(
    "$PROJECT_NAME/$PROJECT_NAME/fancy_convert/__init__.py"
    "$PROJECT_NAME/$PROJECT_NAME/fancy_convert/converters.py"
    "$PROJECT_NAME/$PROJECT_NAME/fancy_convert/utils.py"
    "$PROJECT_NAME/$PROJECT_NAME/fancy_convert/config.py"
    "$PROJECT_NAME/$PROJECT_NAME/tests/__init__.py"
    "$PROJECT_NAME/$PROJECT_NAME/pyproject.toml"
    "$PROJECT_NAME/$PROJECT_NAME/README.md"
    "$PROJECT_NAME/$PROJECT_NAME/LICENSE"

    "$PROJECT_NAME/$PROJECT_NAME-api/app/__init__.py"
    "$PROJECT_NAME/$PROJECT_NAME-api/app/main.py"
    "$PROJECT_NAME/$PROJECT_NAME-api/app/routes.py"
    "$PROJECT_NAME/$PROJECT_NAME-api/app/dependencies.py"
    "$PROJECT_NAME/$PROJECT_NAME-api/app/cli.py"
    "$PROJECT_NAME/$PROJECT_NAME-api/tests/__init__.py"
    "$PROJECT_NAME/$PROJECT_NAME-api/.env.example"
    "$PROJECT_NAME/$PROJECT_NAME-api/pyproject.toml"
    "$PROJECT_NAME/$PROJECT_NAME-api/README.md"

    "$PROJECT_NAME/scripts/install.sh"
    "$PROJECT_NAME/scripts/run_local.sh"
    "$PROJECT_NAME/scripts/build_docker.sh"
    "$PROJECT_NAME/scripts/run_docker.sh"

    "$PROJECT_NAME/docker-compose.yml"
    "$PROJECT_NAME/.gitignore"
    "$PROJECT_NAME/LICENSE"
    "$PROJECT_NAME/README.md"
)

# Create directories
echo "Creating project directories..."
for dir in "${DIRECTORIES[@]}"; do
    mkdir -p "$dir"
done

# Create files
echo "Creating project files..."
for file in "${FILES[@]}"; do
    touch "$file"
done

# Add execute permissions to scripts
chmod +x "$PROJECT_NAME/scripts/"*.sh

echo "Project structure created successfully!"
```

Дальше посмотрим на каждый файл и пупку по отдельности и посмотрим ее назначение.

## .gitignore

Это обычно первый файл, который мы добавляем в проект. Так мы уменьшаем вероятность того, что 
не нужные файлы случайно попадут в репозиторий. Вероятность по-прежнему существует - названия 
папок которые мы разместим в проекте могут быть любые, например IN и OUT для входных и выходных
данных программы. Существует множество сервисов, например  [этот](https://www.toptal.com/developers/gitignore), 
которые позволят Вам создавать начальные файлы `.gitignore`, которые вы можете расширять для 
своего проекта. 

## README.md README.rst

Следующий файл, который мы создаем это файл README.md так же можно встретить README.rst. Отличие в 
языке разметки - [MarkDown](https://github.com/kruzhok-team/fossdev/blob/devel/educational_materials/docs/content.md#markdown) 
и ReStructuredText - [RestructuredText](https://docutils.sourceforge.io/docs/user/rst/quickref.html). 

[Пример README](sample_readme.md)

Единственный способ начать писать хорошее README - это начать писать README. На GitHub есть хорошие 
подборки проектов, где оформлены [README.md](https://github.com/matiassingers/awesome-readme) можете 
обращаться к этой подборке, когда пишите свой README. 


## pyproject.toml

Этот файл содержит всю информацию необходимую информацию для установки зависимостей для проекта и 
установке самого проекта. Он может существовать и по отдельности, но мы будем использовать его 
вместе с [poetry](https://python-poetry.org/). Это почти всегда хорошая замена для pip и setup.py.
Мы рассмотрим более классческие способы управления зависимостями, установки и сборки в пакет далее
по курсу чтобы у вас был инструментарий для работы когда poetry не применим. Но на текущий момент 
будем использовать poetry. 
