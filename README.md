# credit-scraping

## Prerequisites

```sh
uv sync
```

## Run

```sh
uv run src/main.py --year {YEAR}
```

### Get PDF

```sh
uv run src/scraping.py --year {YEAR}
```

### Extract Data

```sh
uv run src/extract.py --year {YEAR}
```

### Convert to JSON

```sh
uv run src/convert.py --year {YEAR}
```
