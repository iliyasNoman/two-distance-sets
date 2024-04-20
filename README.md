.py scripts:

AB_codes_to_edgelist - takes a string of the letters 'a' and 'b' used to encode graphs in some papers and outputs the edgelist 
graphsFail1bitNot2 - enumerates the graphs that pass condition 1 from the paper and fail condition 2 (about the spectrum)
graphsEmbedInR4 - tests the hypothesis that the ones that fail 2 but not 1 are the ones that embed in a smaller dimension
number_of_small_spherical - finds the number of small spherical 2-distance sets
randomMatirxRatio - finds the ratio of the small spherical 2-distance sets to all small two distance sets 
testingEigenvects - uses the data from some files with matrices and tests some things about their eigenvectors
TestsOnSpherical - another one that tests some things about the eigenvects but specifically for spherical graphs

.txt files:

outputX.txt where X is a number is a file with the adjacency matrices of the nonisomorphic graphs with X vertices

.npy files:
saves an array of some adjacency matrices of graphs that satisfy some property
