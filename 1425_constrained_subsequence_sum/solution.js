var constrainedSubsetSum = function(nums, k) {
    const dp = Array(nums.length), deque = [];
    for (let i = 0; i < nums.length; i++) {
        while (deque.length && deque[0] < i - k) deque.shift();
        dp[i] = nums[i] + Math.max(0, deque.length ? dp[deque[0]] : 0);
        while (deque.length && dp[deque[deque.length - 1]] <= dp[i]) deque.pop();
        deque.push(i);
    }
    return Math.max(...dp);
};
