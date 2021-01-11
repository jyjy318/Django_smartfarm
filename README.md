# Services for operating small-scale in-house smart farms

This service is a service developed to help those who run small smart farms in their homes.<br/>
I used image recognition technology using MobileNet, and the service was developed based on an inference model.<br/>
The following is a flow chart of the service.<br/>

![서비스 흐름도1](https://user-images.githubusercontent.com/66713459/104153835-b8273600-5426-11eb-8e69-dddc914f1a4d.png) <br/>
![서비스 흐름도2](https://user-images.githubusercontent.com/66713459/104153844-be1d1700-5426-11eb-9857-ec13e07ce0b2.png) <br/>

----------------------------------------------------

Full functionality is as follows: <br/>
![hw sw 구성도](https://user-images.githubusercontent.com/66713459/104155739-27068e00-542b-11eb-98c7-e9b6f5f00015.png) <br/>
||Contents|Explanation|
|:---:|:---:|:---:|
|SW|Collecting data for train and test|Image crawling for crops to be classified and direct collection of necessary data|
|SW|Data learning through deep learning|Crawling and learning directly collected image data through MobileNet|
|SW|Web application UI configuration|Develope service by using Bootstrap and Django|
|SW|Build a database server|Build an AWS EC2 database server|
|SW|Raspberry Pi and database linkage|Transfer the measured temperature and humidity of the house to the database|
|HW|Understanding user environment using Raspberry Pi|Measuring temperature and humidity at home using IoT equipment|
----------------------------------------------------
The actual screen used is as follows. <br/>
It uses Django, an open source web application framework written in Python. <br/>
![실제화면](https://user-images.githubusercontent.com/66713459/104155742-28d05180-542b-11eb-9fb7-b97882a516d5.png) <br/>
This service is useful when growing early crops. I am developing services such as condition recognition and problem recognition of crops, and I will follow up when the development is completed.
