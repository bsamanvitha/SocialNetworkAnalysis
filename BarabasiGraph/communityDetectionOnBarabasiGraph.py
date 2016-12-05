import igraph
import operator

graph = igraph.Graph.Barabasi(1000, 1)
print "No of nodes = {}".format(graph.vcount())
print "No of edges = {}".format(graph.ecount())
print "Diameter = {}".format(graph.diameter(directed=False))

clusteringCoefficientsList = graph.transitivity_local_undirected(vertices=None)
#print clusteringCoefficientsList  
list1 = sorted(range(len(clusteringCoefficientsList)), key=lambda i: clusteringCoefficientsList[i])[-5:]
print "Five nodes with the highest clustering coefficients are {}, {}, {}, {}, {}".format(list1[0], list1[1], list1[2], list1[3], list1[4])

vertexBetweennessList = graph.betweenness(vertices=None, directed=False)
#print vertexBetweennessList
list2 = sorted(range(len(vertexBetweennessList)), key=lambda i: vertexBetweennessList[i])[-5:]   
print "Five nodes with the highest vertex betweenness are {}, {}, {}, {}, {}".format(list2[0], list2[1], list2[2], list2[3], list2[4])


visual_style = {}
visual_style["edge_curved"] = False
visual_style["vertex_color"] = "#95D2CB"
visual_style["vertex_size"] = 10
visual_style["vertex_label_size"] = 5

#igraph.summary(graph)
igraph.plot(graph,"barabasiGraph.png", **visual_style)

visual_style1 = {}
visual_style1["edge_curved"] = False
visual_style1["vertex_size"] = 10
visual_style1["vertex_label_size"] = 5


#print(communities)
louvainCommunity = graph.community_multilevel()
#print louvainCommunity
print "No of community = {}".format(louvainCommunity.cluster_graph().vcount())
print "Modularity of communities detected by Louvain Algorithm on the Albert-Barabasi model =  {}".format(louvainCommunity.modularity)
igraph.plot(louvainCommunity, "LouvainOnBarabasi.png", **visual_style1)

girvanNewmanCommunity = graph.community_edge_betweenness().as_clustering()
#print girvanNewmanCommunity
print "No of community = {}".format(girvanNewmanCommunity.cluster_graph().vcount())
print "Modularity of communities detected by Girvan-Newman Algorithm on the Albert-Barabasi model  =  {}".format(girvanNewmanCommunity.modularity)
igraph.plot(girvanNewmanCommunity, "GirvanNewmanOnBarabasi.png", **visual_style1)

labelPropagationCommunity = graph.community_label_propagation()
#print labelPropagationCommunity
print "No of community = {}".format(labelPropagationCommunity.cluster_graph().vcount())
print "Modularity of communities detected by Label Propagation Algorithm on the Albert-Barabasi model =  {}".format(labelPropagationCommunity.modularity)
igraph.plot(labelPropagationCommunity, "LabelPropagationOnBarabasi.png", **visual_style1)

fastGreedyCommunity = graph.community_fastgreedy().as_clustering()
#print fastGreedyCommunity
print "No of community = {}".format(fastGreedyCommunity.cluster_graph().vcount())
print "Modularity of communities detected by Fast-greedy Algorithm on the Albert-Barabasi model =  {}".format(fastGreedyCommunity.modularity)
igraph.plot(fastGreedyCommunity, "FastGreedyOnBarabasi.png", **visual_style1)

randomWalkCommunity = graph.community_walktrap().as_clustering()
#print randomWalkCommunity
print "No of community = {}".format(randomWalkCommunity.cluster_graph().vcount())
print "Modularity of communities detected by Random walk Algorithm on the Albert-Barabasi model =  {}".format(randomWalkCommunity.modularity)
igraph.plot(randomWalkCommunity, "RandomWalkOnBarabasi.png", **visual_style1)