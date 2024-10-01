from bs4 import BeautifulSoup
import openpyxl

# Read the HTML file
with open("/Users/namithaprakash/Desktop/Scrape/Flipkart/Flipkart_Mobile.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Define the list of data-tkid values to search for
data_tkid_values = [
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGUFK4TZ2CJYHJ.SEARCH",
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGUFK4P2H9CY7Y.SEARCH",
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGMXSW9PHJVQCA.SEARCH",
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGUFK4QPQMAA2S.SEARCH",
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGQTDP5DGSNS7Q.SEARCH",
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGTEVGHM9ZPZBB.SEARCH",
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGQY93HQSAGAXG.SEARCH",
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGQTDPRFVZQYWB.SEARCH",
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGTEVGGM7CTGXU.SEARCH",
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGVVTESKUVZ8DG.SEARCH",
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGUFK4UBP7ZTXJ.SEARCH",
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGUFK4RNVPCG3M.SEARCH",
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGQY93QMZFZJVN.SEARCH",
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGRNZ3ER4N3K4F.SEARCH",
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGRNZ3FZBVRYHQ.SEARCH",
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGQFX68CXMTSGK.SEARCH",
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGZBFUFNDXSGHS.SEARCH",
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGZBFU4HBKKFSN.SEARCH",
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGRHB7GUUZG3QH.SEARCH",
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGRHB6XAEUADQB.SEARCH",
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGW4HKUXHFDYU2.SEARCH",
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGZJ3ZFQ8AKKRS.SEARCH",
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGZBFUPTU7DNCA.SEARCH",
    "f607e5f6-56d5-437b-877d-6af4c4283ddd.MOBGQFX6H2H2UHFZ.SEARCH"

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
wb.save("Flipkart_Mobile.xlsx")

