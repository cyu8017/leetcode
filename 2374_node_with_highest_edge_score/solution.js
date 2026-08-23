// LeetCode 2374 - Node With Highest Edge Score
// https://leetcode.com/problems/node-with-highest-edge-score/

/**
 * @param {number[]} edges
 * @return {number}
 */
var edgeScore = function(edges) {
    const n = edges.length;
    const score = Array(n).fill(0);
    for (let i = 0; i < n; i++) score[edges[i]] += i;
    let ans = 0;
    for (let i = 1; i < n; i++)
        if (score[i] > score[ans]) ans = i;
    return ans;
};
