import streamlit as st

# a. 
st.title("Rishav's Streamlit Application")

# b.
st.subheader('This is a simple Streamlit application developed by Rishav.')

# c. 
text_area = st.text_area('Enter some text here')

# d. 
options = ['Data Quality Issues', 'Lack of Relevant Insights', 'Lack of Data', 'Lack of Data Science Skills', 'Lack of Data Engineering Skills', 'Lack of Data Visualization Skills', 'Lack of Data Governance', 'Lack of Data Security', 'Lack of Data Strategy', 'Lack of Data Literacy', 'Lack of Data Culture', 'Lack of Data Infrastructure', 'Lack of Data Tools', 'Lack of Data Science Tools', 'Lack of Data Engineering Tools', 'Lack of Data Visualization Tools', 'Lack of Data Governance Tools', 'Lack of Data Security Tools', 'Lack of Data Strategy Tools', 'Lack of Data Literacy Tools', 'Lack of Data Culture Tools', 'Lack of Data Infrastructure Tools', 'Lack of Data Science Skills', 'Lack of Data Engineering Skills', 'Lack of Data Visualization Skills', 'Lack of Data Governance Skills', 'Lack of Data Security Skills', 'Lack of Data Strategy Skills', 'Lack of Data Literacy Skills', 'Lack of Data Culture Skills', 'Lack of Data Infrastructure Skills']
dropdown = st.selectbox('Choose an option:', options)

# e. 
if st.button('Submit'):
    st.write(f'You submitted: {text_area} and {dropdown}')

# f. 
if st.button('Clear'):
    st.experimental_rerun()

st.image('https://share.ftimg.com/aff/flamingtext/2013/03/06/flamingtext__22860409589509131.jpg', width=500)
st.image('data:image/png;base64,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', width=200)

"""
2. In the Retail industry:
   - Customer Churn Prediction: Predicting whether a customer is likely to stop shopping with a particular retailer. This helps in implementing targeted retention strategies.
   - Demand Forecasting: Predicting the future demand for products based on historical data, aiding in inventory management and supply chain optimization.

3. Additional predictive applications in the Retail industry:
   - Fraud Detection: Identifying potentially fraudulent transactions, such as unauthorized credit card use or false returns, to protect the retail business from financial losses.
   - Price Optimization: Predicting optimal pricing for products based on various factors, maximizing revenue and ensuring competitiveness in the market.

4. More predictive applications in the Retail industry:
   - Inventory Management: Predicting the optimal amount of inventory to hold based on sales forecasts and historical trends.
   - Customer Lifetime Value Prediction: Predicting the net profit attributed to the entire future relationship with a customer.

5. In the Health industry:
   - Disease Diagnosis: Predicting whether a patient has a particular disease based on symptoms, medical history, and diagnostic tests, aiding in early intervention and treatment.
   - Patient Readmission Prediction: Predicting the likelihood of a patient being readmitted to the hospital after discharge, allowing healthcare providers to take preventive measures.

6. Additional predictive applications in the Health industry:
   - Drug Response Prediction: Predicting how patients will respond to a particular medication based on genetic and clinical data, enabling personalized medicine.
   - Length of Stay Prediction: Predicting the expected length of a patient's hospital stay, assisting in resource allocation and better patient care planning.

7. More predictive applications in the Health industry:
   - Epidemic Outbreak Prediction: Using data from various sources to predict the likelihood and spread of disease outbreaks.
   - Mental Health Prediction: Using patient data to predict mental health issues, helping in early detection and treatment.

8. In the Financial Services industry:
   - Credit Scoring: Predicting the creditworthiness of individuals or businesses based on financial history, helping in decision-making for loans and credit approvals.
   - Stock Price Prediction: Forecasting future stock prices based on historical market data and other relevant factors, aiding investors in making informed decisions.

9. Additional predictive applications in the Financial Services industry:
   - Customer Segmentation: Grouping customers based on similar characteristics and behaviors, allowing financial institutions to tailor products and services for different segments.
   - Default Risk Prediction: Predicting the likelihood of a borrower defaulting on a loan, assisting in risk management for lending institutions.

10. More predictive applications in the Financial Services industry:
   - Fraud Detection: Using machine learning algorithms to detect fraudulent transactions and protect against financial crime.
   - Market Basket Analysis: Using predictive analytics to understand the purchase behavior of customers and the relationships between the products that they buy.
"""