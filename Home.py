import streamlit as st

st.set_page_config(
    page_title="BRIDGE",
    page_icon="🌉",
)

st.title("BRIDGE 🌉")
st.markdown("# Your BRIDGE to better SALES !")
st.markdown("Are you ready to take your sales and customer service skills to the next level? Look no further! Our cutting-edge Roleplay Bot is here to transform you into a customer service and sales superstar.")

st.markdown("## Experience the Future of Learning")
st.markdown("Our Roleplay Bot is not your ordinary training program. It's your virtual coach, your supportive mentor, and your secret weapon for mastering the art of sales and customer service through immersive roleplay. With three difficulty levels to choose from, you can tailor your training to your unique needs and challenge yourself to grow.")

# centered button
col1, col2, col3 , col4, col5 = st.columns(5)
with col3 :
    center_button = st.link_button('Get started!', type='primary', url='/Signup', use_container_width=True)