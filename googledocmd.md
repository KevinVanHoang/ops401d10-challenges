#!/usr/bin/env python3

import os
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from PIL import Image
from tqdm import tqdm
import logging

# Setup logging
logging.basicConfig(filename='/Users/andrewcarroll/Desktop/conversion.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('DocToMarkdownConverter')

def strip_styles_and_classes(soup):
    # Remove all style tags
    for style in soup.find_all('style'):
        style.decompose()
    # Optionally, remove all class attributes from all tags
    for tag in soup.find_all(True):
        tag.attrs = {key: value for key, value in tag.attrs.items() if key != 'class'}

def convert_to_markdown():
    try:
        folder_name = input("Please enter the name of the folder containing the unzipped Google Doc: ")
        input_dir = os.path.join('/Users/andrewcarroll/Downloads', folder_name)

        if not os.path.isdir(input_dir):
            print(f"The specified directory does not exist: {input_dir}")
            return

        output_name = input("Please enter the output name (e.g., lab40, ops44): ")
        output_dir = os.path.join('/Users/andrewcarroll/Desktop', output_name)
        os.makedirs(output_dir, exist_ok=True)

        # New media directory for images
        media_dir = os.path.join(output_dir, "media")
        os.makedirs(media_dir, exist_ok=True)

        html_files = [f for f in os.listdir(input_dir) if f.endswith('.html')]
        if not html_files:
            print("No HTML file found in the specified directory.")
            return
        html_path = os.path.join(input_dir, html_files[0])

        with open(html_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')

        strip_styles_and_classes(soup)

        images = soup.find_all('img')
        for img_index, img in enumerate(tqdm(images, desc="Processing Images"), start=1):
            img_path = os.path.join(input_dir, img['src'].lstrip('/'))
            new_img_name = f"{output_name}-{img_index}.png"
            new_img_path = os.path.join(media_dir, new_img_name)
            
            with Image.open(img_path) as image:
                image.save(new_img_path, 'PNG')
            # Update the src attribute to point to the new location
            img['src'] = os.path.join("media", new_img_name)

        markdown_text = md(str(soup))
        md_file_path = os.path.join(output_dir, f"{output_name}.md")
        with open(md_file_path, 'w', encoding='utf-8') as md_file:
            md_file.write(markdown_text)

        logger.info(f"Conversion completed successfully. Markdown file and images saved to {output_dir}")
        print(f"Conversion completed successfully. Markdown file and images saved to {output_dir}")

    except KeyboardInterrupt:
        logger.info("Script execution was interrupted by user.")
        print("Script execution was interrupted. Exiting gracefully.")
    except Exception as e:
        logger.error(f"Error during conversion: {e}")
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    convert_to_markdown()
