// LeetCode 2274 - Maximum Consecutive Floors Without Special Floors
// https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

var maxConsecutive = function(bottom, top, special) {
    special.sort((a, b) => a - b);
    let ans = special[0] - bottom;
    for (let i = 1; i < special.length; i++)
        ans = Math.max(ans, special[i] - special[i - 1] - 1);
    ans = Math.max(ans, top - special[special.length - 1]);
    return ans;
};
