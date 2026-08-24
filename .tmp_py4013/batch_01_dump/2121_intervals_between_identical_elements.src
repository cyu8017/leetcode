// LeetCode 2121 - Intervals Between Identical Elements
// https://leetcode.com/problems/intervals-between-identical-elements/

/**
 * @param {number[]} arr
 * @return {number[]}
 */
var getDistances = function(arr) {
    const n = arr.length;
    const pos = new Map();
    for (let i = 0; i < n; i++) {
        if (!pos.has(arr[i])) pos.set(arr[i], []);
        pos.get(arr[i]).push(i);
    }
    const ans = new Array(n).fill(0);
    for (const idxs of pos.values()) {
        const m = idxs.length;
        const pref = new Array(m + 1).fill(0);
        for (let i = 0; i < m; i++) pref[i + 1] = pref[i] + idxs[i];
        for (let i = 0; i < m; i++) {
            const left = i * idxs[i] - pref[i];
            const right = (pref[m] - pref[i + 1]) - (m - i - 1) * idxs[i];
            ans[idxs[i]] = left + right;
        }
    }
    return ans;
};
