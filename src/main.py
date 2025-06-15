from textnode import TextNode, TextType
import os
import sys
import shutil
from pathlib import Path

from nodebuilders import *

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_reader = open(from_path, "r")
    markdown = markdown_reader.read()
    markdown_reader.close()
    
    template_reader = open(template_path)
    template = template_reader.read()
    template_reader.close()

    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)
    template = template.replace('href="/', 'href="' + basepath)
    template = template.replace('src="/', 'src="' + basepath)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def clean_folder(clean_folder_path):
    if not os.path.exists(clean_folder_path):
        print(f"{clean_folder_path} does not exist")
        return
    
    for item in os.listdir(clean_folder_path):
        item_path = os.path.join(clean_folder_path, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        else:
            clean_folder(item_path)
    
    os.rmdir(clean_folder_path)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)

def copy_folder(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_folder(from_path, dest_path)

def setup_static_assets():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_folder(dir_path_static, dir_path_public)

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    setup_static_assets()

    print("Generating page...")

    for item in os.listdir(dir_path_content):
        print(item)

    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)

if __name__=="__main__":
    main()