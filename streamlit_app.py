import streamlit
streamlit.title("My Parents New Healthy Diner")
streamlit.header("Breakfast Favourites")
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#Indico cúal va a ser el índice
my_fruit_list = my_fruit_list.set_index("Fruit")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
# Display the table on the page.
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include
#List selected
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
#we'll ask to use the fruits in our fruits_selected list to pull rows from the full data set (and assign that data to a variable called fruits_to_show)
fruit_to_show = my_fruit_list.loc([fruits_selected])
#display the table on the page
streamlit.dataframe(fruit_to_show)

                    
