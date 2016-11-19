from igraph import *
import igraph

karateGraph = igraph.read('karate.GraphML', format = 'graphml')
plot(karateGraph, "1original.png")
plot(karateGraph.community_edge_betweenness(), "2girvanNewman.png") #returns a dendrogram object
plot(karateGraph.community_multilevel(), "3louvainMethod.png")
plot(karateGraph.community_fastgreedy(), "4fastGreedy.png") #returns a dendrogram object
plot(karateGraph.community_walktrap(), "5randomWalks.png") # returns a dondrogram object
plot(karateGraph.community_label_propagation(), "6labelPropagation.png")

