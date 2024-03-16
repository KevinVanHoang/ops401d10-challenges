# README for `stripToLab.py` Script
## Overview
The `stripToLab.py` script is designed to convert documents from HTML format, specifically those exported from Google Docs, into Markdown format. It also extracts images from the document, saves them in a designated directory, and updates their links in the converted Markdown file. This README provides instructions on how to use the script, including preliminary steps to prepare your document for conversion.
## Pre-requisites
Before using `stripToLab.py`, ensure you have the following:
- **Python 3.x** installed on your computer.
- **Required Python libraries**: BeautifulSoup4, markdownify, Pillow (PIL), and tqdm. Install them using pip with the command below:
  ```
  pip install beautifulsoup4 markdownify Pillow tqdm
  ```
## Preparing Your Document
To convert a Google Doc to Markdown, first, you need to export the document as an HTML file. Follow these steps:
1. **Open your Google Doc**: Go to Google Docs and open the document you want to convert.
2. **Download as HTML**: Click on `File` > `Download` > `Web Page (.html, zipped)`.
3. **Unzip the File**: Once downloaded, locate the `.zip` file in your Downloads folder and unzip it. This will create a folder containing an HTML file and a folder with images used in the document.
## Usage Instructions
1. **Open Terminal or Command Prompt**: Navigate to the directory where `stripToLab.py` is saved.
2. **Run the Script**: Execute the script by typing the following command and pressing Enter:
   ```
   ./stripToLab.py
   ```
   or if that doesn't work,
   ```
   python3 stripToLab.py
   ```
3. **Enter the Required Information**: The script will prompt you for:
   - **Folder name**: The name of the folder where your unzipped Google Doc is. This should be the folder that resulted from unzipping your HTML export.
   - **Output name**: A name for your output Markdown file and image directory. This will be used to organize your converted document and its images.
The script will process the HTML file, converting it to Markdown, save images to a specified directory, and update image links accordingly.
## Output
- A **Markdown file** with your content, located in a new directory on your Desktop named after the output name you provided.
- An **images directory** inside your output directory, containing all images from the document, with links in the Markdown file updated to point to this new location.
## Logging
- The script logs its activity and any encountered errors to `conversion.log`, located on your Desktop. This log can be useful for troubleshooting.
## Customization
- Users might need to modify the `input_dir` and `output_dir` paths in the script to match their system's directory structure, especially if the default paths do not align with their environment.
## Troubleshooting
If the script doesn't work as expected:
- Review the `conversion.log` file for error messages.
- Ensure the HTML file and images are correctly placed in the specified input directory.
- Make sure all required libraries are installed.
For additional help, community forums related to Python or document conversion may offer valuable advice.
