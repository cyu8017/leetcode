// LeetCode 3301 - Maximize the Total Height of Unique Towers
// https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/

var maximumTotalSum = function(maximumHeight) {
    maximumHeight.sort((a, b) => b - a);
    let ans = 0;
    let prev = 1e18;
    for (const h of maximumHeight) {
        let cur = h;
        if (cur >= prev) cur = prev - 1;
        if (cur <= 0) return -1;
        ans += cur;
        prev = cur;
    }
    return ans;
};
