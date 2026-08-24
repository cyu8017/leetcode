// LeetCode 2297 - Jump Game VIII
// https://leetcode.com/problems/jump-game-viii/

var minCost = function(nums, costs) {
    const n = nums.length;
    const dp = new Array(n).fill(Infinity);
    dp[0] = 0;
    const stack1 = [], stack2 = [];
    for (let i = 0; i < n; i++) {
        while (stack1.length && nums[stack1[stack1.length - 1]] <= nums[i]) {
            const j = stack1.pop();
            dp[i] = Math.min(dp[i], dp[j] + costs[i]);
        }
        while (stack2.length && nums[stack2[stack2.length - 1]] > nums[i]) {
            const j = stack2.pop();
            dp[i] = Math.min(dp[i], dp[j] + costs[i]);
        }
        if (stack1.length) dp[i] = Math.min(dp[i], dp[stack1[stack1.length - 1]] + costs[i]);
        if (stack2.length) dp[i] = Math.min(dp[i], dp[stack2[stack2.length - 1]] + costs[i]);
        stack1.push(i);
        stack2.push(i);
    }
    return dp[n - 1];
};
