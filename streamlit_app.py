import streamlit
import pandas

streamlit.title('I love animals!')
streamlit.header('Especially Cats! π»')
streamlit.text('No offence to dogs tho, nor snakes. Not elephants for that matter πΆππ')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

selected = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index), ['Avocado', 'Apple'])

my_fruit_list = my_fruit_list.loc[selected]

streamlit.dataframe(my_fruit_list)
