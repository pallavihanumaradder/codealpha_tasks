import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Book Analytics Dashboard", layout="wide")
st.title("📚 CodeAlpha Data Analytics Dashboard")

# 1. Load the dataset
df = pd.read_csv("books_dataset.csv")
df['Price'] = df['Price'].str.replace('£', '').astype(float)

# 2. Add Sidebar Filter
st.sidebar.header("Filter Options")
max_price_filter = st.sidebar.slider(
    "Select Maximum Book Price (£)", 
    min_value=float(df['Price'].min()), 
    max_value=float(df['Price'].max()), 
    value=float(df['Price'].max())
)

filtered_df = df[df['Price'] <= max_price_filter]

# 3. Summary Cards
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Books Available", len(filtered_df))
with col2:
    st.metric("Average Book Price", f"£{filtered_df['Price'].mean():.2f}")
with col3:
    st.metric("Highest Book Price", f"£{filtered_df['Price'].max():.2f}")

# 4. Display Data Table
st.subheader("📊 Filtered Book Dataset")
st.dataframe(filtered_df, use_container_width=True)

# 5. Render Chart
st.subheader("📈 Price Distribution Analysis")
fig, ax = plt.subplots(figsize=(10, 4))
sns.histplot(filtered_df['Price'], kde=True, color='teal', ax=ax)
ax.set_xlabel("Price (£)")
ax.set_ylabel("Count")
st.pyplot(fig)
