import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Your dataset
payments = pd.DataFrame({
    'Name': [
        'Payer 1',
        'Payer 2',
        'Payer 3',
        'Payer 4',
        'Payer 5',
        'Payer 6',
        'Payer 7',
        'Payer 8',
        'Payer 9',
        'Payer 10',
        'Payer 11',
        'Payer 12',
        'Payer 13',
        'Payer 14',
        'Payer 15',
        'Payer 16',
        'Payer 17',
        'Payer 18',
        'Payer 19',
        'Payer 20',
        'Payer 21',
        'Payer 22',
        'Payer 23',
        'Payer 24',
        'Payer 25',
        'Payer 26',
        'Payer 27',
        'Payer 28',
        'Payer 29',
        'Payer 30',
        'Payer 31',
        'Payer 32',
        'Payer 33',
        'Payer 34',
        'Payer 35',
        'Payer 36',
        'Payer 37',
        'Payer 38',
        'Payer 39',
        'Payer 40',
        'Payer 41',
        'Payer 42',
        'Payer 43',
        'Payer 44',
        'Payer 45',
        'Payer 46',
        'Payer 47',
        'Payer 48',
        'Payer 49',
        'Payer 50',
        'Payer 51',
        'Payer 52',
        'Payer 53',
        'Payer 54',
        'Payer 55',
        'Payer 56',
        'Payer 57',
        'Payer 58',
        'Payer 59',
        'Payer 60',
        'Payer 61',
        'Payer 62',
        'Payer 63',
        'Payer 64',
        'Payer 65',
        'Payer 66',
        'Payer 67',
        'Payer 68',
        'Payer 69',
        'Payer 70',
        'Payer 71',
        'Payer 72',
        'Payer 73',
        'Payer 74',
        'Payer 75',
        'Payer 76',
        'Payer 77',
        'Payer 78',
        'Payer 79',
        'Payer 80',
        'Payer 81',
        'Payer 82',
        'Payer 83',
        'Payer 84',
        'Payer 85',
        'Payer 86',
        'Payer 87',
        'Payer 88',
        'Payer 89',
        'Payer 90',
        'Payer 91',
        'Payer 92',
        'Payer 93',
        'Payer 94',
        'Payer 95',
        'Payer 96',
        'Payer 97',
        'Payer 98',
        'Payer 99',
        'Payer 100'
    ],
    'Amount': [
        1450000,
        1100000,
        700000,
        50000,
        200000,
        106000,
        250000,
        200000,
        200000,
        210000,
        200000,
        100000,
        100000,
        100000,
        250000,
        50000,
        150000,
        60000,
        600000,
        100000,
        100000,
        50000,
        100000,
        500000,
        100000,
        100000,
        60000,
        100000,
        200000,
        103000,
        50000,
        200000,
        10000,
        50000,
        102000,
        10000,
        30000,
        20000,
        50000,
        100000,
        50000,
        200000,
        100000,
        30000,
        60000,
        100000,
        10000,
        40000,
        350000,
        300000,
        30000,
        20000,
        50000,
        10000,
        20000,
        100000,
        500000,
        100000,
        80000,
        100000,
        20000,
        10000,
        100000,
        100000,
        25000,
        100000,
        100000,
        20000,
        200000,
        20000,
        10000,
        10000,
        20000,
        100000,
        10000,
        10000,
        100000,
        20000,
        100000,
        20000,
        20000,
        10000,
        50000,
        20000,
        25000,
        100000,
        20000,
        20000,
        60000,
        50000,
        50000,
        25000,
        10000,
        50000,
        10000,
        20000,
        10000,
        50000,
        50000,
        100000
    ]
})

# Sort data in descending order by amount
payments = payments.sort_values(by='Amount', ascending=False)

# Calculate cumulative sum and percentage
payments['Cumulative Sum'] = payments['Amount'].cumsum()
payments['Percentage'] = (payments['Amount'] / payments['Amount'].sum()) * 100

# Create Streamlit app
st.title("Interactive Payments Visualization")

# Sunburst Chart
st.subheader("Sunburst Chart")
fig = px.sunburst(
    payments,
    path=['Name'],
    values='Amount',
    color='Amount',
    color_continuous_scale='RdBu',
    title="Payment Sunburst by Individual"
)

# Customizing the sunburst chart for better visualization
fig.update_traces(textinfo="label+percent entry")
fig.update_layout(margin=dict(t=50, l=0, r=0, b=0))

st.plotly_chart(fig, use_container_width=True)

# Interactive Data Table
st.header("Payments Data")
st.dataframe(payments[['Name', 'Amount', 'Percentage']])

# Interactive Filter
st.header("Filter Payments")
threshold = st.slider("Select a payment threshold (in ₦)", 0, int(payments['Amount'].max()), 100000, step=10000)
filtered_data = payments[payments['Amount'] >= threshold]

# Display the total amount for the filtered data
total_filtered_amount = filtered_data['Amount'].sum()
st.write(f"Total amount for payments above ₦{threshold:,}: ₦{total_filtered_amount:,}")

# Pie Chart of Filtered Data
st.header("Distribution of Filtered Payments")
fig_pie = px.pie(filtered_data, values='Amount', names='Name', title=f"Distribution of Payments Above ₦{threshold:,}")
st.plotly_chart(fig_pie)

# Additional Interactive Features
# Interactive Insights
st.header("Payment Insights")
st.write(f"Total number of contributors: {len(payments)}")
st.write(f"Total amount collected: ₦{payments['Amount'].sum():,}")

# Individual Contributions
st.header("Individual Contributions")
selected_contributor = st.selectbox("Select a contributor to view details:", payments['Name'].unique())
contributor_info = payments[payments['Name'] == selected_contributor]
st.write(f"Contribution by {selected_contributor}: ₦{contributor_info['Amount'].values[0]:,}")
st.write(f"Percentage Contribution: {contributor_info['Percentage'].values[0]:.2f}%")

# Aggregate Statistics
st.header("Aggregate Statistics")
st.write(f"Average Contribution: ₦{payments['Amount'].mean():,.2f}")
st.write(f"Median Contribution: ₦{payments['Amount'].median():,.2f}")
st.write(f"Standard Deviation: ₦{payments['Amount'].std():,.2f}")

# Top Contributors
st.header("Top 5 Contributors")
top_contributors = payments.nlargest(5, 'Amount')
st.dataframe(top_contributors[['Name', 'Amount', 'Percentage']])

# Pareto Chart
st.title('Pareto 80/20 Rule')

fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.bar(range(len(payments)), payments['Amount'], color=['#4CAF50' if i < 10 else '#6495ED' for i in range(len(payments))])
ax1.set_xlabel('Payment Item', fontsize=12)
ax1.set_ylabel('Amount (₦)', fontsize=12)
ax1.set_title('Pareto Chart of Collections', fontsize=14, fontweight='bold')

ax2 = ax1.twinx()
ax2.plot(range(len(payments)), payments['Percentage'].cumsum(), color='#FF0000', marker='o')
ax2.set_ylabel('Cumulative Percentage (%)', color='#FF0000', fontsize=12)
ax2.tick_params('y', colors='#FF0000')

plt.xticks(range(len(payments)), [f'Item {i+1}' for i in range(len(payments))], rotation=90, fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

st.pyplot(fig)

# Analysis of the top 10 payment items and the remaining 40 payment items
top_10_amount = payments['Amount'].iloc[:10].sum()
remaining_40_amount = payments['Amount'].iloc[10:].sum()

st.write(f"The top 10 payment items (20% of the total) account for approximately ₦{top_10_amount:,.0f}, which is around 80% of the total payments collected.")
st.write(f"The remaining 40 payment items (80% of the total) make up the remaining ₦{remaining_40_amount:,.0f}, which is around 20% of the total payments.")