import igraph

graph = igraph.Graph.Read_Edgelist('0.edges', directed=False)

visual_style = {}
visual_style["edge_curved"] = False
visual_style["vertex_color"] = "#AC0045"
visual_style["vertex_size"] = 10

visual_style["bbox"] = (1500,1500)
visual_style["margin"] = 100

igraph.plot(graph, "facebookNetwork.png", **visual_style)

visual_style1 = {}
visual_style1["edge_curved"] = False
visual_style1["vertex_size"] = 12

visual_style1["bbox"] = (1500,1500)
visual_style1["margin"] = 100

louvainCommunity = graph.community_multilevel()
igraph.plot(louvainCommunity, "LouvainOnFacebook.png", **visual_style1)

girvanNewmanCommunity = graph.community_edge_betweenness()
igraph.plot(girvanNewmanCommunity.as_clustering(), "GirvanNewmanOnFacebook.png", **visual_style1)

labelPropagationCommunity = graph.community_label_propagation()
igraph.plot(labelPropagationCommunity, "LabelPropagationOnFacebook.png", **visual_style)

#fastGreedyCommunity = graph.community_fastgreedy()
#igraph.plot(fastGreedyCommunity.as_clustering(), "FastGreedyOnFacebook.png", **visual_style1)

randomWalkCommunity = graph.community_walktrap()
igraph.plot(randomWalkCommunity.as_clustering(), "RandomWalkOnFacebook.png", **visual_style1)
