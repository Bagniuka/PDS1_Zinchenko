import networkx as nx
import matplotlib.pyplot as pl
from data import cities

def short_path_n_length(graph, c_1, c_2, weight="weight"):
    path = nx.shortest_path(graph, c_1, c_2, weight)
    path_length = nx.shortest_path_length(graph, c_1, c_2, weight)
    return print(f"The shortest way from {c_1} to {c_2}:\n{path}\nIts length: {path_length}km.")

cities_grph = nx.Graph()
for edge in cities:
    cities_grph.add_edge(edge[0], edge[1], weight=int(edge[2]))

pos = nx.spring_layout(cities_grph)
nx.draw(cities_grph, pos)
pl.title("Citie's map")
pl.show()

short_path_n_length(cities_grph, 'Lebedyn', 'Myrhorod', weight="weight")
short_path_n_length(cities_grph, 'Zboriv', 'Yenakiieve', weight="weight")