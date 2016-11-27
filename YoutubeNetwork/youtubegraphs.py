from igraph import *
import igraph

youtubeGraph = Graph.Read_Ncol('youtube.txt')
plot(youtubeGraph, "1original.png")
plot(youtubeGraph.community_edge_betweenness().as_clustering(), "2girvanNewman.png")
plot(youtubeGraph.community_multilevel(), "3louvainMethod.png")
plot(youtubeGraph.community_fastgreedy().as_clustering(), "4fastGreedy.png")
plot(youtubeGraph.community_walktrap().as_clustering(), "5randomWalks.png")
plot(youtubeGraph.community_label_propagation(), "6labelPropagation.png")