import networkx as nx
import matplotlib.pyplot as plt

# Construct a heterogeneous graph using NetworkX
G = nx.Graph()

# Add patient nodes
G.add_node("P1", node_type="patient")
G.add_node("P2", node_type="patient")
G.add_node("P3", node_type="patient")

# Add visit nodes
G.add_node("V1", node_type="visit")
G.add_node("V2", node_type="visit")
G.add_node("V3", node_type="visit")  # 替换 V4 为 V3

# Add diagnosis nodes
G.add_node("Diag1", node_type="diagnosis")
G.add_node("Diag2", node_type="diagnosis")
G.add_node("Diag3", node_type="diagnosis")
G.add_node("Diag4", node_type="diagnosis")
G.add_node("Diag5", node_type="diagnosis")

# Add lab event node
G.add_node("Labevent", node_type="labevent")

# Add edges between nodes
G.add_edge("P1", "V1")
G.add_edge("P1", "V2")
G.add_edge("P2", "Labevent")  # P2 is now connected to Labevent instead of V3
G.add_edge("P3", "V3")  # 替换 V4 为 V3
G.add_edge("V1", "Diag1")
G.add_edge("V1", "Diag2")
G.add_edge("V1", "Diag5")
G.add_edge("V2", "Diag3")
G.add_edge("V3", "Diag5")  # 替换 V4 为 V3
G.add_edge("V3", "Diag4")  # 替换 V4 为 V3
G.add_edge("Labevent", "Diag4")  # Labevent is now connected where V3 was

# Set node attributes for better visualization
node_colors = {"patient": "lightblue", "visit": "lightgreen", "diagnosis": "pink", "labevent": "orange"}
colors = [node_colors[G.nodes[n]["node_type"]] for n in G.nodes]

# Draw the graph using matplotlib
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=600)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, width=3)

# Save the graph to a file
plt.axis('off')
plt.savefig("graph_with_v3.png")  # 保存图形到当前目录下的 graph_with_v3.png 文件
plt.close()  # 关闭图形，避免内存泄漏
print(1)

# Optional: Show the graph (if you want to display it as well)
# plt.show()