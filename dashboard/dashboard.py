import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os


st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")
sns.set(style='darkgrid')

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "day.csv")

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    df['dteday'] = pd.to_datetime(df['dteday'])
    df['mnth'] = df['mnth'].map({
        1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
        7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
    })
    df['season'] = df['season'].map({
        1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
    })
    df['yr'] = df['yr'].map({0: 2011, 1: 2012})
    return df

try:
    day_df = load_data(file_path)
except FileNotFoundError:
    st.error(f"File 'day.csv' tidak ditemukan di: {current_dir}")
    st.stop()

import os
import streamlit as st

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "bi.png")

with st.sidebar:
    
    if os.path.exists(image_path):
        st.image(image_path)
    else:
        st.error(f"File gambar tidak ditemukan di: {image_path}")
    
    year_filter = st.selectbox("Pilih Tahun", options=day_df['yr'].unique())
    

    season_list = day_df['season'].unique().tolist()
    season_filter = st.multiselect("Filter Berdasarkan Musim", options=season_list, default=season_list)

main_df = day_df[(day_df["yr"] == year_filter) & (day_df["season"].isin(season_filter))]

st.header('Bike Sharing Analytics Dashboard 🚲')
st.markdown(f"Analisis untuk tahun **{year_filter}** dengan filter musim: **{', '.join(season_filter)}**")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Rentals", value=f"{main_df.cnt.sum():,}")
with col2:
    st.metric("Avg Daily", value=f"{round(main_df.cnt.mean()):,}")
with col3:
    st.metric("Highest Daily", value=f"{main_df.cnt.max():,}")
with col4:
    st.metric("Weather Condition (Avg)", value=f"{main_df.weathersit.mean():.2f}")

st.divider()


tab1, tab2, tab3 = st.tabs(["📈 Tren Bulanan", "🍂 Analisis Musim", "👥 Tren Harian"])

with tab1:
    st.subheader("Monthly Rental Trends")
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.lineplot(x="mnth", y="cnt", data=main_df, marker='o', linewidth=3, color="#2E86C1", ax=ax)
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)

with tab2:
    st.subheader("Visualisasi Berdasarkan Musim")
    col_a, col_b = st.columns(2)
    
    with col_a:
 
        fig, ax = plt.subplots()
        sns.barplot(x="season", y="cnt", data=main_df, estimator=sum, palette="viridis", ax=ax, hue="season", legend=False)
        ax.set_title("Total Penyewaan per Musim")
        st.pyplot(fig)
    
    with col_b:

        fig, ax = plt.subplots()
        sns.scatterplot(x="temp", y="cnt", data=main_df, hue="season", palette="magma", ax=ax)
        ax.set_title("Suhu vs Jumlah Penyewaan")
        st.pyplot(fig)

with tab3:
    st.subheader("Working Day vs Holiday Distribution")
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.boxplot(x="workingday", y="cnt", data=main_df, hue="workingday", palette=["#E74C3C", "#2ECC71"], ax=ax, legend=False)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Holiday/Weekend", "Working Day"])
    st.pyplot(fig)

st.divider()
st.subheader("🔍 Data Explorer")
with st.expander("Klik untuk melihat detail data mentah (Raw Data)"):
    st.dataframe(main_df.sort_values(by="dteday", ascending=False))
    
    csv = main_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Data sebagai CSV",
        data=csv,
        file_name=f'bike_data_{year_filter}.csv',
        mime='text/csv',
    )

st.caption(f'Copyright (c) Bingky - Dicoding Data Science {pd.Timestamp.now().year}')