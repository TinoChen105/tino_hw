
---

# Lookup-CLI

## Prerequisites

- Python 3.10.16
- Docker (if running in a container)

---

## Installation and Setup

### 1. Install Python Dependencies
Dependencies are listed in `requirements.txt`. Use the following command to install them:
```bash
pip install -r requirements.txt
```

---

## Usage

### 1. Query Data
Run the following command to query a specific field by name:
```bash
python3 ./lookup-cli.py <name> <output_field>
```

---

## Running in Docker

### 1. Build the Docker Image
Run the following command to build the Docker image:
```bash
docker build -t lookup-cli .
```

### 2. Test the Tool in Docker
Use the following commands to test the tool in a Docker container:
```bash
docker run lookup-cli Alice age
# Output: 18
```

---