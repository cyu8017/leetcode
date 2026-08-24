// LeetCode 3937 - Minimum Operations To Make Array Modulo Alternating I
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-i/
var minOperations = function(nums, k) {
        for (let i = 0; i < nums.length; i++) nums[i] %= k;
        let ans = 2147483647;
        for (let x = 0; x < k; x++) {
            for (let y = 0; y < k; y++) {
                if (x == y) continue;
                let cnt = 0;
                for (let i = 0; i < nums.length; i++) {
                    let target = (i & 1) != 0 ? y : x;
                    let diff = Math.abs(target - nums[i]);
                    cnt += Math.min(diff, k - diff);
                }
                ans = Math.min(ans, cnt);
            }
        }
        return ans;
    
};
