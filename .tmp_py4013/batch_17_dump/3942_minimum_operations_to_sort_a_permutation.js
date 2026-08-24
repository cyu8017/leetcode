// LeetCode 3942 - Minimum Operations To Sort A Permutation
// https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/
var minOperations = function(nums) {
        let n = nums.length;
        let zero = 0;
        for (let i = 0; i < n; i++) {
            if (nums[i] == 0) {
                zero = i;
                break;
            }
        }
        let ans = 2147483647;
        if (check(nums, zero, 1)) {
            ans = Math.min(ans, zero);
            ans = Math.min(ans, n - zero + 2);
        }
        if (check(nums, zero, -1)) {
            ans = Math.min(ans, zero + 2);
            ans = Math.min(ans, n - zero);
        }
        return ans == 2147483647 ? -1 : ans;
    
};
var check = function(nums, zero, step) {
        let n = nums.length;
        for (let i = 1; i < n; i++) {
            let prev = ((zero + (i - 1) * step) % n + n) % n;
            let curr = ((zero + i * step) % n + n) % n;
            if (nums[prev] > nums[curr]) return false;
        }
        return true;
    
};
