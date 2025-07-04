-----

# Repository Content Generator

This project provides a Python script, `repo_content_generator.py`, designed to summarize the content of a given repository. It allows for flexible inclusion and exclusion of files based on patterns defined in YAML or JSON configuration files, making it ideal for generating documentation, code summaries, or project overviews.

-----

## Features

  * **Configurable File Filtering**: Easily specify which files and directories to include or exclude using glob-style patterns in configuration files.
  * **Multiple Configuration Formats**: Supports both YAML and JSON for defining include/exclude patterns.
  * **Directory Traversal**: Recursively scans through the specified project directory to find relevant files.
  * **Output Options**: Prints the generated content to the console or saves it to a specified output file.

-----

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You need **Python 3.6+** installed on your system.

### Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```
2.  **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

-----

## Usage

The `repo_content_generator.py` script can be run from the command line with several arguments.

```bash
python repo_content_generator.py --project <root_project_directory> --config <config_file> [--output <output_file>]
```

### Arguments

  * `-p`, `--project`: **(Required)** The root directory of the project you want to summarize.
  * `-c`, `--config`: **(Required)** The path to a YAML or JSON configuration file that defines the include and exclude patterns.
  * `-o`, `--output`: **(Optional)** The name of the file where the generated content will be saved. If not provided, the output will be printed to the console. The default output filename is `output/repo_content_<timestamp>.txt`.

### Configuration Files

The project uses configuration files (either YAML or JSON) to determine which files to include and exclude from the summary.

  * **`include`**: A list of glob-style patterns for files and directories to include.
  * **`exclude`**: A list of glob-style patterns for files and directories to exclude. Exclude patterns take precedence over include patterns.

#### Example Configuration (`config/python.yaml`):

```yaml
include:
  - "*.py"
  - "requirements.txt"
  - "config/*.yaml"
exclude:
  - "venv/*"
  - ".gitignore"
  - ".git/*"
  - "build/*"
```

#### Example Configuration (`config/nodejs.yaml`):

```yaml
include:
  - "*.ts"
  - "*.js"
exclude:
  - "dist/*"
  - ".gitignore"
  - ".git/*"
  - "build/*"
  - "node_modules/*"
```

### Examples

1.  **Generate content for a Python project and print to console:**

    ```bash
    python repo_content_generator.py --project . --config config/python.yaml
    ```

    (Assuming your current directory is the root of your Python project.)

2.  **Generate content for a Node.js project and save to a file:**

    ```bash
    python repo_content_generator.py --project /path/to/my/nodejs/app --config config/nodejs.yaml --output my_nodejs_summary.txt
    ```

-----

## Project Structure

```
.
├── repo_content_generator.py   # Main script to generate repository content
├── requirements.txt            # Python dependencies
└── config/
    ├── python.yaml             # Example configuration for Python projects
    └── nodejs.yaml             # Example configuration for Node.js projects
```

-----

## Contributing to Repository Content Generator

Want to help make this project better? Awesome\! Here's how you can contribute.

-----

### Found a Bug?

If something's broken, please [open an issue](https://github.com/bahirul/repo-content/issues) on GitHub. Tell us what went wrong and how we can see it too.

### Have an Idea?

Got a suggestion for a new feature or an improvement? [Open an issue](https://github.com/bahirul/repo-content/issues) and share your thoughts\!

### Want to Code?

If you'd like to write code to fix a bug or add a feature:

1.  **Fork** this project.
2.  **Clone** your copy to your computer.
3.  **Create a new branch** for your changes.
4.  **Make your changes**.
5.  **Test your code**.
6.  **Commit** your changes with a clear message.
7.  **Push** your branch.
8.  **Open a Pull Request** to our main project. Explain what you did\!