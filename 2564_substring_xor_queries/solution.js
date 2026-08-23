// LeetCode 2564 - Substring XOR Queries
// https://leetcode.com/problems/substring-xor-queries/

/**
 * @param {string} s
 * @param {number[][]} queries
 * @return {number[][]}
 */
var substringXorQueries = function(s, queries) {
    const pos = new Map();
    const n = s.length;
    for (let i = 0; i < n; ++i) {
        if (s[i] === '0') {
            if (!pos.has(0)) pos.set(0, [i, i]);
            continue;
        }
        let val = 0;
        for (let j = i; j < n && j < i + 30; ++j) {
            val = val * 2 + (s.charCodeAt(j) - 48);
            if (!pos.has(val)) pos.set(val, [i, j]);
        }
    }
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; ++i) {
        const need = queries[i][0] ^ queries[i][1];
        ans[i] = pos.has(need) ? pos.get(need).slice() : [-1, -1];
    }
    return ans;
};
