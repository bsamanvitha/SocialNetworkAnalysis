import igraph


graph = igraph.Graph.Erdos_Renyi(50, 0.2)

#igraph.summary(graph)
igraph.plot(graph,"erdosRenyi.png")

#print(communities)
louvainCommunity = graph.community_multilevel()
igraph.plot(louvainCommunity, "LouvainOnErdosRenyi.png")

girvanNewmanCommunity = graph.community_edge_betweenness()
igraph.plot(girvanNewmanCommunity.as_clustering(), "GirvanNewmanOnErdosRenyi.png")

labelPropagationCommunity = graph.community_label_propagation()
igraph.plot(labelPropagationCommunity, "LabelPropagationOnErdosRenyi.png")

fastGreedyCommunity = graph.community_fastgreedy()
igraph.plot(fastGreedyCommunity.as_clustering(), "FastGreedyOnErdosRenyi.png")

randomWalkCommunity = graph.community_walktrap()
igraph.plot(randomWalkCommunity.as_clustering(), "RandomWalkOnErdosRenyi.png")