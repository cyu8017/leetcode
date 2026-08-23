// LeetCode 3253 - Construct String with Minimum Cost (Easy)
// https://leetcode.com/problems/construct-string-with-minimum-cost-easy/

var minimumCost = function(target, words, costs) {
    const inf = 1e18;
    const n = target.length;
    const dp = new Array(n + 1).fill(inf);
    dp[0] = 0;
    const best = new Map();
    for (let i = 0; i < words.length; i++) {
        const old = best.get(words[i]);
        if (old === undefined || costs[i] < old) best.set(words[i], costs[i]);
    }
    for (let i = 0; i < n; i++) {
        if (dp[i] === inf) continue;
        for (const [w, c] of best) {
            const L = w.length;
            if (i + L <= n && target.startsWith(w, i) && dp[i] + c < dp[i + L]) dp[i + L] = dp[i] + c;
        }
    }
    if (dp[n] === inf) return -1;
    return dp[n];
};
