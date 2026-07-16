// LeetCode 0087 - Scramble String
// https://leetcode.com/problems/scramble-string/

/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var isScramble = function(s1, s2) {
    const memo = new Map();

    var dfs = function(a, b) {
        const key = a + '#' + b;
        if (memo.has(key)) {
            return memo.get(key);
        }
        if (a === b) {
            memo.set(key, true);
            return true;
        }
        if ([...a].sort().join('') !== [...b].sort().join('')) {
            memo.set(key, false);
            return false;
        }

        const n = a.length;
        for (let i = 1; i < n; i++) {
            if (dfs(a.slice(0, i), b.slice(0, i)) && dfs(a.slice(i), b.slice(i))) {
                memo.set(key, true);
                return true;
            }
            if (dfs(a.slice(0, i), b.slice(n - i)) && dfs(a.slice(i), b.slice(0, n - i))) {
                memo.set(key, true);
                return true;
            }
        }
        memo.set(key, false);
        return false;
    };

    return dfs(s1, s2);
};
