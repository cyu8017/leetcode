// LeetCode 2404 - Most Frequent Even Element
// https://leetcode.com/problems/most-frequent-even-element/

/**
 * @param {number[]} nums
 * @return {number}
 */
var mostFrequentEven = function(nums) {
    const cnt = new Map();
    let ans = -1, best = 0;
    for (const x of nums) {
        if (x % 2 !== 0) continue;
        const c = (cnt.get(x) || 0) + 1;
        cnt.set(x, c);
        if (c > best || (c === best && (ans === -1 || x < ans))) {
            best = c;
            ans = x;
        }
    }
    return ans;
};
