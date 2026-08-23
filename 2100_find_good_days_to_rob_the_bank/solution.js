// LeetCode 2100 - Find Good Days to Rob the Bank
// https://leetcode.com/problems/find-good-days-to-rob-the-bank/

/**
 * @param {number[]} security
 * @param {number} time
 * @return {number[]}
 */
var goodDaysToRobBank = function(security, time) {
    const n = security.length;
    if (time === 0) return Array.from({length: n}, (_, i) => i);
    const left = new Array(n).fill(0), right = new Array(n).fill(0);
    for (let i = 1; i < n; i++) if (security[i] <= security[i - 1]) left[i] = left[i - 1] + 1;
    for (let i = n - 2; i >= 0; i--) if (security[i] <= security[i + 1]) right[i] = right[i + 1] + 1;
    const ans = [];
    for (let i = time; i < n - time; i++)
        if (left[i] >= time && right[i] >= time) ans.push(i);
    return ans;
};
