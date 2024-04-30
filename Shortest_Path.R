library("igraph")


Relations <- read.table("shortest_path.txt", header=FALSE)  #read ppi file 2 columns

relation_data = data.frame(from= Relations[,1],Relations[,2])

relation_data

biogrid_short=graph.data.frame(relation_data, directed=TRUE, vertices=NULL) #read ppi file as igraph
subgraph1=biogrid_short

paths = get.all.shortest.paths(subgraph1, from=V(subgraph1)['Neuronal acetylcholine receptor subunit alpha-3'], to=V(subgraph1)['Tyrosine-protein phosphatase non-receptor type 16'], mode="out") #shortest path command 

print (paths)
