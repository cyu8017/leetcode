// LeetCode 3865 - Reverse K Subarrays
// https://leetcode.com/problems/reverse-k-subarrays/

var reverseSubarrays = function(nums, k) {
    const n = nums.length;
    const m = Math.floor(n / k);
    for (let i = 0; i < n; i += m) {
        let lo = i, hi = i + m - 1;
        while (lo < hi) {
            const t = nums[lo];
            nums[lo] = nums[hi];
            nums[hi] = t;
            lo++;
            hi--;
        }
    }
    return nums;
};
