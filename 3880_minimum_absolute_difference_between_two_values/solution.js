// LeetCode 3880 - Minimum Absolute Difference Between Two Values
// https://leetcode.com/problems/minimum-absolute-difference-between-two-values/

var minAbsoluteDifference = function(nums) {
    const n = nums.length;
    let ans = n + 1;
    const last = [-ans, -ans, -ans];
    for (let i = 0; i < n; i++) {
        const x = nums[i];
        if (x !== 0) {
            ans = Math.min(ans, i - last[3 - x]);
            last[x] = i;
        }
    }
    if (ans > n) return -1;
    return ans;
};
