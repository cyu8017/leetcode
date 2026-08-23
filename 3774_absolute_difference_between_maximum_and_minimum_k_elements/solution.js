// LeetCode 3774 - Absolute Difference Between Maximum And Minimum K Elements
// https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/

var absDifference = function(nums, k) {
    const a = nums.slice().sort((x, y) => x - y);
    let ans = 0;
    const n = a.length;
    for (let i = 0; i < k; i++) ans += a[n - i - 1] - a[i];
    return ans;
};
