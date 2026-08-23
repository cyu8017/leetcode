// LeetCode 3379 - Transformed Array
// https://leetcode.com/problems/transformed-array/

var constructTransformedArray = function(nums) {
    const n = nums.length;
    const ans = new Array(n);
    for (let i = 0; i < n; i++) {
        const j = ((i + nums[i]) % n + n) % n;
        ans[i] = nums[j];
    }
    return ans;
};
