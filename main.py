from download_resource_images import download_resource_images

url_list = [
    "https://www.saizeriya.co.jp/entertainment/images/1710/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1801/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1804/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1806/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1810/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1812/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1904/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1907/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1910/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1912/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/2003/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/2007/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/2009/body.png"
]
resource_path = "resource"
intermediate_path = "intermediate"
result_path = "result"

download_resource_images(url_list, resource_path)
