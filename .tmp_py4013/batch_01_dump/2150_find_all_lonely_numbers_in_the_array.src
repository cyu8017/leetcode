// LeetCode 2150 - Find All Lonely Numbers in the Array
// https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findLonely = function(nums) {
    const freq = new Map();
    for (const x of nums) freq.set(x, (freq.get(x) || 0) + 1);
    const ans = [];
    for (const [k, v] of freq)
        if (v === 1 && !freq.has(k - 1) && !freq.has(k + 1))
            ans.push(k);
    return ans;
};
