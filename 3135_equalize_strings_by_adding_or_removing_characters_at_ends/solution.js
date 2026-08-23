// LeetCode 3135 - Equalize Strings by Adding or Removing Characters at Ends
// https://leetcode.com/problems/equalize-strings-by-adding-or-removing-characters-at-ends/

/**
 * @param {string} initial
 * @param {string} target
 * @return {number}
 */
var minOperations = function(initial, target) {
    const m = initial.length, n = target.length;
    const f = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
    let mx = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (initial[i] === target[j]) {
                f[i + 1][j + 1] = f[i][j] + 1;
                mx = Math.max(mx, f[i + 1][j + 1]);
            }
        }
    }
    return m + n - 2 * mx;
};
