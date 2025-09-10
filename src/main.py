import sys
import shutil
from copystatic import copy_files_recursive
from generate_pages_recursive import generate_pages_recursive

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    content_dir = "content"
    template_path = "template.html"
    output_dir = "docs"  # GitHub Pages uses /docs

    generate_pages_recursive(content_dir, template_path, output_dir, basepath)

if __name__ == "__main__":
    main()

