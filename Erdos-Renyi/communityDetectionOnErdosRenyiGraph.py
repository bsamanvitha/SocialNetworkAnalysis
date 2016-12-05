import igraph


graph = igraph.Graph.Erdos_Renyi(300, 0.04)
#graph.vs["label"] = range(500)

visual_style = {}
visual_style["edge_curved"] = False
visual_style["vertex_color"] = "#95D2CB"
visual_style["vertex_size"] = 15
visual_style["vertex_label_size"] = 12

#igraph.summary(graph)
igraph.plot(graph,"erdosRenyiNetwork.png", **visual_style)

visual_style1 = {}
visual_style1["edge_curved"] = False
visual_style1["vertex_size"] = 15
visual_style1["vertex_label_size"] = 12

#print(communities)
louvainCommunity = graph.community_multilevel()
#print louvainCommunity
print "No of community = {}".format(louvainCommunity.cluster_graph().vcount())
print "Modularity of communities detected by Louvain Algorithm on the Erdos-Renyi graph =  {}".format(louvainCommunity.modularity)
igraph.plot(louvainCommunity, "LouvainOnErdosRenyi.png", **visual_style1)

girvanNewmanCommunity = graph.community_edge_betweenness().as_clustering()
#print girvanNewmanCommunity
print "No of community = {}".format(girvanNewmanCommunity.cluster_graph().vcount())
print "Modularity of communities detected by Girvan-Newman Algorithm on the Erdos-Renyi graph =  {}".format(girvanNewmanCommunity.modularity)
igraph.plot(girvanNewmanCommunity, "GirvanNewmanOnErdosRenyi.png", **visual_style1)

labelPropagationCommunity = graph.community_label_propagation()
#print labelPropagationCommunity
print "No of community = {}".format(labelPropagationCommunity.cluster_graph().vcount())
print "Modularity of communities detected by Label Propagation Algorithm on the Erdos-Renyi graph =  {}".format(labelPropagationCommunity.modularity)
igraph.plot(labelPropagationCommunity, "LabelPropagationOnErdosRenyi.png", **visual_style1)

fastGreedyCommunity = graph.community_fastgreedy().as_clustering()
#print fastGreedyCommunity
print "No of community = {}".format(fastGreedyCommunity.cluster_graph().vcount())
print "Modularity of communities detected by Fast-greedy Algorithm on the Erdos-Renyi graph =  {}".format(fastGreedyCommunity.modularity)
igraph.plot(fastGreedyCommunity, "FastGreedyOnErdosRenyi.png", **visual_style1)

randomWalkCommunity = graph.community_walktrap().as_clustering()
#print randomWalkCommunity
print "No of community = {}".format(randomWalkCommunity.cluster_graph().vcount())
print "Modularity of communities detected by Random walk Algorithm on the Erdos-Renyi graph =  {}".format(randomWalkCommunity.modularity)
igraph.plot(randomWalkCommunity, "RandomWalkOnErdosRenyi.png", **visual_style1)