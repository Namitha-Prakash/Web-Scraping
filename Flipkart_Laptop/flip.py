from bs4 import BeautifulSoup
import openpyxl

# Read the HTML file
with open("/Users/namithaprakash/Desktop/Scrape/Flipkart_Laptop/Flipkart_Laptop.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Define the list of data-tkid values to search for
data_tkid_values = [
    "en_-LzNkdyIFH3MAabz42mf2sM72owmWwt-_UFIybAYKGwXQa7LsXWJGq4ZgNrEWriAwHbzu7u-sFuJLp3nCv5BJA==",
    "en_-LzNkdyIFH3MAabz42mf2sM72owmWwt-_UFIybAYKGwkehcEbYWyeVrXIBvDk3BefIyPb4cq1W-nekcYDAAPBPUFjCTyOHoHZs-Z5_PS_w0=",
    "8a144dfb-8dac-4f66-84ff-8141a12c0418.COMGKW2NSU4SPZSG.SEARCH",
    "8a144dfb-8dac-4f66-84ff-8141a12c0418.COMGH3V3UUGM46BQ.SEARCH",
    "8a144dfb-8dac-4f66-84ff-8141a12c0418.COMG9WH98ZNYXWYH.SEARCH",
    "8a144dfb-8dac-4f66-84ff-8141a12c0418.COMGHAGN3U9FJH39.SEARCH",
    "8a144dfb-8dac-4f66-84ff-8141a12c0418.COMGRC9RPSRGEWRT.SEARCH",
    "en_-LzNkdyIFH3MAabz42mf2sM72owmWwt-_UFIybAYKGzEMdZtClP0PqcdTHoB8DlLFicfvUYQYcWJ6DeeXNigLUKsf8s6I2Oz2HOgbXTo_9U=",
    "8a144dfb-8dac-4f66-84ff-8141a12c0418.COMGTDKFTDWHWXX5.SEARCH",
    "8a144dfb-8dac-4f66-84ff-8141a12c0418.COMGPYKZAWY8UX6C.SEARCH",
    "en_-LzNkdyIFH3MAabz42mf2sM72owmWwt-_UFIybAYKGx6zywgEzf0qBjx44GlPZzOMo9kt81_sWnE5snBmn0QGEhz9c-MSIoFe8xMxkfU6dM=",
    "en_-LzNkdyIFH3MAabz42mf2sM72owmWwt-_UFIybAYKGyJ4FSA0qP3r2A2wnnGwHQsNqe6NC0jg5yZZjkQ05BOBK8iqbiwhGf4dwbXVx7ZSks=",
    "8a144dfb-8dac-4f66-84ff-8141a12c0418.COMGHNBG4KF5UYJH.SEARCH",
    "8a144dfb-8dac-4f66-84ff-8141a12c0418.COMGRDC8H7JACZJQ.SEARCH",
    "8a144dfb-8dac-4f66-84ff-8141a12c0418.COMGRDC8H7JACZJQ.SEARCH",
    "8a144dfb-8dac-4f66-84ff-8141a12c0418.COMGJ75HJGFDJ6JN.SEARCH",
    "8a144dfb-8dac-4f66-84ff-8141a12c0418.COMGMGXFGF7ZTKHF.SEARCH",
    "en_-LzNkdyIFH3MAabz42mf2sM72owmWwt-_UFIybAYKGztkJVtrz2BaYq7L50fMTZFN0duTjjm0QwrXJQpOttAO2Vkv0XZFiOX7bbXdlao_f8=",
    "en_-LzNkdyIFH3MAabz42mf2sM72owmWwt-_UFIybAYKGzj6HOHamICX3Fl5cZM9bVy1Pc2dqra_VxHweGIEtQ5dssrgPW5YLzJU0_H6_RHKR0=",
    "8a144dfb-8dac-4f66-84ff-8141a12c0418.COMGZ7FRUHRF8AA3.SEARCH",
    "8a144dfb-8dac-4f66-84ff-8141a12c0418.COMGRZNJNFT765HD.SEARCH",
    "en_-LzNkdyIFH3MAabz42mf2sM72owmWwt-_UFIybAYKGzRBWZ2sZ0Co5LmrGTOkuLV4CtW1g75cwbvOkoaKMKGi8DbPjpExlWhmpgUQnOg2ao=",
    "en_-LzNkdyIFH3MAabz42mf2sM72owmWwt-_UFIybAYKGxcEQUHkeUqtKpKRYxPaCgwF4cMCCu4FYy3FvVTBNtGkWJMZAJirnjvZRqZ0WhE16A=",
    "8a144dfb-8dac-4f66-84ff-8141a12c0418.COMGPQEXKNS6N2ZM.SEARCH",
    "8a144dfb-8dac-4f66-84ff-8141a12c0418.COMGNRNUUGYRB96A.SEARCH"

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
wb.save("Flipkart_Laptop.xlsx")
