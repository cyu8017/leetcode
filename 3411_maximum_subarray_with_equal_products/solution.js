// LeetCode 3411 - Maximum Subarray With Equal Products
// https://leetcode.com/problems/maximum-subarray-with-equal-products/

var maxLength = function(nums) {
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    const n = nums.length;
    let ans = 1;
    for (let i = 0; i < n; i++) {
        let prod = 1;
        let g = 0, l = 1;
        for (let j = i; j < n; j++) {
            if (prod > 1000000000 / nums[j]) break;
            prod *= nums[j];
            if (g === 0) {
                g = nums[j];
                l = nums[j];
            } else {
                g = gcd(g, nums[j]);
                l = l / gcd(l, nums[j]) * nums[j];
            }
            if (prod === l * g && j - i + 1 > ans) ans = j - i + 1;
        }
    }
    return ans;
};
