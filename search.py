import json

# Sample data for similar products
similar_products = [
    {
        "id": 15970,
        "gender": "Men",
        "masterCategory": "Apparel",
        "subCategory": "Topwear",
        "articleType": "Shirts",
        "baseColor": "Navy Blue",
        "season": "Fall",
        "year": 2011.0,
        "usage": "Casual",
        "productDisplayName": "Turtle Check Men Navy Blue Shirt",
        "SKU": "M15970",
        "imgFilePath": "data/sampledataset/imgsample000001.jpg"
    },
    {
        "id": 39386,
        "gender": "Men",
        "masterCategory": "Apparel",
        "subCategory": "Bottomwear",
        "articleType": "Jeans",
        "baseColor": "Blue",
        "season": "Summer",
        "year": 2012.0,
        "usage": "Casual",
        "productDisplayName": "Peter England Men Party Blue Jeans",
        "SKU": "M39386",
        "imgFilePath": "data/sampledataset/imgsample000003.jpg"
    },
    {
        "id": 59263,
        "gender": "Women",
        "masterCategory": "Accessories",
        "subCategory": "Watches",
        "articleType": "Watches",
        "baseColor": "Silver",
        "season": "Winter",
        "year": 2016.0,
        "usage": "Casual",
        "productDisplayName": "Titan Women Silver Watch",
        "SKU": "W59263",
        "imgFilePath": "data/sampledataset/imgsample000004.jpg"
    },
    {
        "id": 21379,
        "gender": "Men",
        "masterCategory": "Apparel",
        "subCategory": "Bottomwear",
        "articleType": "Track Pants",
        "baseColor": "Black",
        "season": "Fall",
        "year": 2011.0,
        "usage": "Casual",
        "productDisplayName": "Manchester United Men Solid Black Track Pants",
        "SKU": "M21379",
        "imgFilePath": "data/sampledataset/imgsample000005.jpg"
    },
    {
        "id": 53759,
        "gender": "Men",
        "masterCategory": "Apparel",
        "subCategory": "Topwear",
        "articleType": "Tshirts",
        "baseColor": "Grey",
        "season": "Summer",
        "year": 2012.0,
        "usage": "Casual",
        "productDisplayName": "Puma Men Grey T-shirt",
        "SKU": "M53759",
        "imgFilePath": "data/sampledataset/imgsample000006.jpg"
    },
    {
        "id": 17036,
        "gender": "Men",
        "masterCategory": "Footwear",
        "subCategory": "Shoes",
        "articleType": "Casual Shoes",
        "baseColor": "White",
        "season": "Summer",
        "year": 2013.0,
        "usage": "Casual",
        "productDisplayName": "Gas Men Caddy Casual Shoe",
        "SKU": "M17036",
        "imgFilePath": "data/sampledataset/imgsample000007.jpg"
    },
    {
        "id": 6461,
        "gender": "Men",
        "masterCategory": "Footwear",
        "subCategory": "Flip Flops",
        "articleType": "Flip Flops",
        "baseColor": "Red",
        "season": "Summer",
        "year": 2011.0,
        "usage": "Casual",
        "productDisplayName": "Lotto Men's Soccer Track Flip Flop",
        "SKU": "M6461",
        "imgFilePath": "data/sampledataset/imgsample000008.jpg"
    },
    {
        "id": 18842,
        "gender": "Men",
        "masterCategory": "Apparel",
        "subCategory": "Topwear",
        "articleType": "Tshirts",
        "baseColor": "Blue",
        "season": "Fall",
        "year": 2011.0,
        "usage": "Casual",
        "productDisplayName": "Puma Men Graphic Stellar Blue Tshirt",
        "SKU": "M18842",
        "imgFilePath": "data/sampledataset/imgsample000001.jpg"
    },
    {
        "id": 46694,
        "gender": "Women",
        "masterCategory": "Personal Care",
        "subCategory": "Fragrance",
        "articleType": "Perfume and Body Mist",
        "baseColor": "Blue",
        "season": "Spring",
        "year": 2017.0,
        "usage": "Casual",
        "productDisplayName": "Rasasi Women Blue Lady Perfume",
        "SKU": "W46694",
        "imgFilePath": "data/sampledataset/imgsample000003.jpg"
    },
    {
        "id": 51623,
        "gender": "Women",
        "masterCategory": "Accessories",
        "subCategory": "Watches",
        "articleType": "Watches",
        "baseColor": "Pink",
        "season": "Winter",
        "year": 2016.0,
        "usage": "Casual",
        "productDisplayName": "Fossil Women Pink Dial Chronograph Watch ES3050",
        "SKU": "W51623",
        "imgFilePath": "data/sampledataset/imgsample000004.jpg"
    }
]

similar_products2 = [
    {
        "id": 55970,
        "gender": "Women",
        "masterCategory": "Footwear",
        "subCategory": "Women's shoe",
        "articleType": "Sandal",
        "baseColor": "Black",
        "season": "Fall",
        "year": 2023.0,
        "usage": "Casual",
        "SKU": "S27668",
        "site": "Amazon",
        "productDisplayName": "Kenneth Cole REACTION Women's Fine Glass Slingback Platform Sandal",
        "prices": "$31.32 - $41.30",
        "referralLink": "https://www.amazon.com/Kenneth-Cole-REACTION-Womens-Sandal/dp/B01AXPFQUK/",
        "imgFilePath": "data/sampledataset/0001amazon.jpg"
    },
    {
        "id": 15971,
        "gender": "Women",
        "masterCategory": "Footwear",
        "subCategory": "Women's shoe",
        "articleType": "Sandal",
        "baseColor": "Black",
        "season": "Fall",
        "year": 2023.0,
        "usage": "Casual",
        "SKU": "S27668",
        "site": "Walmart",
        "productDisplayName": "Women's Kenneth Cole Reaction Fine Glass Wedge Sandal",
        "prices": "$78.09",
        "referralLink": "https://www.walmart.com/ip/Women-s-Kenneth-Cole-Reaction-Fine-Glass-Wedge-Sandal/232044097",
        "imgFilePath": "data/sampledataset/0001walmart.jpg"
    },
        {
        "id": 15972,
        "gender": "Women",
        "masterCategory": "Footwear",
        "subCategory": "Women's shoe",
        "articleType": "Sandal",
        "baseColor": "Black",
        "season": "Fall",
        "year": 2023.0,
        "usage": "Casual",
        "SKU": "S27668",
        "site": "Zappos",
        "productDisplayName": "Kenneth Cole Reaction Fine Glass",
        "prices": "$41.30",
        "referralLink": "https://www.zappos.com/p/kenneth-cole-reaction-fine-glass/product/9100912",
        "imgFilePath": "data/sampledataset/0001zappos.jpg"
    },
        {
        "id": 15973,
        "gender": "Women",
        "masterCategory": "Footwear",
        "subCategory": "Women's shoe",
        "articleType": "Sandal",
        "baseColor": "Black",
        "season": "Fall",
        "year": 2023.0,
        "usage": "Casual",
        "SKU": "S2766187",
        "site": "Target",
        "productDisplayName": "Journee Collection Womens Mckell Wedge Heel Buckle Sandals",
        "prices": "$58.99",
        "referralLink": "https://www.target.com/p/journee-collection-womens-mckell-wedge-heel-buckle-sandals/-/A-88470806",
        "imgFilePath": "data/sampledataset/0001target.jpg"
    },    {
        "id": 15974,
        "gender": "Women",
        "masterCategory": "Footwear",
        "subCategory": "Women's shoe",
        "articleType": "Sandal",
        "baseColor": "Black",
        "season": "Fall",
        "year": 2023.0,
        "usage": "Casual",
        "SKU": "S276423",
        "site": "Lightinthebox",
        "productDisplayName": "Women's Sandals Comfort Shoes Outdoor Slippers Outdoor Daily Summer Embroidery Wedge Heel Open Toe Casual Chinoiserie Walking Shoes Faux Leather Loafer Floral Black Red Brown",
        "prices": "$18.90",
        "referralLink": "https://www.lightinthebox.com/en/p/women-s-sandals-wedge-heel-round-toe-pu-floral-black-red-brown_p8635416.html",
        "imgFilePath": "data/sampledataset/0001light.jpg"
    }    
]


# Convert the list of similar products to JSON format
similar_products_json = json.dumps(similar_products2, indent=4)

# Print the JSON data
print(similar_products_json)
