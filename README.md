Here's a clean and professional `README.md` documentation for your **repo content generator** project:

---

# Repo Content Generator

This Python utility generates a readable summary of the source code files within a given project directory. It supports custom include/exclude patterns via a YAML or JSON configuration file, making it ideal for documenting repositories, preparing technical reviews, or creating educational materials.

---

## Features

* ✅ Traverse a project directory recursively
* ✅ Include or exclude files based on glob patterns
* ✅ Outputs formatted code blocks per file
* ✅ Cleans outdated generated files from the output directory
* ✅ Supports YAML or JSON config formats

---

## Installation

To run this script, ensure you have Python 3.6+ installed. Clone the repository and install the required packages:

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
python repo_content_generator.py \
  --project path/to/your/project \
  --config path/to/config.yaml \
  --output output/summary.txt
```

### Arguments

| Flag            | Description                                                          | Required |
| --------------- | -------------------------------------------------------------------- | -------- |
| `--project, -p` | Root path of the target repository                                   | ✅        |
| `--config, -c`  | Path to YAML or JSON config file (include/exclude)                   | ✅        |
| `--output, -o`  | Output file path (defaults to `output/repo_content_<timestamp>.txt`) | ❌        |

---

## Configuration File

You must supply a config file (YAML or JSON) with the desired `include` and `exclude` patterns using Unix shell-style wildcards.

### Example: `example.config.yaml`

```yaml
include:
  - "*.py"

exclude:
  - "dist/*"
  - ".git/*"
  - "build/*"
  - "venv/*"
```

* **`include`**: Files to include (if omitted, includes everything unless excluded)
* **`exclude`**: Files to exclude (if omitted, includes all that match the include patterns)

---

## Output

The output is a text file containing sections like:

```
Files: src/main.py

<SOURCE CODE BLOCK>
```

Each included file is wrapped in a Markdown-style code block for easy rendering and readability.

---

## Output Directory Cleanup

Generated files older than **1 day** in the `output/` folder (except `.gitignore`) are automatically deleted before each run.

---

## Example

```bash
python repo_content_generator.py \
  --project ./my-python-app \
  --config ./example.config.yaml
```

Sample output path:

```
output/repo_content_1720173312.txt
```

---