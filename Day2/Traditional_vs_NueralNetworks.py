import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="ML vs Neural Networks Comparison",
    page_icon="🤖",
    layout="wide"
)

# Main title
st.title("🤖 Traditional ML vs Neural Networks Comparison")
st.markdown("---")

# Create comparison data
comparison_data = {
    "Aspect": [
        "Learning Approach",
        "Data Requirements",
        "Feature Engineering",
        "Interpretability",
        "Training Time",
        "Computational Resources",
        "Performance on Small Data",
        "Performance on Large Data",
        "Overfitting Tendency",
        "Implementation Complexity",
        "Domain Expertise Required",
        "Handling Raw Data",
        "Memory Usage",
        "Real-time Inference",
        "Maintenance",
        "Cost",
        "Debugging Difficulty",
        "Scalability",
        "Transfer Learning",
        "Hardware Requirements"
    ],
    "Traditional ML": [
        "Rule-based, statistical patterns",
        "Works well with small to medium datasets",
        "Manual feature extraction required",
        "High - easy to understand decisions",
        "Fast training (minutes to hours)",
        "Low computational requirements",
        "Excellent performance",
        "Limited by feature engineering",
        "Lower risk with proper techniques",
        "Relatively simple",
        "High - domain knowledge crucial",
        "Requires preprocessing",
        "Low memory usage",
        "Very fast inference",
        "Easy to maintain and update",
        "Low cost",
        "Easy to debug and troubleshoot",
        "Limited scalability",
        "Not applicable",
        "Standard CPU sufficient"
    ],
    "Neural Networks": [
        "Learns complex patterns automatically",
        "Requires large datasets for best results",
        "Automatic feature learning",
        "Low - black box nature",
        "Slow training (hours to days)",
        "High computational requirements (GPU)",
        "May overfit or underperform",
        "Excellent with sufficient data",
        "Higher risk without regularization",
        "Complex architecture design",
        "Medium - more automated",
        "Can process raw data directly",
        "High memory usage",
        "Fast inference (after training)",
        "Complex debugging and updates",
        "High cost (hardware, energy)",
        "Difficult to debug",
        "Highly scalable",
        "Excellent transfer learning",
        "GPU/TPU recommended"
    ]
}

# Create DataFrame
df = pd.DataFrame(comparison_data)

# Display the comparison table with enhanced styling
st.subheader("📊 Detailed Comparison Table")

# Add some styling to make it more readable
st.markdown("""
<style>
.dataframe {
    font-size: 14px;
}
.dataframe th {
    background-color: #f0f2f6;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Display table - compatible with all Streamlit versions
st.dataframe(df)

# Alternative table view with better formatting
st.markdown("---")
st.subheader("📋 Alternative Table View")

# Create a more structured table using columns
for i, row in df.iterrows():
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 2])
        with col1:
            st.markdown(f"{row['Aspect']}")
        with col2:
            st.markdown(f"🔵 {row['Traditional ML']}")
        with col3:
            st.markdown(f"🟠 {row['Neural Networks']}")
        st.markdown("---")

# Create two columns for side-by-side comparison
st.subheader("🔍 Side-by-Side Overview")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🎯 Traditional Machine Learning")
    st.info("""
    Strengths:
    ✅ Fast training and inference
    ✅ Works well with small datasets
    ✅ Highly interpretable
    ✅ Low computational cost
    ✅ Easy to debug and maintain
    
    Weaknesses:
    ❌ Manual feature engineering
    ❌ Limited complexity handling
    ❌ Requires domain expertise
    ❌ Poor with raw data
    """)
    
    st.markdown("Common Algorithms:")
    algorithms_traditional = [
        "Linear/Logistic Regression",
        "Decision Trees",
        "Random Forest",
        "Support Vector Machines",
        "Naive Bayes",
        "K-Means Clustering",
        "XGBoost/LightGBM"
    ]
    for algo in algorithms_traditional:
        st.markdown(f"• {algo}")

with col2:
    st.markdown("### 🧠 Neural Networks")
    st.warning("""
    Strengths:
    ✅ Automatic feature learning
    ✅ Handles complex patterns
    ✅ Excellent with large data
    ✅ Works with raw data
    ✅ Transfer learning capable
    
    Weaknesses:
    ❌ Requires large datasets
    ❌ Black box nature
    ❌ High computational cost
    ❌ Difficult to debug
    """)
    
    st.markdown("Common Types:")
    algorithms_nn = [
        "Feedforward Neural Networks",
        "Convolutional Neural Networks (CNN)",
        "Recurrent Neural Networks (RNN)",
        "Long Short-Term Memory (LSTM)",
        "Transformer Networks",
        "Generative Adversarial Networks (GAN)",
        "Autoencoders"
    ]
    for algo in algorithms_nn:
        st.markdown(f"• {algo}")


    

# Footer with key takeaways
st.markdown("---")
st.markdown("""
<div style='background-color: #f0f2f6; padding: 20px; border-radius: 10px; margin: 20px 0;'>
    <h3 style='color: #1f77b4; margin-top: 0;'>🎯 Key Takeaways</h3>
    <ul style='color: #333;'>
        <li><strong>Data Size Matters:</strong> Traditional ML for small data, Neural Networks for large data</li>
        <li><strong>Context is King:</strong> Consider interpretability, resources, and domain requirements</li>
        <li><strong>Start Simple:</strong> Begin with traditional ML, then scale to neural networks if needed</li>
        <li><strong>Hybrid Solutions:</strong> Combine both approaches for optimal results</li>
        <li><strong>Continuous Learning:</strong> Stay updated with both traditional and modern techniques</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("💡 Remember: The best model is the one that solves your specific problem effectively!")