from bs4 import BeautifulSoup
import json
with open("input.html", "r", encoding="utf-8") as file:
    html_content = file.read()
soup = BeautifulSoup(html_content, "html.parser")

data = []
rows = soup.find_all("tr")

for row in rows:
    cols = row.find_all("td")
    
    if len(cols) >= 2:
        title_tag = cols[0].find("p")
        title = title_tag.get_text(strip=True) if title_tag else None
        
        img_tag = cols[1].find("img")
        image = img_tag["src"] if img_tag and img_tag.has_attr("src") else None
        
        if title and image:
            data.append({
                "title": title,
                "image": image
            })

with open("output.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

print("✅ تم استخراج البيانات بنجاح!")
