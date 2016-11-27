import igraph


graph = igraph.Graph.Barabasi(100, 2)

#igraph.summary(graph)
igraph.plot(graph,"barabasi.png")

#print(communities)
louvainCommunity = graph.community_multilevel()
igraph.plot(louvainCommunity, "LouvainOnBarabasi.png")

girvanNewmanCommunity = graph.community_edge_betweenness()
igraph.plot(girvanNewmanCommunity.as_clustering(), "GirvanNewmanOnBarabasi.png")

labelPropagationCommunity = graph.community_label_propagation()
igraph.plot(labelPropagationCommunity, "LabelPropagationOnBarabasi.png")

fastGreedyCommunity = graph.community_fastgreedy()
igraph.plot(fastGreedyCommunity.as_clustering(), "FastGreedyOnBarabasi.png")

randomWalkCommunity = graph.community_walktrap()
igraph.plot(randomWalkCommunity.as_clustering(), "RandomWalkOnBarabasi.png")