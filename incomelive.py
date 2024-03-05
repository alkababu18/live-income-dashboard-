import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px

# Set up Streamlit page
st.set_page_config(
    page_title='Live Data Dashboard',
    page_icon='📊',
    layout='wide'
)
st.title('Live Data Dashboard')

# Load dataset
df = pd.read_csv('incomedata.csv')

# Widget to choose job
job_filter = st.selectbox('Choose a job', df['occupation'].unique(), index=2)

# Filter DataFrame based on selected job
filtered_df = df[df['occupation'] == job_filter].copy()

# Perform calculations or data manipulation
filtered_df['new_age'] = filtered_df['age'] * np.random.choice(range(1, 5))
filtered_df['whpw_new'] = filtered_df['hours.per.week'] * np.random.choice(range(1, 5))

avg_age = np.mean(filtered_df['new_age'])
count_married = int(filtered_df[filtered_df['marital.status'] == 'married-civ-spouse']['marital.status'].count() + np.random.choice(range(1, 30)))
hpw = np.mean(filtered_df['whpw_new'])

# Display filtered DataFrame
st.write(filtered_df)

# Display KPIs or metrics
st.metric(label='Average Age', value=round(avg_age), delta=round(avg_age) - 10)
st.metric(label='Married Count', value=int(round(count_married)), delta=10 + count_married)
st.metric(label='Working Hours/Week', value=round(hpw), delta=round(count_married / hpw) / 8)

# Create two columns for charts
fig_col1, fig_col2 = st.columns(2)

with fig_col1:
    st.markdown("### Age vs marital.status")
    fig_age_marital = px.density_heatmap(data_frame=filtered_df, y='new_age', x='marital.status', histfunc='count', nbinsx=20, nbinsy=20)
    fig_age_marital.update_layout(yaxis_title='Age', xaxis_title='marital.status')
    st.plotly_chart(fig_age_marital)

with fig_col2:
    st.markdown('### Age Count')
    fig2 = px.histogram(data_frame=filtered_df, x='new_age').update_layout(xaxis_title='Age')
    st.plotly_chart(fig2)
    st.markdown('### Data View as per Selection')
    st.dataframe(filtered_df)
time.sleep(1)