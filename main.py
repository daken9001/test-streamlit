import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.dataframe(df.style.highlight_max(axis=0), width=500, height=200)

#"""
# 章
## 節
### 項

#```python
#import streamlit as st
#import numpy as np
#import pandas as pd
#```
#"""

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.area_chart(df2)


df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50]+[35.69,139.70],
    columns=['lat', 'lon']
)

st.map(df3)

st.write('')
st.write('Display Image and Interractive Widgets')

if st.checkbox('Show Image'):
    img = Image.open('image.jpg')
    st.image(img, caption='koko', use_column_width=True)

option = st.selectbox(
    'Select Number',
    list(range(1,11))
)
'You selected No.',option

#text = st.sidebar.text_input('Do you like...')
#text,' is good!'

#slider = st.sidebar.slider('Your condition', 0, 100, 50)
#slider,'% condition!'

left_column, right_column = st.columns(2)
button = left_column.button('Display Right_Column')
if button:
    right_column.write('Here is Right_Column')

expander1 = st.expander('Question1')
expander1.write('Answer1')
expander2 = st.expander('Question2')
expander2.write('Answer2')

st.write('')
st.write('Progress')
'Start!!!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Interation {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!!!'
