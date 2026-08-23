// LeetCode 3649 - Number of Perfect Pairs
// https://leetcode.com/problems/number-of-perfect-pairs/

var perfectPairs = function(nums) {
    const n = nums.length;
    const absNums = nums.map(Math.abs).sort((a, b) => a - b);
    let ans = 0, j = 0;
    for (let i = 0; i < n; i++) {
        if (j < i + 1) j = i + 1;
        while (j < n && absNums[j] <= 2 * absNums[i]) j++;
        ans += j - i - 1;
    }
    return ans;
};
