"""Generate a summary of the content in a repository for documentation purposes."""

import argparse
import calendar
import fnmatch
import json
import os
import time

import yaml


def should_include(file_path, should_include_patterns, should_exclude_patterns):
    """Check if a file should be included based on include and exclude patterns."""
    included = any(fnmatch.fnmatch(file_path, pat) for pat in should_include_patterns)
    excluded = any(fnmatch.fnmatch(file_path, pat) for pat in should_exclude_patterns)
    return included and not excluded


def load_config_file(config_path):
    """Load include/exclude patterns from a JSON or YAML config file."""
    if config_path.endswith(".json"):
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    elif config_path.endswith(".yaml") or config_path.endswith(".yml"):
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    else:
        raise ValueError("Unsupported config file format. Use JSON or YAML.")


def generate_repo_content(
    root_dir, repo_include_patterns, repo_exclude_patterns, output_file=None
):
    """Generate a summary of the content in the repository."""
    result = []

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            relative_path = os.path.relpath(full_path, root_dir)

            if not should_include(
                relative_path, repo_include_patterns, repo_exclude_patterns
            ):
                continue

            try:
                print(f"Processing {relative_path}...")
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except (OSError, UnicodeDecodeError) as e:
                print(f"Skipping {relative_path} (error: {e})")
                continue

            result.append(f"Files: {relative_path}\n\n```\n{content}\n```\n")

    final_output = "\n".join(result)

    if output_file:
        with open(output_file, "w", encoding="utf-8") as out:
            out.write(final_output)
        print(f"Output saved to {output_file}")
    else:
        print(final_output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate repo content summary.")
    parser.add_argument("-p", "--project", help="Root project directory", required=True)
    parser.add_argument(
        "-c",
        "--config",
        help="YAML or JSON config file for include/exclude",
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output file name",
        default=f"output/repo_content_{calendar.timegm(time.gmtime())}.txt",
    )

    args = parser.parse_args()

    config = load_config_file(args.config)
    include_patterns = config.get("include", [])
    exclude_patterns = config.get("exclude", [])

    generate_repo_content(
        root_dir=args.project,
        repo_include_patterns=include_patterns,
        repo_exclude_patterns=exclude_patterns,
        output_file=args.output,
    )
