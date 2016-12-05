from igraph import *
import igraph

karateGraph = igraph.Graph.Read_GraphML('karate.GraphML')
karateGraph.vs["label"] = range(34)

visual_style = {}
visual_style["edge_curved"] = False
visual_style["vertex_color"] = "#95D2CB"
visual_style["vertex_size"] = 25
visual_style["vertex_label_size"] = 15

plot(karateGraph, "karateClubGraph.png", **visual_style)

visual_style1 = {}
visual_style1["edge_curved"] = False
visual_style1["vertex_size"] = 25
visual_style1["vertex_label_size"] = 15

girvanNewmanCommunity = karateGraph.community_edge_betweenness().as_clustering(n=2);
print "No of community = {}".format(girvanNewmanCommunity.cluster_graph().vcount())
print "Modularity of communities detected by Girvan-Newman Algorithm on the Karate club network =  {}".format(girvanNewmanCommunity.modularity)
plot(girvanNewmanCommunity, "GirvanNewmanOnKarateClubNetwork.png", **visual_style1) #returns a dendrogram object

louvainCommunity = karateGraph.community_multilevel()
print "No of community = {}".format(louvainCommunity.cluster_graph().vcount())
print "Modularity of communities detected by Louvain Algorithm on the Karate club network =  {}".format(louvainCommunity.modularity)
plot(louvainCommunity, "LouvainOnKarateClubNetwork.png", **visual_style1)

fastGreedyCommunity = karateGraph.community_fastgreedy().as_clustering(n=2)
print "No of community = {}".format(fastGreedyCommunity.cluster_graph().vcount())
print "Modularity of communities detected by Fast-greedy Algorithm on the Karate club network =  {}".format(fastGreedyCommunity.modularity)
plot(fastGreedyCommunity, "FastGreedyOnKarateClubNetwork.png", **visual_style1) #returns a dendrogram object

randomWalkCommunity = karateGraph.community_walktrap().as_clustering(n=2)
print "No of community = {}".format(randomWalkCommunity.cluster_graph().vcount())
print "Modularity of communities detected by Random walk Algorithm on the Karate club network =  {}".format(randomWalkCommunity.modularity)
plot(randomWalkCommunity, "RandomWalkOnKarateClubNetwork.png", **visual_style1) # returns a dondrogram object

labelPropagationCommunity = karateGraph.community_label_propagation()
print "No of community = {}".format(labelPropagationCommunity.cluster_graph().vcount())
print "Modularity of communities detected by Label Propagation Algorithm on the Karate club network =  {}".format(labelPropagationCommunity.modularity)
plot(labelPropagationCommunity, "LabelPropagationOnKarateClubNetwork.png", **visual_style1)