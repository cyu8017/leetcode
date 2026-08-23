// LeetCode 3524 - Find X Value of Array I
// https://leetcode.com/problems/find-x-value-of-array-i/

var resultArray = function(nums, k) {
    const ans = new Array(k).fill(0);
    let dp = new Array(k).fill(0);
    for (const num of nums) {
        const newDp = new Array(k).fill(0);
        const nm = num % k;
        newDp[nm] = 1;
        for (let i = 0; i < k; i++) newDp[(i * nm) % k] += dp[i];
        for (let i = 0; i < k; i++) ans[i] += newDp[i];
        dp = newDp;
    }
    return ans;
};
