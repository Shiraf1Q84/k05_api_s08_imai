import folium
from streamlit_folium import folium_static
import streamlit as st
import pandas as pd

# サンプル用の緯度経度データを作成
sales_office = pd.DataFrame(
    data=[[32.0, 131.1], [33.1, 131.2], [34.2, 131.3]],
    index=["本社", "A営業所", "B営業所"],
    columns=["latitude", "longitude"]
)

# 地図上に拠点のマーカーと円を追加する関数
def add_area_marker(df, map_obj, radius):
    for index, row in df.iterrows():
        # マーカーを追加
        folium.Marker(
            location=[row.latitude, row.longitude],
            popup=index,
        ).add_to(map_obj)

        # 半径を示す円を追加
        folium.Circle(
            radius=radius * 1000,
            location=[row.latitude, row.longitude],
            popup=index,
            color="yellow",
            fill=True,
            fill_opacity=0.07
        ).add_to(map_obj)

# Streamlitの画面設定
st.title("サンプル地図")
radius = st.slider('拠点を中心とした円の半径（km）', value=40, min_value=5, max_value=50)
st.subheader(f"各拠点からの距離：{radius}km")

# Foliumで地図を初期化
map_obj = folium.Map(location=[33.1, 131.0], zoom_start=7)

# データを地図に追加
add_area_marker(sales_office, map_obj, radius)

# 地図をStreamlitに表示
folium_static(map_obj)
