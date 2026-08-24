// LeetCode 2924 - Find Champion II
// https://leetcode.com/problems/find-champion-ii/

/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var findChampion = function(n, edges) {
    const indeg = Array(n).fill(0);
    for (const e of edges) indeg[e[1]]++;
    let ans = -1;
    for (let i = 0; i < n; i++) {
        if (indeg[i] === 0) {
            if (ans !== -1) return -1;
            ans = i;
        }
    }
    return ans;
};
