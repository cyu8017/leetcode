// LeetCode 2908 - Minimum Sum of Mountain Triplets I
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/

/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumSum = function(nums) {
    const n = nums.length;
    let ans = 1 << 30;
    for (let j = 1; j < n - 1; j++) {
        let left = 1 << 30, right = 1 << 30;
        for (let i = 0; i < j; i++)
            if (nums[i] < nums[j] && nums[i] < left) left = nums[i];
        for (let k = j + 1; k < n; k++)
            if (nums[k] < nums[j] && nums[k] < right) right = nums[k];
        if (left < (1 << 30) && right < (1 << 30)) {
            const cand = left + nums[j] + right;
            if (cand < ans) ans = cand;
        }
    }
    return ans === (1 << 30) ? -1 : ans;
};
