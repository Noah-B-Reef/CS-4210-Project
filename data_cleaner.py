import sys, gzip
import pandas as pd
import numpy as np
import networkx as nx

# Read in the data
df = pd.read_csv('cisco+secure+workload+networks+of+computing+hosts\Cisco_22_networks\dir_20_graphs\dir_day1\out1_1.txt.gz', compression='gzip', sep="\t", header=None, names=["src", "dst", "weight"], dtype={"src": str, "dst": str, "weight": str})
df.sort_index(inplace=True)

# Replace final column with computed weight

df["weight"] = df["weight"].map(lambda x: len(x.split(","))) # Count the number of communications between the two hosts

# Convert to networkx graph
G = nx.from_pandas_edgelist(df, "src", "dst", ["weight"], create_using=nx.DiGraph())

# Display the graph
# nx.draw(G, with_labels=True)

# Louvain community detection
louvain_communities = nx.community.louvain_communities(G)
print(louvain_communities)
print(df.head())