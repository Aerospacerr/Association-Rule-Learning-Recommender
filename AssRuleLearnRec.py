import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

##### Part 1 #####
#Database setup
df_ = pd.read_excel("/content/online_retail_II.xlsx", sheet_name="Year 2010-2011")
df = df_.copy()
df.info()
df.head()

def outlier_thresholds(dataframe, variable):
    quartile1 = dataframe[variable].quantile(0.01)
    quartile3 = dataframe[variable].quantile(0.99)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit, up_limit

def replace_with_thresholds(dataframe, variable):
    low_limit, up_limit = outlier_thresholds(dataframe, variable)
    dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit

def retail_data_prep(dataframe):
    dataframe.dropna(inplace=True)
    dataframe = dataframe[~dataframe["Invoice"].str.contains("C", na=False)]
    dataframe = dataframe[dataframe["Quantity"] > 0]
    dataframe = dataframe[dataframe["Price"] > 0]
    replace_with_thresholds(dataframe, "Quantity")
    replace_with_thresholds(dataframe, "Price")
    return dataframe

df = retail_data_prep(df)


##### Part 2#####
# Association rules
def create_rules(dataframe, id=True, country="Germany"):
    dataframe = dataframe[dataframe['Country'] == country]
    dataframe = create_invoice_product_df(dataframe, id)
    frequent_itemsets = apriori(dataframe, min_support=0.01, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="support", min_threshold=0.01)
    return rules

def create_invoice_product_df(dataframe, id=False):
    if id:
        return dataframe.groupby(['Invoice', "StockCode"])['Quantity'].sum().unstack().fillna(0). \
            applymap(lambda x: 1 if x > 0 else 0)
    else:
        return dataframe.groupby(['Invoice', 'Description'])['Quantity'].sum().unstack().fillna(0). \
            applymap(lambda x: 1 if x > 0 else 0)

#Let's do it for Germany
df_ger = df[df['Country'] == "Germany"]
rules_ger = create_rules(df_ger)
rules_ger.sort_values("lift", ascending=False).head(50)

#Preparing the ARL Data Structure (Invoice-Product Matrix)
ger_inv_pro_df = create_invoice_product_df(df_ger, id=True)
ger_inv_pro_df.head()


##### Part 3 #####
#ID check for stocks
def check_id(dataframe, stock_code):
    product_name = dataframe[dataframe["StockCode"] == stock_code][["Description"]].values[0].tolist()
    print(product_name)

#We randomly picked those users for example. It can be changed
print(check_id(df_ger, 21987))
print(check_id(df_ger, 23235))
print(check_id(df_ger, 22747))

##### Part 4 #####
#Let's make a product recommendation for users
def arl_recommender(rules_df, product_id, rec_count=1):

    sorted_rules = rules_df.sort_values("lift", ascending=False)

    recommendation_list = []

    for i, product in sorted_rules["antecedents"].items():
        for j in list(product):
            if j == product_id:
                recommendation_list.append(list(sorted_rules.iloc[i]["consequents"]))

    recommendation_list = list({item for item_list in recommendation_list for item in item_list})

    return recommendation_list[:rec_count]

def list_to_int(lists):
  strings = [str(lists) for lists in lists]
  a_string = "". join(strings)
  an_integer = int(a_string)
  return an_integer

#Here is 1. user
rec_1= arl_recommender(rules_ger, 21987, 1)
print(check_id(df_ger, list_to_int(rec_1)))

#Here is 2. user
rec_2= arl_recommender(rules_ger, 23235, 1)
print(check_id(df_ger, list_to_int(rec_2)))

#Here is 3. user
rec_3= arl_recommender(rules_ger, 22747, 1)
print(check_id(df_ger, list_to_int(rec_3)))
