// LeetCode 2509 - Cycle Length Queries in a Tree
// https://leetcode.com/problems/cycle-length-queries-in-a-tree/

/**
 * @param {number} n
 * @param {number[][]} queries
 * @return {number[]}
 */
var cycleLengthQueries = function(n, queries) {
    const ans = Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        let a = queries[i][0], b = queries[i][1], steps = 0;
        while (a !== b) {
            if (a > b) a = Math.floor(a / 2);
            else b = Math.floor(b / 2);
            steps++;
        }
        ans[i] = steps + 1;
    }
    return ans;
};
