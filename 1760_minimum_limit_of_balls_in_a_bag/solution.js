// LeetCode 1760 - Minimum Limit of Balls in a Bag
// https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

/**
 * @param {number[]} nums
 * @param {number} maxOperations
 * @return {number}
 */
var minimumSize = function(nums, maxOperations) {
    let lo = 1;
    let hi = Math.max(...nums);
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        let ops = 0;
        for (const x of nums) {
            ops += Math.floor((x - 1) / mid);
        }
        if (ops <= maxOperations) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    return lo;
};
