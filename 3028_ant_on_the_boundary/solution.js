// LeetCode 3028 - Ant on the Boundary
// https://leetcode.com/problems/ant-on-the-boundary/

var returnToBoundaryCount = function(nums) {
    let s = 0, ans = 0;
    for (const x of nums) {
        s += x;
        if (s === 0) ans++;
    }
    return ans;
};
