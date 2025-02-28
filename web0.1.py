#启动咒语：streamlit run web0.1.py
import streamlit as st

## 侧边栏
with st.sidebar:
    st.title(' _欢迎来到我的世界_ (*^_^*)')
    st.divider()
    st.markdown('这是它的特点：\n- :blue[简单]\n- :red[明了]\n- :green[大气]')


#标签页
st.title('偷得浮生半日闲')
tab1,tab2,tab3,tab4,tab5,tab6= st.tabs(['番剧', '游戏', '书籍','彩蛋','水果猜猜猜','媒体播放器'])

#每个都做折页
with tab1:
    st.info('《葬送的芙莉莲》')
    expander_1 = st.expander('一般路过魔法使')
    expander_1.warning('比心')
    expander_1.image('https://s2.loli.net/2024/01/19/JV52r6QaMhsLoqm.jpg')
    '''
    ```python
    音乐、作画、剧情神中神！2023年度霸权番！
    ```
    '''

with tab2:
    st.info('《博德之门3》')
    expander_2 = st.expander('一般路过提夫林')
    expander_2.warning('看书')
    expander_2.image('https://s2.loli.net/2024/01/19/Jwa8bmST7ZqYvze.png')
    '''
    ```python
    博德之门3。。。你的命中率能不能每次百分百？
    ```
    '''

with tab3:
    st.info('《银河英雄传说》')
    expander_3 = st.expander('一般路过两军对垒')
    expander_3.warning('科幻')
    expander_3.image('https://s2.loli.net/2024/01/19/CqXldP452KEuAHz.png')
    '''
    ```python
    太 空 史 诗
    ```
    '''

with tab4:
    # 折叠页面
    st.info('猜猜我在哪里？')
    expander_4 = st.expander('你是？')
    expander_5 = st.expander('我是？')

    expander_4.warning('不在这里！')
    expander_4.image('https://pica.zhimg.com/80/v2-5e767eeed478fc195d5df472db538640_1440w.png')

    expander_5.warning('也不在这里！')
    expander_5.image('https://pic1.zhimg.com/80/v2-79ba9b4bee266815fb4069a5de5afea7_1440w.png')

with tab5:
    # 按钮
    st.info('猜猜这里有哪些水果')
    fruit_shelter = ['苹果', '梨子', '香蕉', '草莓', '西瓜']
    fruit = st.text_input('输入一个水果名')

    if st.button('找找看'):
        have_it = fruit.lower() in fruit_shelter
        '有这个水果！' if have_it else '没有这个水果哦~'

with tab6:
    #播放器
    st.info('视 频 播 放')
    # 打开视频文件
    video_file = open('web0.1v.mp4', 'rb')
    video_bytes = video_file.read()
    # 使用st.video函数播放视频
    st.video(video_bytes)

    st.divider()

