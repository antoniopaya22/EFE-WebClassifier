import networkx as nx
import os
import re

"""
Creates a list of tuples and for each word, and creates a set 
to avoid the repetitions of the edges.
"""
def obtainGraph(text):
    G=nx.Graph()
    G.add_nodes_from(text)
    edges = []
    for i in range(len(text)-2):
        edge1 = (text[i], text[i+1])
        edge2 = (text[i], text[i+2])
        edge3 = (text[i+1], text[i])
        edge4 = (text[i+1], text[i+2])
        edge5 = (text[i+2], text[i])
        edge6 = (text[i+2], text[i+1])
        edges.append(edge1)
        edges.append(edge2)
        edges.append(edge3)
        edges.append(edge4)
        edges.append(edge5)
        edges.append(edge6)
    G.add_edges_from(set(edges))
    return G

"""
Read the first word of each line.
We obtain words that also contains the character '. 
"""
def obtainEmptyWords():
    file = open("stop.txt", 'r', encoding="utf-8")
    lines = file.readlines()
    file.close()
    wordsList = []
    for line in lines:
        word = re.search(r'\w+(\')*\w*', line.split(" ",1)[0])
        if (word): wordsList.append(word.group())

    return wordsList

def main(data):
    data = {
        "/collections/accessories": "Bullguard antivirus 1 year 3 PC's Regular price £29.99 Samsung 960 EVO 500 GB PCIe NVMe M.2 (2280) Internal Solid State Drive (SSD) (MZ-V7S500) Samsung 960 EVO 500 GB PCIe NVMe M.2 (2280) Internal Solid State Drive (SSD) (MZ-V7S500) Regular price £139.00 Office 365 Personal Office 365 Personal Regular price £59.99 Sandberg USB headset Sandberg USB headset Regular price £26.99 Xiaomi IMILAB Full HD 1080P Webcam Black Xiaomi IMILAB Full HD 1080P Webcam Black Regular price £34.99 SOLD OUT Kingston 32GB USB datatraveler Kingston 32GB USB datatraveler Regular price £7.99 Aiwa AW1 wave - headphones HeadphonesAiwa AW1 wave - headphones Regular price £9.99 Logitech B100 USB Black Mouse Logitech B100 USB Black Mouse Regular price £7.99 Dynamode USB Sound Adapter 7.1 Channel Dynamode USB Sound Adapter 7.1 Channel Regular price £5.99 Transcend RDF5 Super Speed USB 3.1 Gen 1 Interface Card Reader Transcend RDF5 Super Speed USB 3.1 Gen 1 Interface Card Reader Regular price £8.99 Team Group 16 GB USB stick Team Group 16 GB USB stick Regular price £5.99 Kingston 32GB 100 MB/s with adaptor Kingston 32GB 100 MB/s with adaptor Regular price £15.99 Kingston 128GB 100 MB/s with adaptor Kingston 128GB 100 MB/s with adaptor Regular price £24.99 Microsoft Office Home & Business 2019 - 1 user Microsoft Office Home & Business 2019 - 1 user Regular price £269.99 Scorpion HG9015G RGB 7.1 Surround Gaming Headset Scorpion HG9015G RGB 7.1 Surround Gaming Headset Regular price £24.99 Scorpion HG8901 RGB Gaming Headset Scorpion HG8901 RGB Gaming Headset Regular price £15.99 Scorpion KG909 Mechanical Gaming Keyboard Scorpion KG909 Mechanical Gaming Keyboard Regular price £32.99 Apple AirPods Pro With Wireless Charging Case Apple AirPods Pro With Wireless Charging Case Regular price £249.00 Apple AirPods With Wireless Charging Case Apple AirPods With Wireless Charging Case Regular price £199.00 Apple AirPods With Charging Case Apple AirPods With Charging Case Regular price £159.00",
        "/collections/accessories/products/bullguard-antivirus-1-year-3-pcs" : "Bullguard antivirus 1 year 3 PC's Regular price £29.99 Tax included. Add Accessories Quick View Office 365 Personal £59.99 Adding product to your cart Bullguard antivirus 1 year 3 PC's   Product Key card  WHY NOT CHECK OUT.... Samsung 960 EVO 500 GB PCIe NVMe M.2 (2280) Internal Solid State Drive (SSD) (MZ-V7S500) Samsung 960 EVO 500 GB PCIe NVMe M.2 (2280) Internal Solid State Drive (SSD) (MZ-V7S500) VENDOR SAMSUNG Regular price £139.00 Office 365 Personal Office 365 Personal VENDOR MICROSOFT Regular price £59.99 Sandberg USB headset Sandberg USB headset VENDOR SANDBERG Regular price £26.99 Kingston 32GB USB datatraveler Kingston 32GB USB datatraveler VENDOR KINGSTON Regular price £7.99 ",
        "/collections/laptops-and-desktops" : "Acer Aspire 5* WINTER SALE! * Acer Aspire 5 N19H2, Intel i5 10210U Processor, 8GB RAM, 256GB SSD, 14 IPS Thin Bezel FHD Display, Windows 10, 1 Year Warranty. Regular price £579.00 Exist2Game Gaming Turbine E2, AMD Ryzen 5 2600 3.6GHz Hexa Core Processor, 16GB DDR4 3200MHz RAM, 500GB M.2 NVMe SSD, 1TB HDD, Windows 10 Home, 1 Year Warranty. Add A GPU For Additional Cost. Exist2Game Gaming Turbine E2, AMD Ryzen 5 2600 3.6GHz Hexa Core Processor, 16GB DDR4 3200MHz RAM, 500GB M.2 NVMe SSD, 1TB HDD, Windows 10 Home, 1 Year Warranty. Add A GPU For Additional Cost. Regular price £799.00 Exist2Game Gaming Turbine E3 Ultra, High-End Custom PC Build, Intel i9 10850K 3.6GHz, 32GB DDR4 RAM, 512GB M.2 NVMe SSD, 2TB HDD, RTX 3070 Gaming OC Graphics Card, Cooler Master MasterCase H500 ARGB Mid Tower Case, Windows 10 Home, 1 Year Warranty. Exist2Game Gaming Turbine E3 Ultra, High-End Custom PC Build, Intel i9 10850K 3.6GHz, 32GB DDR4 RAM, 512GB M.2 NVMe SSD, 2TB HDD, RTX 3070 Gaming OC Graphics Card, Cooler Master MasterCase H500 ARGB Mid Tower Case, Windows 10 Home, 1 Year Warranty. Regular price £1,999.00 HP AIO Q046, Intel i5-9400T, 8GB RAM, 16GB Intel Optane Memory, 1TB HDD, 23.8 FHD Display, Windows 10, 1 Year Warranty. HP AIO Q046, Intel i5-9400T, 8GB RAM, 16GB Intel Optane Memory, 1TB HDD, 23.8 FHD Display, Windows 10, 1 Year Warranty. Regular price £729.00 Acer Aspire 5, Intel i3-1011U, 4GB RAM, 256GB SSD, 14 FHD Display, Windows 10, 1 Year Warranty. Acer Aspire 5, Intel i3-1011U, 4GB RAM, 256GB SSD, 14 FHD Display, Windows 10, 1 Year Warranty. Regular price £479.00 SOLD OUT Acer Swift 1, Intel Pentuim Silver N5000, 4GB RAM, 128GB SSD, 14 FHD Display, Windows 10, 1 Year Warranty. Acer Swift 1, Intel Pentuim Silver N5000, 4GB RAM, 128GB SSD, 14 FHD Display, Windows 10, 1 Year Warranty. Regular price £479.00 Acer Aspire AIO C22-820, Intel Pentium Silver J5005 Processor, 4GB RAM, 1TB HDD, 21.5 FHD Display, Windows 10, 1 Year Warranty. Acer Aspire AIO C22-820, Intel Pentium Silver J5005 Processor, 4GB RAM, 1TB HDD, 21.5 FHD Display, Windows 10, 1 Year Warranty. Regular price £409.00 Acer Aspire 5, Intel i5-8265U, 8GB RAM, 256GB SSD, 14 FHD Display, Windows 10, 1 Year Warranty. Acer Aspire 5, Intel i5-8265U, 8GB RAM, 256GB SSD, 14 FHD Display, Windows 10, 1 Year Warranty. Regular price £559.00 Predator Orion 5000 Gaming PC, Intel i5-9400F, GTX 1660 Ti, 8GB RAM 1TB HDD, 256GB SSD, Windows 10, 1 Year warranty. Predator Orion 5000 Gaming PC, Intel i5-9400F, GTX 1660 Ti, 8GB RAM 1TB HDD, 256GB SSD, Windows 10, 1 Year warranty. Regular price £1,099.00 Acer Nitro N50-600 Gaming PC, Core i5 9400F Processor, 8GB RAM, 1TB HDD, 256GB SSD, Nvidia GTX1660 TI, Windows 10, 1 Year Warranty. Acer Gaming PCAcer Nitro N50-600 Gaming PC, Core i5 9400F Processor, 8GB RAM, 1TB HDD, 256GB SSD, Nvidia GTX1660 TI, Windows 10, 1 Year Warranty. Regular price £829.00 Acer Nitro N50-600 Gaming PC, Core i5-9400F Processor, 8GB RAM, 1TB HDD, 126 GB SSD, Nvidia GTX1650 4GB, Windows 10, 1 Year Warranty. Acer Gaming PCAcer Nitro N50-600 Gaming PC, Core i5-9400F Processor, 8GB RAM, 1TB HDD, 126 GB SSD, Nvidia GTX1650 4GB, Windows 10, 1 Year Warranty. Regular price £759.00 Lenovo V530S, Intel Core i5-8400, 8GB RAM, 256GB SSD, DVD-RW, Windows 10 Home, 1 Year Warranty. Lenovo V530S, Intel Core i5-8400, 8GB RAM, 256GB SSD, DVD-RW, Windows 10 Home, 1 Year Warranty. Regular price £519.00 HP 14S, 14 Display, Intel Pentium Gold 5405U Processor, 4GB RAM, 128GB SSD, Windows 10 S Mode, 1 Year Warranty. HP 14S, 14 Display, Intel Pentium Gold 5405U Processor, 4GB RAM, 128GB SSD, Windows 10 S Mode, 1 Year Warranty. Regular price £499.00 Lenovo V130, Intel Core i5 7200U Processor, 8GB RAM, 256GB SSD, Windows 10 Home, 1 Year Warranty Lenovo V130, Intel Core i5 7200U Processor, 8GB RAM, 256GB SSD, Windows 10 Home, 1 Year Warranty Regular price £539.00 Acer C24-860 All-In-One core i5, 8gb, 23.8 screen, windows 10 Acer desktopAcer C24-860 All-In-One core i5, 8gb, 23.8 screen, windows 10 Regular price £499.99 Custom Workstation PC, Intel i5 9400 4.10GHz, 8GB DDR4 RAM, 1TB HDD, Intel UHD Graphics onboard, Nvidia GT210 1GB Graphics Card, Windows 10, 1 Year Warranty. Custom Workstation PC, Intel i5 9400 4.10GHz, 8GB DDR4 RAM, 1TB HDD, Intel UHD Graphics onboard, Nvidia GT210 1GB Graphics Card, Windows 10, 1 Year Warranty. Regular price £699.00 HP Stream, Intel Celeron N4000,2GB RAM, 32GB eMMC, 11 Display, Windows 10 S mode, 1 Year Warranty HP Stream, Intel Celeron N4000,2GB RAM, 32GB eMMC, 11 Display, Windows 10 S mode, 1 Year Warranty Regular price £199.00 HP Spectre, Intel i7-8750H, 8GB RAM, Nvidia GTX 1050Ti GPU, 512GB SSD,15.6 Display, 360 Touchscreen, Fingerprint scanner, Windows 10, 1 Year Warranty HP Spectre, Intel i7-8750H, 8GB RAM, Nvidia GTX 1050Ti GPU, 512GB SSD,15.6 Display, 360 Touchscreen, Fingerprint scanner, Windows 10, 1 Year Warranty Regular price £1,275.00 Exist2Game Gaming Turbine E1, Intel i5-6600 3.3GHz Quad Core Processor, 16GB DDR4 2400MHz RGB RAM, 256GB 2.5 SSD, 1TB HDD, Nvidia GTX 1650 OC 4GB, Windows 10 Home, 1 Year Warranty. Exist2Game Gaming Turbine E1, Intel i5-6600 3.3GHz Quad Core Processor, 16GB DDR4 2400MHz RGB RAM, 256GB 2.5 SSD, 1TB HDD, Nvidia GTX 1650 OC 4GB, Windows 10 Home, 1 Year Warranty. Regular price £599.00 SOLD OUT HP 14S, 14 Display, Intel Pentium Gold Processor, 4GB RAM, 128GB SSD, Windows 10 Home, 1 Year Warranty. HP 14S, 14 Display, Intel Pentium Gold Processor, 4GB RAM, 128GB SSD, Windows 10 Home, 1 Year Warranty. Regular price £359.00 SOLD OUT"
    }

    result = {} 

    print("Obtaining keywords")

    for key in data:
        text = re.sub("\d+", "", data[key])
        text = re.findall(r'\w+', text.lower())
        graph = obtainGraph(text)
        pr = nx.pagerank(graph)
        emptyWords = obtainEmptyWords()
        for w in emptyWords:
            if (w in pr): pr.pop(w)
        orderedWords = [k for k, v in sorted(pr.items(), key=lambda item: item[1], reverse=True)]
        orderedWords = list(filter(lambda w: len(w) > 1, orderedWords))
        result[key] = orderedWords[:20]
        

    print("Result: ", result)
    print("Finished!")

main(0)
# if __name__ == '__main__':
#     main(sys.argv[1])