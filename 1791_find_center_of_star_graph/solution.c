// LeetCode 1791 - Find Center of Star Graph
// https://leetcode.com/problems/find-center-of-star-graph/

int findCenter(int** edges, int edgesSize, int* edgesColSize) {
    int a = edges[0][0], b = edges[0][1];
    int c = edges[1][0], d = edges[1][1];
    return (a == c || a == d) ? a : b;
}
