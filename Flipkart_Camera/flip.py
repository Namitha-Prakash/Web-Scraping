from bs4 import BeautifulSoup
import openpyxl

# Read the HTML file
with open("/Users/namithaprakash/Desktop/Scrape/Flipkart_Camera/Flipkart.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Define the list of data-tkid values to search for
data_tkid_values = [
    "en_kwUgLyfE845bNPWlsin1hnbYTsoQzWGKpvPWqspPl360VVTM2O8JnLDSMdE7BE26C3HuHElpRoVda74qhJrfdg==",
    "en_kwUgLyfE845bNPWlsin1hnbYTsoQzWGKpvPWqspPl37jbaPZjgY-mC_ImgMNxLmBBIqq5XrNzAsnAhmZ1bG42Q==",
    "27941d5b-fa5b-41fa-a8e2-dbe6f5193d00.DLLFDJ9DFXVAZDTS.SEARCH",
    "27941d5b-fa5b-41fa-a8e2-dbe6f5193d00.DLLG6G8U8P2NGEHG.SEARCH",
    "27941d5b-fa5b-41fa-a8e2-dbe6f5193d00.CAMFM67HBBUJWA9Y.SEARCH",
    "27941d5b-fa5b-41fa-a8e2-dbe6f5193d00.DLLF7GBGWYNB5SZK.SEARCH",
    "27941d5b-fa5b-41fa-a8e2-dbe6f5193d00.DLLFHY8YCXP7WM32.SEARCH",
    "en_kwUgLyfE845bNPWlsin1hnbYTsoQzWGKpvPWqspPl358W1SJpIzTCkQSimEm5924arT1HM9otk0Ie2VBFC1gvA==",
    "27941d5b-fa5b-41fa-a8e2-dbe6f5193d00.DLLGBKMZHNUDSPBP.SEARCH",
    "27941d5b-fa5b-41fa-a8e2-dbe6f5193d00.DLLG6G8UNHFCDYY9.SEARCH",
    "27941d5b-fa5b-41fa-a8e2-dbe6f5193d00.CAMFM67HGGZDDXUE.SEARCH",
    "27941d5b-fa5b-41fa-a8e2-dbe6f5193d00.DLLF6QZPNKTQMS8J.SEARCH",
    "27941d5b-fa5b-41fa-a8e2-dbe6f5193d00.DLLFHY8YC9GHHZH4.SEARCH",
    "27941d5b-fa5b-41fa-a8e2-dbe6f5193d00.DLLF7GBGTVVCVHAQ.SEARCH",
    "27941d5b-fa5b-41fa-a8e2-dbe6f5193d00.DLLG2XDCDGMG54AJ.SEARCH",
    "27941d5b-fa5b-41fa-a8e2-dbe6f5193d00.CAMFM67HNWZRQMC4.SEARCH",
    "27941d5b-fa5b-41fa-a8e2-dbe6f5193d00.DLLFDJ8AHYXPQKRG.SEARCH",
    "27941d5b-fa5b-41fa-a8e2-dbe6f5193d00.DLLGARYGYKXAWATX.SEARCH",
    "27941d5b-fa5b-41fa-a8e2-dbe6f5193d00.DLLGGYSTMHSSXFZR.SEARCH",
    "27941d5b-fa5b-41fa-a8e2-dbe6f5193d00.DLLGGYSTTDDMGMX3.SEARCH",
    "27941d5b-fa5b-41fa-a8e2-dbe6f5193d00.DLLGFY7XYG8YFMQT.SEARCH",
    "27941d5b-fa5b-41fa-a8e2-dbe6f5193d00.DLLG2XDCY9HZMBB7.SEARCH",
    "27941d5b-fa5b-41fa-a8e2-dbe6f5193d00.DLLGGYSQZ7ZGD5PA.SEARCH",
    "27941d5b-fa5b-41fa-a8e2-dbe6f5193d00.DLLFYB4EDZXMPXWG.SEARCH"

]

# Initialize lists to store product information
product_names = []
product_prices = []
product_reviews = []

# Iterate over each data-tkid value
for data_tkid_value in data_tkid_values:
    # Find all divs with class="_2kHMtA" and the specified data-tkid attribute
    divs = soup.find_all('div', class_='_2kHMtA', attrs={'data-tkid': data_tkid_value})
    
    # Extract data for each div
    for div in divs:
        # Find div with class="_4rR01T" (Product Name)
        product_name_tag = div.find("div", class_="_4rR01T")
        product_name = product_name_tag.get_text(strip=True) if product_name_tag else ""

        # Find div with class="_30jeq3 _1_WHN1" (Product Price)
        product_price_tag = div.find("div", class_="_30jeq3 _1_WHN1")
        product_price = product_price_tag.get_text(strip=True) if product_price_tag else ""

        # Find div with class="_3LWZlK" (Product Reviews)
        product_reviews_tag = div.find("div", class_="_3LWZlK")
        product_review = product_reviews_tag.get_text(strip=True) if product_reviews_tag else ""

        # Append product information to lists
        product_names.append(product_name)
        product_prices.append(product_price)
        product_reviews.append(product_review)

# Write data to Excel file
wb = openpyxl.Workbook()
ws = wb.active

# Write headers
ws.append(["Product Name", "Product Price", "Product Reviews"])

# Write data
for name, price, review in zip(product_names, product_prices, product_reviews):
    ws.append([name, price, review])

# Save Excel file
wb.save("Flipkart_Camera.xlsx")
