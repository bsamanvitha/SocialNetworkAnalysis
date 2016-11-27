from igraph import *
import igraph

karateGraph = igraph.read('karate.GraphML', format = 'graphml')

visual_style = {}
visual_style["vertex_size"] = 10

plot(karateGraph, "1original.png", **visual_style)
plot(karateGraph.community_edge_betweenness().as_clustering(), "2girvanNewman.png", **visual_style)
plot(karateGraph.community_multilevel(), "3louvainMethod.png", **visual_style)
plot(karateGraph.community_fastgreedy().as_clustering(), "4fastGreedy.png", **visual_style)
plot(karateGraph.community_walktrap().as_clustering(), "5randomWalks.png", **visual_style)
plot(karateGraph.community_label_propagation(), "6labelPropagation.png", **visual_style)
