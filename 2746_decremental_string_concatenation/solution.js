// LeetCode 2746 - Decremental String Concatenation
// https://leetcode.com/problems/decremental-string-concatenation/

/**
 * @param {string[]} words
 * @return {number}
 */
var minimizeConcatenatedLength = function(words) {
    const n = words.length;
    const memo = new Map();
    const w0 = words[0];
    const dfs = (i, first, last) => {
        if (i === n) return 0;
        const key = i + ',' + first + ',' + last;
        if (memo.has(key)) return memo.get(key);
        const w = words[i];
        const wf = w[0], wl = w[w.length - 1];
        const add1 = w.length - (last === wf ? 1 : 0);
        const add2 = w.length - (wl === first ? 1 : 0);
        const a = add1 + dfs(i + 1, first, wl);
        const b = add2 + dfs(i + 1, wf, last);
        const ans = Math.min(a, b);
        memo.set(key, ans);
        return ans;
    };
    return w0.length + dfs(1, w0[0], w0[w0.length - 1]);
};
