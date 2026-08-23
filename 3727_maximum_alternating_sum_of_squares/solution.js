// LeetCode 3727 - Maximum Alternating Sum of Squares
// https://leetcode.com/problems/maximum-alternating-sum-of-squares/

var maxAlternatingSum = function(nums) {
    const a = nums.map(x => x * x);
    a.sort((x, y) => x - y);
    const m = Math.floor(a.length / 2);
    let ans = 0;
    for (let i = 0; i < m; i++) ans -= a[i];
    for (let i = m; i < a.length; i++) ans += a[i];
    return ans;
};
