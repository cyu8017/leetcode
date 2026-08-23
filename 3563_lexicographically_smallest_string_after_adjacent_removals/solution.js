// LeetCode 3563 - Lexicographically Smallest String After Adjacent Removals
// https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/

function isConsec3563(a, b) {
    const d = Math.abs(a.charCodeAt(0) - b.charCodeAt(0));
    return d === 1 || d === 25;
}
var lexicographicallySmallestString = function(s) {
    const n = s.length;
    const dp = Array.from({length: n + 1}, () => new Array(n + 1).fill(''));
    for (let length = 1; length <= n; length++) {
        for (let i = 0; i + length <= n; i++) {
            const j = i + length;
            let minStr = s[i] + dp[i + 1][j];
            for (let k = i + 1; k < j; k++) {
                if (isConsec3563(s[i], s[k]) && dp[i + 1][k] === '') {
                    const cand = dp[k + 1][j];
                    if (cand < minStr) minStr = cand;
                }
            }
            dp[i][j] = minStr;
        }
    }
    return dp[0][n];
};
