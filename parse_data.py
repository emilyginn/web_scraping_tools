##################### PARSE DATA ROWS FROM SCRAPED DATA #####################

def extract_headers(rows):
    from bs4 import BeautifulSoup
    
    for row in rows:
        headers = row.find_all('th')
        header_texts = [header.text.strip() for header in headers]
        if header_texts:
            return header_texts
        
def extract_cells(rows):
    from bs4 import BeautifulSoup 
    
    output_cells = []
    cells = []

    for row in rows:
        find_cells = row.find_all('td')
        cell_data = []
        for cell in find_cells:
            text = cell.get_text(strip=True)
            cell_data.append(text)
        cells.append(cell_data)

    # Print the data
    for cell_data in cells:
        if cell_data:
            output_cells.append(cell_data)
            
    return output_cells

##################### BUILD TABLES FROM PARSED DATA #####################

def build_table(rows):
    import pandas as pd
    return pd.DataFrame(extract_cells(rows), columns=extract_headers(rows))