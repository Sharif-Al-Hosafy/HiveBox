# HiveBox

A containerized Python application built following the [Dynamic DevOps Roadmap](https://devopsroadmap.io/projects/hivebox/).

The app reads its version from a local `version.txt` file and prints it. A missing version file fails loudly with an error on `stderr` and a non-zero exit code.

<p align="center">
  <img src="https://devopsroadmap.io/img/hivebox-architecture.gif" width="60%" />
</p>

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed
- (Optional) Python 3 to run the script directly for testing

## Build

```bash
docker build -t hivebox:v0.0.1 .
```

## Run

```bash
docker run --rm hivebox:v0.0.1
```

Expected output:

```
v0.0.1
```

## Testing

### Success case

```bash
docker run --rm hivebox:v0.0.1
```

The container should print `v0.0.1` and exit with code `0`.

### Failure case (missing `version.txt`)

Run the script directly with the version file temporarily renamed:

```bash
mv version.txt version.txt.bk
python3 app.py; echo "Exit: $?"
mv version.txt.bk version.txt
```

Expected behaviour:
- `version.txt file doesn't exist` printed to **stderr**
- Exit code: `1`
