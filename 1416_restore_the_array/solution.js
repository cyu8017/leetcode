// LeetCode 1416: Restore The Array

var numberOfArrays = function(s, k) {
    const mod = 1000000007, dp = Array(s.length + 1).fill(0);
    dp[0] = 1;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === "0") continue;
        let value = 0;
        for (let j = i; j < s.length; j++) { value = value * 10 + Number(s[j]); if (value > k) break; dp[j + 1] = (dp[j + 1] + dp[i]) % mod; }
    }
    return dp[s.length];
};
