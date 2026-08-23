// LeetCode 3730 - Maximum Calories Burnt from Jumps
// https://leetcode.com/problems/maximum-calories-burnt-from-jumps/

var maxCaloriesBurnt = function(heights) {
    heights = heights.slice().sort((a, b) => a - b);
    let ans = 0;
    let pre = 0, l = 0, r = heights.length - 1;
    while (l < r) {
        const d1 = heights[r] - pre;
        ans += d1 * d1;
        const d2 = heights[l] - heights[r];
        ans += d2 * d2;
        pre = heights[l];
        l++;
        r--;
    }
    const d = heights[r] - pre;
    ans += d * d;
    return ans;
};
