// LeetCode 1679 - Max Number of K-Sum Pairs
// https://leetcode.com/problems/max-number-of-k-sum-pairs/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function(nums, k) {
    const c = new Map();
    let ans = 0;
    for (const x of nums) {
        const need = k - x;
        if (c.get(need) > 0) {
            c.set(need, c.get(need) - 1);
            ans++;
        } else {
            c.set(x, (c.get(x) || 0) + 1);
        }
    }
    return ans;
};
