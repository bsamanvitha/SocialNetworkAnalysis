from igraph import *
import igraph

karateGraph = igraph.read('karate.GraphML', format = 'graphml')
plot(karateGraph, "1original.png")
plot(karateGraph.community_edge_betweenness().as_clustering(), "2girvanNewman.png")
plot(karateGraph.community_multilevel(), "3louvainMethod.png")
plot(karateGraph.community_fastgreedy().as_clustering(), "4fastGreedy.png")
plot(karateGraph.community_walktrap().as_clustering(), "5randomWalks.png")
plot(karateGraph.community_label_propagation(), "6labelPropagation.png")
