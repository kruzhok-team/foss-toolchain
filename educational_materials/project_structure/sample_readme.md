# FancyConvert

FancyConvert is a lightweight unit conversion library (`fancy-convert`) and a 
REST API (`fancy-convert-api`) that provides unit conversions without local installation.

## Features

- Convert various measureable types (length, weight, temperature, time etc.).
- Standard and Fancy units (meters, inches, whales, parrots etc)
- Standalone library (`fancy-convert`) in any Python project.
- Application based on FastAPI (`fancy-convert-api`).
- CLI client for interactions with API.
- Deployable as a Docker container or locally with Bash scripts.
- Environment variables for configuration (no hardcoded values).

## Installation

### 1. Install the `fancy-convert` Library

```bash
cd fancy-convert
poetry install
```

### 2. Install the `fancy-convert-api` Application

```bash
cd fancy-convert-api
poetry install
```

## Usage

### Library (Python)

```python
from fancy_convert import convert_length

result = convert_length(100, "meters", "kilometers")
print(result)  # Output: 0.1
```

### Run apllication (API)

Run Locally (develop):

```bash
cd fancy-convert-api
uvicorn app.main:app --reload
```

or

```bash
./scripts/run_local.sh
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

Run for production:

```bash
cd fancy-convert-api
uvicorn app.main:app --host 0.0.0.0 --nworkers 4
```

### CLI

CLI client allows connection to API via command line interface. 


## Environment Variables

The application uses environment variables for configuration. Copy `.env.example` to `.env` and update the values.

```bash
cp fancy-convert-api/.env.example fancy-convert-api/.env
```

## Testing

### Library Tests
```bash
cd fancy-convert
pytest
```

### API Tests
```bash
cd fancy-convert-api
pytest
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

1. Fork the repository.
2. Create a new branch (`feature-name`).
3. Commit your changes.
4. Push to your branch and create a Pull Request.

