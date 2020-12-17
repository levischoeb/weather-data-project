Web scraping Weather Data with Python

In this project we scraped weather data from st gallen to get a forecast of the next seven days. We ran the code on IDLE with Python version 3.9.0 on our Mac OS 11.0.1. Running the code with a different Python GUI or a different version Python / OS might cause errors. 

Suggested Procedure:

To run the code you need to go through the following steps:
1. Open terminal on your mac to install requests, pandas and BeautifulSoup bs4. requests allows you to get the data from the web server. pandas is a      DataFrame which allows you to store tabular data to make data analysis easier. BeautifulSoup bs4 helps you to filter data based on HTML tags.

2. To install the packages first you need to install pip by entering: 

   sudo easy_install pip

3. Afterwards you install the packages one after another on your terminal: 

   pip3 install requests
   
   pip3 install pandas 
   
   pip3 install bs4
   
 Code Explanation:
First the before installed packages need to be imported to the program. Then you get the data from the chosen website with requests and parse it with BeautifulSoup. Then we create a list to hold the extracted data. In a next step we had to get rid of the data we didn't want to extract by finding the right class in the developer tools of the website. We created a loop to pick the relevent weather information of each day by choosing their position in the created list. For every category we first extracted the text an then removed unwanted characters such as spaces and sections by replacing them with no space. The maximum and minimum temperature needed to be split so we could display them individually. Additionaly we created a dictionary to name each category and added this dictionary to our list. With panda we created a frame for our extracted data on our list. At the end we printed our dataframe which displays the weather forecast from the chosen website.


