





## Attribute Information:






Hello to all, this is my first github experience :) Hope you enjoy and benefit from it.
# Association Rule Learning Recommender
<p align="center">
  
<img src="https://miro.medium.com/max/300/1*z5zToUtprDu4Dz6_DLDIKA.jpeg" >  
      
</p>

## Table of contents
* [General info](#general-info)
* [Dataset info](#dataset-info)
* [Project info](#project-info)
* [Technologies](#technologies)
* [Setup](#setup)


## General info
We have given a set of transactions, we try to aim find rules that will predict the occurrence of an item, based on the occurrences of other items in the transaction. In short, this is a daily situation like when we buy a laptop from any shopping site, the site instantly recommends us a laptop bag. We use apriori algorithm and association rules which are support, lift and confidence.

## Dataset info
Name: Online Retail II  
Link: https://archive.ics.uci.edu/ml/machine-learning-databases/00502/   
You can download it from the link, it is bigger than 25MB, therefore couldn't upload here.

It is a real online retail transaction data of a UK-based online store between 01/12/2009 and 09/12/2011.
The product catalog of this company includes souvenirs. They can also be considered as promotional items.
There is also information that most of its customers are wholesalers.

**InvoiceNo:** Invoice number. Nominal. A 6-digit integral number uniquely assigned to each transaction. If this code starts with the letter 'c', it indicates a cancellation.

**StockCode:** Product (item) code. Nominal. A 5-digit integral number uniquely assigned to each distinct product.

**Description:** Product (item) name. Nominal.

**Quantity:** The quantities of each product (item) per transaction. Numeric.

**InvoiceDate:** Invice date and time. Numeric. The day and time when a transaction was generated.

**UnitPrice:** Unit price. Numeric. Product price per unit in sterling (Â£).

**CustomerID:** Customer number. Nominal. A 5-digit integral number uniquely assigned to each customer.

**Country:** Country name. Nominal. The name of the country where a customer resides.


<p align="center">
<img src="https://predictivehacks.com/wp-content/uploads/2020/07/mba-1-1024x376.png" width="500px"> 
</p>


## Project info
Here,we tried to make the most suitable product suggestion for the cart information of 3 different users.
We derived the decision rules from customers from 2010-2011 Germany. Also, product recommendations can be 1 or more than 1.
For example, we can guess information on purchasing behavior like “If someone buys chips and pringles, then is likely to buy cola with high probability“

## Technologies
Project is created with:
* PyCharm: 2021.3 
* Pandas: 1.3.4 
* mlextend: 0.19.0 (especially apriori, association_rules)

	
## Setup
To run this project, just run the functions call "arl_recommender". That's it!











