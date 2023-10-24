# Zillow Rental Listings to Google Forms

This project automates the process of scraping rental listings from Zillow and populating a Google Form with the scraped data. This can be very useful for personal or small-scale real estate projects.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.6 or higher.
- ChromeDriver compatible with the version of Chrome you have installed.

### Libraries Used

- Selenium: For browser automation to interact with the web page and Google Forms.
- BeautifulSoup: For parsing HTML and extracting the required information.

### Installation

1. Clone the repository or download the project to your local machine.
2. Install the required libraries using pip:

```bash
pip install selenium beautifulsoup4
```

[Download ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) from the official website and place it in the project directory or a location in your system PATH.

## Configuration

1. Update the `GOOGLE_SHEETS` and `ZILLOW_URL` variables in the script with your Google Form URL and the Zillow URL for the rental listings you're interested in.
2. (Optional) Update the `options` object with any additional Chrome options you want to use.

## Usage

Run the script from the command line:

```bash
python main.py
```

The script will scrape rental listings from the specified Zillow URL, then navigate to the specified Google Form URL and populate the form with the listing data, submitting one form per listing.

## Customization

You can customize the script to fit your needs by modifying the XPath selectors to match the structure of your Google Form, or by modifying the scraping logic to extract different data from Zillow.

## Notes

- Be sure to comply with Zillow's terms of use and Google's terms of service when using this script.
- The script uses headless Chrome, but you can disable headless mode in the `options` object if you want to see the browser while the script is running.

## Contributing

Feel free to fork the project and submit pull requests for any enhancements you'd like to contribute.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
