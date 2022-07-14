# Analyzing Shipping orders for an ecommerce store
### Using Snowflake and python-connector

Snowflake delivers the Data Cloud — a global network where thousands of organizations mobilize data with near-unlimited scale, concurrency, and performance. Inside the Data Cloud, organizations unite their siloed data, easily discover and securely share governed data, and execute diverse analytic workloads. Snowflake’s platform allows for data warehousing, data lakes, data engineering, data science, data application development, and data sharing. 

In this project I used python-connector loacally to connect to snowflake. I then created a warehouse, database, and schema to upload store data into. This data is from an ecommerce store listing various variables related to customer orders. The steps:

1. Download python connector and configure it to connect to snowflakes' latest version
2. Create the warehouse
3. Create the database
4. Create schema
5. Create a table
6. Populate the table with order data
7. Data exploration
8. Run queries for visualizations
9. Create a dashboard


## Using python connector and connecting to snowflake
I accomplished this locally by running the following scripts on python IDLE shell:

![alt text](https://github.com/Zi-Stonga/Snowflake/blob/main/Images/python_script.JPG)


###Phython Script

## Snowflake
Snowflake is a great data platform as it allows organizations to handle megadata in the cloud, making data engineering, collaboration and data analysis easy to accomplish. I created a database, created a schema, and created a table to populate with my ecommerce data. Below is a preview of the data:



![alt text](https://github.com/Zi-Stonga/Snowflake/blob/main/Images/Data_preview.JPG)

###Data Preview

## Creating Visualizations
Snowflake allows users to create basic visualizations of their data. While you can configure snowflake to work with Tableau, I find it useful to be able to create visualization right on the platform. Below are some visualization I created of the ecommerce data using the snowflake platform.

![alt text](https://github.com/Zi-Stonga/Snowflake/blob/main/Images/Sales,region.JPG)

### Sales per Region


![alt text](https://github.com/Zi-Stonga/Snowflake/blob/main/Images/sales,region,shipmode.JPG)

### Sales per Region, with shipping mode


![alt text](https://github.com/Zi-Stonga/Snowflake/blob/main/Images/Sales,shipmode.JPG)

### Sales by shipping mode

![alt text](https://github.com/Zi-Stonga/Snowflake/blob/main/Images/Shipmode,Segment.JPG)

### Sales by shipping mode, with segment(Consumer, Corporate, Home Office)

![alt text](https://github.com/Zi-Stonga/Snowflake/blob/main/Images/Shipmode,Sales,region.JPG)


### Sales per Region, with shipping mode




## Creating a dashboard
Working with snowflake and analyzing this data was a great way to experience some of Snowflake's capabilities. I put together a dashboard of some of the graphs I produced from the data to get a visual representation.

![alt text](https://github.com/Zi-Stonga/Snowflake/blob/main/Images/dashboard2.JPG)

## Sentiments
I found snowflake to be a great data platform. It's user intuitive and you can accomplish a great deal on just the platform alone without much configuration or intergraton.




