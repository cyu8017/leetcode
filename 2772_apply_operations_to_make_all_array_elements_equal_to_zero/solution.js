// LeetCode 2772 - Apply Operations to Make All Array Elements Equal to Zero
// https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var checkArray = function(nums, k) {
    const n = nums.length;
    const diff = Array(n + 1).fill(0);
    let cur = 0;
    for (let i = 0; i < n; i++) {
        cur += diff[i];
        const need = nums[i] - cur;
        if (need < 0) return false;
        if (need > 0) {
            if (i + k > n) return false;
            cur += need;
            diff[i + k] -= need;
        }
    }
    return true;
};
