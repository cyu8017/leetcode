// LeetCode 2653 - Sliding Subarray Beauty
// https://leetcode.com/problems/sliding-subarray-beauty/

var getSubarrayBeauty = function(nums, k, x) {
    const freq = new Array(101).fill(0);
    const ans = new Array(nums.length - k + 1);
    for (let i = 0; i < nums.length; i++) {
        freq[nums[i] + 50]++;
        if (i >= k) freq[nums[i - k] + 50]--;
        if (i >= k - 1) {
            let need = x, val = 0;
            for (let j = 0; j < 50; j++) {
                need -= freq[j];
                if (need <= 0) { val = j - 50; break; }
            }
            ans[i - k + 1] = val;
        }
    }
    return ans;
};
