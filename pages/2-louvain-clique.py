import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
import time
from utils import *
import networkx.algorithms.community as nx_comm
import subprocess


def draw_graph(graph_option):
    g = get_graph(graph_option)
    fig = plt.figure()
    start_time = time.time()
    partitions = detect_communities(g, randomized=False)
    st.write("Temps d'exécution :  %.4f secondes " % (time.time() - start_time))
    modularity_score = nx_comm.modularity(g, partitions, weight="weight")
    st.write(f"Nombre de partitions: {len(partitions)}")
    st.write(f"Modularité: %.4f" % (modularity_score))

    nx.draw(g, node_color=list(set_to_dict(g, partitions).values()), with_labels = True)
    st.pyplot(fig=fig, clear_figure=True)

st.title("Algorithme de louvain-clique")
graph_option = st.selectbox("Choisir un graphe", ("Karate Club", "Dolphins", "Football", "Polbooks","Synthetiques"))
def run_benchmark():
        command = f'benchmark -N {n} -k {k} -maxk {maxk} -mu {mu} -minc {minc} -maxc {maxc}'
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
# Define function to remove files

if(graph_option=="Synthetiques"):
    # Create input widgets for the parameters
    n =128
    k=16
    maxk=16
    minc=32
    maxc=32
    st.write('Number of nodes is 128')
    st.write('Average degree of each node is 16')
    st.write('Maximum degree of each node is 16')
    st.write('minimum size of each community is 32')
    st.write('maximum size of each community is 32')
    k = 16
    maxk = 16
    mu = st.number_input('mixing parameter of the graph', value=0.1, step=0.01)
    minc = 32
    maxc = 32
    # st.caching.clear_cache()
    st.button('Run benchmark', on_click=run_benchmark)

button1 = st.button("Simuler")
if button1:
    draw_graph(graph_option)