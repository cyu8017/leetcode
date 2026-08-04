// LeetCode 1925 - Count Square Sum Triples
// https://leetcode.com/problems/count-square-sum-triples/

/**
 * @param {number} n
 * @return {number}
 */
var countTriples = function(n) {
    const squares = new Set();
    for (let i = 1; i <= n; i++) squares.add(i * i);
    let ans = 0;
    for (let a = 1; a <= n; a++) {
        for (let b = 1; b <= n; b++) {
            if (squares.has(a * a + b * b)) ans++;
        }
    }
    return ans;
};
