import streamlit as st
import pandas as pd
import random
import plotly.express as px

# 1. Page Config
st.set_page_config(page_title="Konecranes OTD Optimizer", layout="wide")

# --- 🙅‍♂️ EASTER EGG SECTION 🙅‍♂️ ---
st.markdown(
    """
    <div style="background-color: #5e35b1; padding: 20px; border-radius: 15px; text-align: center; border: 3px solid #ffb300;">
        <h1 style="color: #ffb300; font-family: 'Trebuchet MS', sans-serif; font-weight: bold; margin: 0;">
            🙅‍♂️ WAKANDA FOREVER! 🙅‍♂️
        </h1>
        <p style="color: white; margin-top: 10px; font-size: 1.2rem; font-style: italic;">
            Empowering Konecranes Supply Chain with Vibranium-grade Accuracy
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)
st.balloons() 
# ------------------------------

st.title("🏗️ Konecranes Strategic OTD Framework")
st.write("Optimizing On-Time Delivery (OTD) by accurately classifying root causes.")

# 2. Sidebar Settings
st.sidebar.header("⚙️ Control Panel")
num_orders = st.sidebar.slider("Shipments to Simulate", 50, 1000, 300)
delay_prob = st.sidebar.slider("Delay Probability (%)", 10, 70, 25)
run_btn = st.sidebar.button("🚀 Run Analysis")

# 3. Decision Logic Based on Classification Design [cite: 5-35]
scenarios = [
    {"cat": "Supplier", "event": "Production/Capacity Shortage", "rate": 500, "note": "Goods not ready on time [cite: 16]"},
    {"cat": "Supplier", "event": "Quality Issues / Rework", "rate": 450, "note": "Failed internal QA [cite: 12]"},
    {"cat": "Logistics", "event": "Port Congestion / Connection Missed", "rate": 200, "note": "Delay during transit [cite: 21, 23]"},
    {"cat": "Logistics", "event": "Customs Clearance Issue", "rate": 150, "note": "External logistics factor [cite: 22]"},
    {"cat": "Konecranes", "event": "Late Freight Booking (FCA)", "rate": 250, "note": "Internal planning failure [cite: 31]"},
    {"cat": "Konecranes", "event": "Warehouse Receiving Backlog", "rate": 100, "note": "Internal process delay [cite: 33]"},
    {"cat": "Force Majeure", "event": "Extreme Weather / Act of God", "rate": 0, "note": "Contractual exemption [cite: 24]"}
]

if run_btn:
    data = []
    for i in range(num_orders):
        is_delayed = random.random() < (delay_prob / 100)
        
        if is_delayed:
            s = random.choice(scenarios)
            days = random.randint(1, 15)
            # Comparing Old Default vs New Framework [cite: 72-74]
            data.append({
                "Order ID": f"KC-PO-{7000 + i}",
                "Event": s['event'],
                "Accountable Party": s['cat'],
                "Delay (Days)": days,
                "Penalty ($)": days * s['rate'],
                "Decision Logic": s['note'],
                "Legacy System": "Supplier Delay", # The "Guilty until proven innocent" flaw 
                "New Framework": f"{s['cat']} Delay"
            })
    
    df = pd.DataFrame(data)

    # 4. Dashboard KPIs [cite: 65-69]
    st.header("📊 Performance Comparison")
    k1, k2, k3 = st.columns(3)
    
    total_delayed = len(df)
    actual_supplier_faults = len(df[df['Accountable Party'] == 'Supplier'])
    
    k1.metric("Delayed Orders", total_delayed)
    k2.metric("Legacy Error Count", total_delayed, help="Old system defaults all delays to Supplier ")
    k3.metric("Corrected Error Count", actual_supplier_faults, 
              delta=f"-{total_delayed - actual_supplier_faults} Corrections", delta_color="normal")

    st.markdown("---")

    # 5. Charts
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Root Cause Distribution")
        fig_pie = px.pie(df, names='Accountable Party', color='Accountable Party',
                         color_discrete_map={'Supplier':'#EF553B', 'Logistics':'#636EFA', 'Konecranes':'#00CC96', 'Force Majeure':'#AB63FA'})
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with c2:
        st.subheader("Financial Impact by Party ($)")
        fig_bar = px.bar(df, x='Accountable Party', y='Penalty ($)', color='Accountable Party')
        st.plotly_chart(fig_bar, use_container_width=True)

    # 6. Audit Log
    st.subheader("📋 Detailed Audit Log")
    st.dataframe(df, use_container_width=True)
    
    st.success("💡 System Summary: Transitioning to an evidence-based model prevents unfair penalization  and identifies true process bottlenecks[cite: 68].")
else:
    st.info("👈 Use the sidebar to set parameters and click 'Run Analysis' to see the Wakanda-powered OTD Optimizer in action!")
