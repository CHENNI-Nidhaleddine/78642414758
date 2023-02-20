
import subprocess
import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
import time
import numpy as np
from utils import *

def semi_sync_lpa_s(G, max_iter=100, choice = "random"):
  """
    Implementation of Semi-Synchronous Label Propagation algorithm for community detection in Python.
    
    Args:
    G: A NetworkX graph object.
    max_iter: Maximum number of iterations for the algorithm (default: 100).
    choice: In case of equal frequency, what criteria to use for choosing a new label (default: random)
    options: ["random", "lpa-prec", "lpa-max", "lpa-prec-max"]
    
    Returns:
    A dictionary with nodes as keys and their respective list of communities/labels as values.
  """

  # Phase 0: Initialization phase
  nodes = list(G.nodes())
  labels = dict(zip(nodes, range(len(nodes))))
  old_labels = labels.copy()
  iteration = 0
  history = [labels.copy()]
  # PHASE 1: Coloring phase 
  colors = nx.greedy_color(G)
  # Initialize an empty dictionary to store the nodes for each color
  color_dict = {}
  for color in set(colors.values()):
    color_dict[color] = []

  # Add the nodes to the corresponding color lists
  for node, color in colors.items():
    color_dict[color].append(node)
  
  # PHASE 2: Propagation phase
  while (iteration<=max_iter):
    iteration +=1
    for j in range(len(color_dict)):
      # This loop can be parallelized
      for node in color_dict[j]:
        label_freq = {}
        for neighbor in G.neighbors(node):
          neighbor_label = labels[neighbor]
          if neighbor_label in label_freq:
            label_freq[neighbor_label] += 1
          else:
            label_freq[neighbor_label] = 1
          
          # Assign the label with the highest frequency to the node
          max_freq = max(label_freq.values())
          max_labels = [label for label, freq in label_freq.items() if freq == max_freq]
          # Case equal freq choose randomly
          if choice == "random":
            new_label = np.random.choice(max_labels)
          elif choice == "lpa-prec":
            if labels[node] in max_labels:
              new_label = labels[node]
            else:
              new_label = np.random.choice(max_labels)
          elif choice == "lpa-max":
            new_label = np.max(max_labels)
          elif choice == "lpa-prec-max":
            if labels[node] in max_labels:
              new_label = labels[node]
            else:
              new_label = np.max(max_labels)
          labels[node] = new_label

    history.append(labels.copy())

    # Checking stability or convergence
    if labels == old_labels:
      break
    old_labels = labels
  
  return history

def draw_graph(graph_option):
    g = get_graph(graph_option)
    fig = plt.figure()
    start_time = time.time()
    partitions = semi_sync_lpa_s(g, choice=choice)
    st.write("Temps d'exécution :  %.4f secondes " % (time.time() - start_time))
    modularity_scores = [calculate_modularity(g, partition, weight="weights") for partition in partitions]
    st.write(f"Nombre d'itération: {len(partitions)}")

    st.write(f"**Modularity: %.4f**" % (modularity_scores[-1]))            
    nx.draw(g, community_layout(g, partitions[-1]), node_color=list(partitions[-1].values()), with_labels = True)
    st.pyplot(fig=fig, clear_figure=True)



st.title("Algorithme de SS-LPA")

graph_option = st.selectbox("Choisir un graphe", ("Karate Club", "Dolphins", "Football", "Polbooks","Synthetiques"))
choice = st.selectbox("choisir la stratégie de résolution d'égalité", options=["random", "lpa-prec", "lpa-max", "lpa-prec-max"])

def run_benchmark():
        command = f'benchmark -N {n} -k {k} -maxk {maxk} -mu {mu} -minc {minc} -maxc {maxc}'
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

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
    st.button('Run benchmark', on_click=run_benchmark)
button1 = st.button("Simuler")

if button1:
    draw_graph(graph_option)

