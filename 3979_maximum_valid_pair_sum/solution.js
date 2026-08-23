// LeetCode 3979 - Maximum Valid Pair Sum
// https://leetcode.com/problems/maximum-valid-pair-sum/
var maxValidPairSum = function(nums, k) {
        let ans = 0, x = 0;
        for (let j = k; j < nums.length; j++) {
            let y = nums[j];
            x = Math.max(x, nums[j - k]);
            ans = Math.max(ans, x + y);
        }
        return ans;
    
};
