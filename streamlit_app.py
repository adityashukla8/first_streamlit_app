import streamlit
import pandas

streamlit.title('I love animals!')
streamlit.header('Especially Cats! 😻')
streamlit.text('No offence to dogs tho, nor snakes. Not elephants for that matter 🐶🐍🐘')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
print(my_fruit_list)
