
# SKU Technology Mapper with Web Scraping

This Streamlit app allows you to upload an Excel file containing SKUs and maps each SKU to a predefined technology category by scraping firesecurityproducts.com.

## Features
- Upload `.xlsx` file
- Scrape firesecurityproducts.com for each SKU
- Replace SKU with technology category in a new column
- Show progress bar during processing
- Download updated Excel file

## Deployment on Streamlit Cloud
1. Push `app.py` and `requirements.txt` to your GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and connect your GitHub repo.
3. Select `app.py` as the main file.
4. Deploy and use the app online.

## Notes
- This app uses web scraping, which may be slow for large files.
- Add delays to avoid overwhelming the target website.
