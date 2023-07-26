# Selenium File Downloader

This Python script utilizes the Selenium library to interact with the website [https://stats.oecd.org/](https://stats.oecd.org/) and download files from it. The website provides statistical data from the Organisation for Economic Co-operation and Development (OECD) on various topics.

## Prerequisites

1. Python 3.x installed on your system.
2. Install required packages by running `pip install selenium`.

## Webdriver Setup

1. Download the appropriate WebDriver for your browser:
   - Chrome: [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
   - Firefox: [GeckoDriver](https://github.com/mozilla/geckodriver/releases)

2. Place the WebDriver executable in the same directory as the Python script.

## Configuration

Open the Python script `selenium_file_downloader.py` and modify the following variables as per your environment:

```python
download_dir = "YOUR-ABSOLUTE-DOWNLOAD-DIRECTORY-PATH"
```

Set the `download_dir` variable to the absolute path of the directory where you want the downloaded files to be saved.

## Running the Script

Run the Python script `selenium_file_downloader.py`:

```bash
python selenium_file_downloader.py
```

The script will use Selenium to navigate to the [https://stats.oecd.org/](https://stats.oecd.org/) website, search for specific statistical data, and download the files to the specified `download_dir` directory.

## Important Notes

- Ensure that you have the necessary permissions to download files from the website.
- Always comply with the terms of service and usage policies of the website.
- Use this script responsibly and avoid causing any load or strain on the website's server.

Feel free to explore and modify the script according to your specific requirements and file download needs. Happy coding!
