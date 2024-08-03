import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="BTC - The Beat Coin Tokenomics", layout="wide")

st.title("BTC: The Beat Coin Tokenomics")
st.subheader("Powered by Mminer Technology")

st.write("""
BTC (The Beat Coin) is the native cryptocurrency of the Mminer ecosystem, 
which revolutionizes the music industry by combining blockchain technology with music streaming and engagement.
""")

st.header("Proof of Work: The Mminer Way")

st.write("""
The Mminer ecosystem introduces a unique 'Proof of Play' mechanism, which is an evolution of the traditional Proof of Work:

1. **Music Playback as Work**: Each song play counts as 'work' in the system.
2. **Audio Fingerprinting**: Ensures the validity of each play.
3. **Engagement Metrics**: User interactions boost the 'work' value.
4. **Rarity Multiplier**: Less popular songs have higher work value.
5. **Hardware Contribution**: Traditional mining hardware secures the network.
6. **Hybrid Block Creation**: Combines musical engagement and computational work.
7. **Network Validation**: Nodes verify both proof of play and computational work.
""")

st.header("BTC Tokenomics: 100 Billion Total Supply")

# Define the tokenomics data
tokenomics_data = {
    'Category': ['Mining Rewards', 'Artist and Content Creator Pool', 'Listener Rewards', 
                 'Development Fund', 'Ecosystem Growth Fund', 'Liquidity Provision', 
                 'Community Governance'],
    'Allocation (Billion BTC)': [40, 25, 15, 10, 5, 3, 2],
    'Percentage': [40, 25, 15, 10, 5, 3, 2]
}

df = pd.DataFrame(tokenomics_data)

# Create a pie chart using matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
ax.pie(df['Allocation (Billion BTC)'], labels=df['Category'], autopct='%1.1f%%', startangle=90)
ax.axis('equal')
plt.title('BTC Token Distribution')
st.pyplot(fig)

# Display the tokenomics breakdown
st.table(df)

st.header("Tokenomics Breakdown Explanation")

st.write("""
1. **Mining Rewards (40%)**: Distributed to miners (both listeners and hardware operators) over time.
2. **Artist and Content Creator Pool (25%)**: Allocated to artists based on play counts and engagement.
3. **Listener Rewards (15%)**: Incentives for active listeners and platform engagement.
4. **Development Fund (10%)**: Reserved for ongoing platform development and improvements.
5. **Ecosystem Growth Fund (5%)**: Used for partnerships, marketing, and ecosystem expansion.
6. **Liquidity Provision (3%)**: Allocated to ensure trading liquidity on exchanges.
7. **Community Governance (2%)**: Distributed to BTC holders for voting on platform decisions.
""")

st.header("Key Benefits of BTC Tokenomics")

st.write("""
- Balanced distribution incentivizing all participants in the ecosystem
- Self-sustaining model rewarding participation and music discovery
- Fair compensation for artists
- Encourages long-term holding and community participation
- Transparency through smart contract governance
- Fine-grained transactions and rewards with 100 billion total supply
- Long-term sustainability and growth focus
""")

st.header("Get Involved")

st.write("""
Join the Mminer ecosystem and be part of the future of music and blockchain technology!
Start earning BTC by listening to your favorite tunes, supporting artists, and contributing to the network.
""")

# Add a call-to-action button
if st.button("Learn More About Mminer"):
    st.write("Thank you for your interest! Visit our website for more information on how to get started with Mminer and BTC.")