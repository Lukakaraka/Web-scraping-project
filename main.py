from bs4 import BeautifulSoup
import requests
import pandas as pd

# Request link to the website
site = requests.get('https://content.codecademy.com/courses/beautifulsoup/cacao/index.html')

soup = BeautifulSoup(site.content, "html.parser")

# taking all elements with a class called "Rating"
ratings = soup.find_all(attrs = {'class': 'Rating'})

# A list where we will store only the text from the elements with a class called "Rating"
real_ratings = []
# A function that adds text to the real_ratings list
for rating in ratings[1:]:
  real_ratings.append(rating.get_text())

# taking all elements with a class called "Company"
company_names = soup.find_all(attrs = {'class': 'Company'})

# A list where we will store only the text from the elements with a class called "Rating"
real_company_names = []
# A function that adds text to the real_company_names list
for i in company_names[1:]:
  real_company_names.append(i.get_text())

# A dataframe that can be used for multiple purposes
d = {'Company': real_company_names, 'Rating': real_ratings}
dataframe = pd.DataFrame.from_dict(d)


# You can then convert it to a csv file using this command:
# dataframe.to_csv(r'C:\Users\Korisnik\Desktop\export_dataframe.csv', index = False, header=True)
