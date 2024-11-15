# credit-scraping

## Prerequisites

```sh
uv sync
```

## Run

```sh
uv run src/main.py {YEAR}
```

### Get PDF

```sh
uv run src/scraping.py {YEAR}
```

### Extract Data

```sh
uv run src/extract.py {YEAR}
```

### Convert to JSON

```sh
uv run src/convert.py {YEAR}
```
