// LeetCode 3291 - Minimum Number of Valid Strings to Form Target I
// https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/

var minValidStrings = function(words, target) {
    const n = target.length;
    const inf = 1000000000;
    const dp = new Array(n + 1).fill(inf);
    dp[0] = 0;
    const root = { next: new Array(26).fill(null) };
    for (const w of words) {
        let cur = root;
        for (const c of w) {
            const ci = c.charCodeAt(0) - 97;
            if (!cur.next[ci]) cur.next[ci] = { next: new Array(26).fill(null) };
            cur = cur.next[ci];
        }
    }
    for (let i = 0; i < n; i++) {
        if (dp[i] === inf) continue;
        let cur = root;
        for (let j = i; j < n; j++) {
            const ci = target.charCodeAt(j) - 97;
            if (!cur.next[ci]) break;
            cur = cur.next[ci];
            if (dp[i] + 1 < dp[j + 1]) dp[j + 1] = dp[i] + 1;
        }
    }
    return dp[n] === inf ? -1 : dp[n];
};
