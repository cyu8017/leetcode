// LeetCode 0077 - Combinations
// https://leetcode.com/problems/combinations/

/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
    const result = [];
    const path = [];

    function backtrack(start) {
        if (path.length === k) {
            result.push(path.slice());
            return;
        }

        const remaining = k - path.length;
        for (let i = start; i <= n - remaining + 1; i++) {
            path.push(i);
            backtrack(i + 1);
            path.pop();
        }
    }

    backtrack(1);
    return result;
};
