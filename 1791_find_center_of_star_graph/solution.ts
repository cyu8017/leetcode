// LeetCode 1791 - Find Center of Star Graph
// https://leetcode.com/problems/find-center-of-star-graph/

function findCenter(edges: number[][]): number {
    const [a, b] = edges[0];
    const [c, d] = edges[1];
    return (a === c || a === d) ? a : b;
}
