# Analyzing Shipping orders for an ecommerce store
### Using Snowflake and python-connector

Snowflake delivers the Data Cloud — a global network where thousands of organizations mobilize data with near-unlimited scale, concurrency, and performance. Inside the Data Cloud, organizations unite their siloed data, easily discover and securely share governed data, and execute diverse analytic workloads. Snowflake’s platform allows for data warehousing, data lakes, data engineering, data science, data application development, and data sharing. 

In this project I used python-connector loacally to connect to snowflake. I then created a warehouse, database, and schema to upload a dataset from Kaggle. This data ia from an ecommerce site listing various variables related to customer orders. The steps:

1. Download python connector and configure it to connect to snowflakes' latest version
2. Create the warehouse
3. Create the database
4. Create schema
5. Create a table
6. Populate the table with ecommerce data
7. Data exploration
8. Run queries for visualizations
9. Create a dashboard


## Using python connector and connecting to snowflake
I accomplished this locally by running the following scripts on python IDLE shell:

![alt text](https://github.com/Zi-stonga/Snowflake/images/python script.JPG)

## Snowflake
Snowflake is a great data tool as it allows organisations to handle incredibly large datasets in the cloud, making data engineering, collaboration and data analysis easy to accomplish. I created a database, created a schema, and created a table to populate with my ecommerce data. Below is a preview of the data.

![alt text](https://github.com/Zi-stonga/Snowflake/images/Data preview.JPG)

## Creating Visualizations
Snowflake allows users to create basic visualizations of their data. While you can configure snowflake to work with Tableau, I find it useful to be able to create visualization right on the platform. Below are some visualization I created of the ecommerce data right on the snowflake platform.

![alt text](https://github.com/Zi-stonga/Snowflake/images/sales, region, ship mode.JPG)
![alt text](https://github.com/Zi-stonga/Snowflake/images/Sales, region.JPG)
![alt text](https://github.com/Zi-stonga/Snowflake/images/Sales, shipmode.JPG)
![alt text](https://github.com/Zi-stonga/Snowflake/images/Ship mode, Segment.JPG)
![alt text](https://github.com/Zi-stonga/Snowflake/images/Shipmode, Sales, region.JPG)
![alt text](https://github.com/Zi-stonga/Snowflake/images/Shipmode, sales.JPG)

## Creating a dashboard
Working with snowflake and analyzing this small dataset was a great way to experience some of Snowflake's capabilities. I put together a dashboard of some of the graphs I produced from the data to get a visual representations.

![alt text](https://github.com/Zi-stonga/Snowflake/images/dashboard2.JPG)

## Sentiments
I found snowflake to be a great data tool. It's user friendly and you can accomplish a great deal on just the platform alone without much configuration and intergraton.




