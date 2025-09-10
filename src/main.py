import os
import shutil
from copystatic import copy_files_recursive
from generate_pages_recursive import generate_pages_recursive

def main():
    content_dir = "content"
    template_path = "template.html"
    public_dir = "public"

    generate_pages_recursive(content_dir, template_path, public_dir)

if __name__ == "__main__":
    main()
