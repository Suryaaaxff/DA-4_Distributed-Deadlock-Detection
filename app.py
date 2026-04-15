import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from simulation import run_simulation

st.set_page_config(page_title="Deadlock Detection", layout="wide")

# --- STYLE ---
st.markdown("""
<style>
[data-testid="stSidebar"] {display:none;}

.stApp {
    background: #f8fafc;
}

.title {
    font-size: 32px;
    font-weight: 700;
    color: #111827;
}

.section {
    background: white;
    padding: 16px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    margin-bottom: 20px;
}

.small-title {
    font-weight: 600;
    margin-bottom: 10px;
}

.stButton > button {
    background: #2563eb;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown('<div class="title">Distributed Deadlock Detection</div>', unsafe_allow_html=True)

# --- CONTROLS ---
c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    num_sites = st.number_input("Sites", 2, 6, 3)
with c2:
    procs = st.number_input("Processes", 2, 5, 3)
with c3:
    res = st.number_input("Resources", 1, 4, 2)
with c4:
    duration = st.number_input("Duration", 10, 100, 40)
with c5:
    run = st.button("Run")

st.markdown("---")

# --- RUN ---
if run:
    results = run_simulation(
        num_sites=int(num_sites),
        num_processes_per_site=int(procs),
        num_resources_per_site=int(res),
        sim_duration=int(duration)
    )

    log = results["log"]
    G = results["global_wfg"]
    deadlocks = results["detected_deadlocks"]

    # --- RESULT CARD ---
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown("### Deadlock Result")

    if deadlocks:
        st.error("Deadlock Detected")
        for d in deadlocks:
            st.write(" → ".join(d))
    else:
        st.success("No Deadlock")

    st.markdown('</div>', unsafe_allow_html=True)

    # --- GLOBAL GRAPH ---
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown("### Global Wait-For Graph")

    fig, ax = plt.subplots(figsize=(6,4))
    pos = nx.spring_layout(G, seed=42)

    nx.draw(G, pos, with_labels=True, node_color="#3b82f6", node_size=800, ax=ax)
    ax.axis("off")

    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- PER SITE GRAPHS ---
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown("### Local Wait-For Graphs per Site")

    sites = results["all_sites"]

    cols = st.columns(len(sites))

    for i, (sid, site) in enumerate(sites.items()):
        with cols[i]:
            st.markdown(f"**Site {sid}**")

            local_G = nx.DiGraph()
            local_G.add_edges_from(site.wfg.edges())

            fig2, ax2 = plt.subplots(figsize=(4,3))

            if len(local_G.nodes) > 0:
                pos2 = nx.spring_layout(local_G, seed=42)
                nx.draw(local_G, pos2, with_labels=True,
                        node_color="#60a5fa", node_size=700, ax=ax2)
            else:
                ax2.text(0.5, 0.5, "No Data", ha="center")

            ax2.axis("off")
            st.pyplot(fig2)

            # Resource table
            data = []
            for r, holder in site.resources.items():
                data.append({
                    "Resource": f"R{r}",
                    "Holder": f"P{holder}" if holder else "Free"
                })

            df = pd.DataFrame(data)
            st.dataframe(df, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # --- LOG ---
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown("### Event Log")
    df_log = pd.DataFrame([vars(e) for e in log])
    st.dataframe(df_log)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.info("Run the simulation")