import woocommerce

from woocommerce import API

wcapi = API(
    url="https://gioielleriamazzon.it",
    consumer_key ="ck_a9a9a9bccb424ba57a5c1d2ba6d2dd85007d937d",
    consumer_secret = "cs_660dbdd4267f8be9fc7f0bae563237810e5788fd",
    wp_api=True,
    version="wc/v3",
    query_string_auth=True,
)


print(wcapi.get("products", params={"per_page": 20}).json())