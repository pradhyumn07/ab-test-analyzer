import streamlit as st
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest
import seaborn as sns
import matplotlib.pyplot as plt

st.title("🧪 A/B Test Results Analyzer")

uploaded_file = st.file_uploader("Upload your CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("📄 Raw Data Preview")
    st.dataframe(df.head())

    group_A = df[df['group'] == 'A']
    group_B = df[df['group'] == 'B']

    conv_A = group_A['converted'].mean()
    conv_B = group_B['converted'].mean()

    st.markdown(f"**Conversion Rate A:** {conv_A:.2%}  \n**Conversion Rate B:** {conv_B:.2%}")

    success = [group_A['converted'].sum(), group_B['converted'].sum()]
    nobs = [len(group_A), len(group_B)]

    z_stat, p_val = proportions_ztest(success, nobs)

    st.markdown(f"**Z-Statistic:** {z_stat:.3f}  \n**P-Value:** {p_val:.4f}")

    alpha = 0.05
    if p_val < alpha:
        st.success("✅ Statistically significant difference found.")
        st.info("Group B performed better." if conv_B > conv_A else "Group A performed better.")
    else:
        st.warning("❌ No statistically significant difference found.")

    # Plot
    plot_data = pd.DataFrame({
        'Group': ['A', 'B'],
        'Conversion Rate': [conv_A, conv_B]
    })

    st.subheader("📊 Conversion Rate Comparison")
    sns.set(style='whitegrid')
    fig, ax = plt.subplots()
    sns.barplot(x='Group', y='Conversion Rate', data=plot_data, palette='pastel', ax=ax)
    ax.set_ylim(0, 1)
    st.pyplot(fig)
