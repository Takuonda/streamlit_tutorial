import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Intro of streamlit')

df = pd.DataFrame({
    '1column': [1, 2, 3, 4],
    '2column': [10, 20, 30, 40]
})

#dataframeは引数設定が可能、writeは出来ない、tableはstaticな表示でsortが出来ない（width設定も不可）
st.write('DataFrame')
st.dataframe(df.style.highlight_max(axis=0), width=500, height=300)
st.write('Write')
st.write(df.style.highlight_max(axis=0), width=500, height=300)
st.write('Table')
st.table(df.style.highlight_max(axis=0))

st.write('MarkDown')
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.write('Line_chart')
st.line_chart(df)

st.write('Area_chart')
st.area_chart(df)

st.write('Bar_chart')
st.bar_chart(df)

#新宿周辺の緯度経度をマップで表示
df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70], #新宿周辺の緯度経度情報
    columns=['lat', 'lon']
)
st.write('Map')
st.map(df)

st.write('Interactive widgets')
st.write('Image')
if st.checkbox('Show Image'):
    img = Image.open('sample.JPG')
    st.image(img, caption='Taku Onda', use_column_width=True)


'Select box'
option = st.selectbox(
    'What is your favorite number?',
    list(range(1,11)),
)

'Your favorite number is', option, '!'

'Text box'
text = st.text_input('What do you like to do in your free time?')
'Your hobby is', text, '!'

'Slider'
condition = st.slider('What is your energy percentage?', 0, 100, 50)
'Condition:', condition

st.write('Input from side bar')
st.sidebar.write('Side bar')
text_sidebar = st.sidebar.text_input('What do you like to do in your free time?', key='text_sidebar')
condition_sidebar = st.sidebar.slider('What is your energy percentage?', 0, 100, 50, key='condition_sidebar')

'Your hobby is', text_sidebar, '!'
'Condition:', condition_sidebar

'Column and Button'
left_column, right_column = st.columns(2)
button = left_column.button('Show text on right column')
if button:
    right_column.write('This is right column')
    
'Expander'
expander = st.expander('Contact')
expander.write('Write here')

'Progress bar'
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)
    
'Done!!!'