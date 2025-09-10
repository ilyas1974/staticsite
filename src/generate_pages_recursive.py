import os
from pathlib import Path
from tempfile import template
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

def convert_markdown_to_html(markdown: str) -> str:
    return markdown_to_html_node(markdown).to_html()

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str):
    template = Path(template_path).read_text()

    for root, _, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                md_path = Path(root) / file
                rel_path = md_path.relative_to(dir_path_content)
                html_filename = rel_path.with_suffix("") / "index.html"
                dest_path = Path(dest_dir_path) / html_filename

                dest_path.parent.mkdir(parents=True, exist_ok=True)

                markdown = md_path.read_text()
                body = convert_markdown_to_html(markdown)
                title = extract_title(markdown)

                final_html = template.replace("{{ Title }}", title).replace("{{ Content }}", body)
                dest_path.write_text(final_html)

