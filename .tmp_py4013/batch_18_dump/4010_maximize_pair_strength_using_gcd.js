// LeetCode 4010 - Maximize Pair Strength Using GCD
// https://leetcode.com/problems/maximize-pair-strength-using-gcd/
var Gcd = function(a, b) {
        while (b != 0) { let t = a % b; a = b; b = t; }
        return a;
    
};
var maxPairStrength = function(nums) {
        let n = nums.length;
        let ans = 0;
        for (let i = 0; i < n; i++) {
            for (let j = i + 1; j < n; j++) {
                let g = Gcd(nums[i], nums[j]);
                let x = nums[i] * nums[j] / (g * g);
                ans = Math.max(ans, x);
            }
        }
        return ans;
    
};
