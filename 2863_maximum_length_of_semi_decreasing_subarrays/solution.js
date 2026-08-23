// LeetCode 2863 - Maximum Length of Semi-Decreasing Subarrays
// https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubarrayLength = function(nums) {
    const n = nums.length;
    let ans = 0;
    const st = [];
    for (let i = n - 1; i >= 0; i--) {
        if (!st.length || nums[i] > nums[st[st.length - 1]]) st.push(i);
    }
    for (let i = 0; i < n; i++) {
        while (st.length && nums[i] > nums[st[st.length - 1]]) {
            const j = st.pop();
            if (j - i + 1 > ans) ans = j - i + 1;
        }
    }
    return ans;
};
