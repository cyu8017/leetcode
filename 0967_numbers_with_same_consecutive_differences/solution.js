// LeetCode 0967 - Numbers With Same Consecutive Differences
// https://leetcode.com/problems/numbers-with-same-consecutive-differences/

/**
 * @param {number} n
 * @param {number} k
 * @return {number[]}
 */
var numsSameConsecDiff = function(n, k) {
    const ans = [];
    const dfs = (num, length) => {
        if (length === n) {
            ans.push(num);
            return;
        }
        const last = num % 10;
        const nexts = new Set([last + k, last - k]);
        for (const nxt of nexts) {
            if (nxt >= 0 && nxt <= 9) dfs(num * 10 + nxt, length + 1);
        }
    };
    for (let start = 1; start <= 9; start++) dfs(start, 1);
    return ans;
};
