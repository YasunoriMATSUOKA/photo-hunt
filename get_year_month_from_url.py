def get_year_month_from_url(url):
    year_month = url.replace(
        "https://www.saizeriya.co.jp/entertainment/images/", "").replace("/body.png", "")
    return year_month
