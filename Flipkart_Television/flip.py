from bs4 import BeautifulSoup
import openpyxl

# Read the HTML file
with open("/Users/namithaprakash/Desktop/Scrape/Flipkart/Flipkart_Television.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Define the list of data-tkid values to search for
data_tkid_values = [
    "en_4pm7weSLmiC_9dIP6PhCLwd8LAA_KhBI2ucyCSVhNi5lMnghfkTBqcVFQbNYzk2e-uBrJIcG8z_VYBXGyq2yGfUFjCTyOHoHZs-Z5_PS_w0=",
    "en_4pm7weSLmiC_9dIP6PhCLwd8LAA_KhBI2ucyCSVhNi6GQTr8Mo3i58Q42YafRhyhK63XuIDzIWIVSCA2lSMo8YQEIsITtCzc4bHaOMTqL08=",
    "be43a9f9-d4d8-4e54-ad52-edfe5267ffb4.TVSGC8FKBCFFBFT7.SEARCH",
    "be43a9f9-d4d8-4e54-ad52-edfe5267ffb4.TVSGEMQV7R4CMTGA.SEARCH",
    "be43a9f9-d4d8-4e54-ad52-edfe5267ffb4.TVSGMGWWZYMMPG83.SEARCH",
    "be43a9f9-d4d8-4e54-ad52-edfe5267ffb4.TVSGSHZRWZPTZ47Z.SEARCH",
    "en_4pm7weSLmiC_9dIP6PhCLwd8LAA_KhBI2ucyCSVhNi7Sl3pfaZeANHJy43ZLIdPnDgzqBP-u3I-STDKw_vFtL-I7uWi7bi3WLqk6JF-UYDE=",
    "en_4pm7weSLmiC_9dIP6PhCLwd8LAA_KhBI2ucyCSVhNi7ijOMQb7p02Z_og5qTDAua35wO5OTF0DorU0evd2dGgg==",
    "be43a9f9-d4d8-4e54-ad52-edfe5267ffb4.TVSGZ8GQEPCENXHC.SEARCH",
    "be43a9f9-d4d8-4e54-ad52-edfe5267ffb4.TVSGRFZN7VS3AKFM.SEARCH",
    "en_4pm7weSLmiC_9dIP6PhCLwd8LAA_KhBI2ucyCSVhNi4IbLIMZ1Q31L70V5F6OwZ1UuIRI5Tw-8C7q7udk34rkQDM2KWit8hFHxJOvPdMi04=",
    "en_4pm7weSLmiC_9dIP6PhCLwd8LAA_KhBI2ucyCSVhNi5VzN--v-aQw2JBcvXL5YiUy6_7e_AriGgn6lfpkk7SnBhTy0lUJ14SzoMSv_CzLF0=",
    "be43a9f9-d4d8-4e54-ad52-edfe5267ffb4.TVSGS8GYDQXWP8QX.SEARCH",
    "be43a9f9-d4d8-4e54-ad52-edfe5267ffb4.TVSGRS7GYVN3UZNZ.SEARCH",
    "be43a9f9-d4d8-4e54-ad52-edfe5267ffb4.TVSGRFZN4AXHVHFQ.SEARCH",
    "be43a9f9-d4d8-4e54-ad52-edfe5267ffb4.TVSGRNGZGWNFGCZM.SEARCH",
    "be43a9f9-d4d8-4e54-ad52-edfe5267ffb4.TVSGRFZNKSWQN6G8.SEARCH",
    "be43a9f9-d4d8-4e54-ad52-edfe5267ffb4.TVSGHY2UZA9YHWQN.SEARCH",
    "be43a9f9-d4d8-4e54-ad52-edfe5267ffb4.TVSGRTDDGYA4HPWU.SEARCH",
    "be43a9f9-d4d8-4e54-ad52-edfe5267ffb4.TVSGSRQ9SXPXPTXJ.SEARCH",
    "be43a9f9-d4d8-4e54-ad52-edfe5267ffb4.TVSGZ8GQDGNYHDPR.SEARCH",
    "be43a9f9-d4d8-4e54-ad52-edfe5267ffb4.TVSGRFZNMPKT7RVK.SEARCH",
    "be43a9f9-d4d8-4e54-ad52-edfe5267ffb4.TVSGRFZNG6FY3D2S.SEARCH",
    "be43a9f9-d4d8-4e54-ad52-edfe5267ffb4.TVSGPGXBCEPEZH2Q.SEARCH"
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
wb.save("Flipkart_Television.xlsx")
