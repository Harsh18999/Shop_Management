import streamlit as st

# Initialize connection.
conn = st.connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT PRODUCT_NAME FROM TEST1', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row} has a :{row}:")