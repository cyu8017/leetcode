// LeetCode 2107 - Number of Unique Flavors After Sharing K Candies
// https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/

/**
 * @param {number[]} candies
 * @param {number} k
 * @return {number}
 */
var shareCandies = function(candies, k) {
    const n = candies.length;
    const freq = new Map();
    for (const c of candies) freq.set(c, (freq.get(c) || 0) + 1);
    if (k === 0) return freq.size;
    for (let i = 0; i < k; i++) {
        const c = candies[i];
        const v = freq.get(c) - 1;
        if (v === 0) freq.delete(c); else freq.set(c, v);
    }
    let ans = freq.size;
    for (let i = k; i < n; i++) {
        freq.set(candies[i - k], (freq.get(candies[i - k]) || 0) + 1);
        const c = candies[i];
        const v = freq.get(c) - 1;
        if (v === 0) freq.delete(c); else freq.set(c, v);
        ans = Math.max(ans, freq.size);
    }
    return ans;
};
