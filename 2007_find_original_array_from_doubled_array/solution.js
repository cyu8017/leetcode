// LeetCode 2007 - Find Original Array From Doubled Array
// https://leetcode.com/problems/find-original-array-from-doubled-array/

/**
 * @param {number[]} changed
 * @return {number[]}
 */
var findOriginalArray = function(changed) {
    if (changed.length % 2 !== 0) return [];
    changed.sort((a, b) => a - b);
    const freq = new Map();
    for (const x of changed) freq.set(x, (freq.get(x) || 0) + 1);
    const ans = [];
    for (const x of changed) {
        if ((freq.get(x) || 0) === 0) continue;
        freq.set(x, freq.get(x) - 1);
        if ((freq.get(2 * x) || 0) === 0) return [];
        freq.set(2 * x, freq.get(2 * x) - 1);
        ans.push(x);
    }
    return ans;
};
