This was a project done for my Software Development Lab at College of Engineering Guindy, Anna University during my final year. All API's and code are valid as of November, 2017.

Gift giving is one of the main reasons for shopping. People are generally very confused in finding what their companions like and hence spend a lot of time in finding the “right” gift for their friends. It is truly a difficult task to choose between millions of possible gifts and narrow it down based on the budget and liking of friends. 

Hence, to recommend suitable gifts, we design a system to suggest gifts fitting the interests and the likes of the user based on their social media profile. The user need only give the profile username of the friend for whom the gift needs to be found.

Among social networking websites, we have chosen Facebook because of its large user database, easy to use API and colossus of information pertaining to an individual.

Research Questions to be answered:
1. Find out common interests of users.
2. List of gifts possible for each user based on their interests specified in Social Media.

Procedure:
1. Scraping general Facebook posts
2. Identifying specific keywords during extraction process to filter posts.
3. Getting features of users like Age, Gender, Pages Liked, Birthdays, etc.
4. Recommendation of Gifts to be given based on comments in which gifts have been mentioned.
Refer Block Diagram and Base Paper in the Documentation_SDL folder for better understanding.


In the folder, "Project Code Repository", the functions of the various code are given below:
Adding Gender to Directory.py - used to get gender of users and add it to the directory folder created for each user.

Amazon_Product_Search.py - Used to search a product by giving a keyword.

books_likes.py - Getting the most liked books and searching it in Google Books API

favorite_athletes.py - Finding the favorite athletes using wikipedia api to find the most liked sport.

favorite_teams.py - Finding the favorite teams using wikipedia api to find the most liked sport.

like_finding.py - finding the likes of the user based on pages liked.

Most_Liked_Sport_Count.py - Counting the likes of the most liked sport by forming a dictionary using the Keywords.csv file

movie_finder.py - Finding similar movies and most liked movies using the TMDB api

music_like_finder.py - Finding the most liked music using PyLyrics

reading_json.py - Used to read the Scraped Json data and writing directories for each user.

Scraping.py - Querying FB using the GRAPH API and getting required data and storing it in the JSON file.

Procedure to run:
1. Run the Scraping.py file to first scrape all relevant data to user.
2. You can run all the other code files in any order to obtain relevant features pertaining to user except the Amazon_Product_Search.py file which is specifically used for querying amazon.
Note: Make sure to install all relevant libraries to run. I used Spyder in Anaconda to code everything.
3. Run Amazon_Product_Search.py file to query Amazon and get relevant products according to search.

In the folder, "Example User Data Extracted", examples of data extracted about my friends on facebook who have allowed Developer access to Facebook's Graph API are given. The name of the folder (if the code is run) is saved as the name of the person about whom the data is extracted. I have named it as "Anonymous" in order not to reveal the true and personal information about my friends. Everything published about them is publicly available in facebook. 

The "Keywords.csv" file is a dictionary made to map and identify different sports which interest users and a simple counting algorithm is used to get the most liked sport of the user.

The probable gifts possible for each user is given in the "probable_gifts.csv" file which will be present in the directory of each user.

All code are run individually as I was testing them one after another but one main program could be easily written to call all the other code in order for simplicity.
