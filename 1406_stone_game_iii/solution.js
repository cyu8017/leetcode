// LeetCode 1406: Stone Game Iii

var stoneGameIII = function(stoneValue) {
    const dp = Array(stoneValue.length + 1).fill(0);
    for (let i = stoneValue.length - 1; i >= 0; i--) {
        let sum = 0; dp[i] = -Infinity;
        for (let take = 1; take <= 3 && i + take <= stoneValue.length; take++) { sum += stoneValue[i + take - 1]; dp[i] = Math.max(dp[i], sum - dp[i + take]); }
    }
    return dp[0] > 0 ? "Alice" : dp[0] < 0 ? "Bob" : "Tie";
};
