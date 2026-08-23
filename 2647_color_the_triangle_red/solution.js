// LeetCode 2647 - Color the Triangle Red
// https://leetcode.com/problems/color-the-triangle-red/

var colorRed = function(n) {
    const ans = [];
    for (let i = 1; i <= n; i++) ans.push([i, 1]);
    for (let i = n % 2 + 2; i <= n; i += 2)
        for (let j = 2; j <= 2 * (n - i) + 2; j++)
            ans.push([i, j]);
    return ans;
};
