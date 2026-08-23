// LeetCode 3320 - Count the Number of Winning Sequences
// https://leetcode.com/problems/count-the-number-of-winning-sequences/

var countWinningSequences = function(s) {
    const mod = 1000000007;
    const n = s.length;
    const mp = { F: 0, W: 1, E: 2 };
    const beat = [2, 0, 1];
    const score = Array.from({length: 3}, () => new Array(3));
    for (let a = 0; a < 3; a++) {
        for (let b = 0; b < 3; b++) {
            if (a === b) score[a][b] = 0;
            else if (beat[a] === b) score[a][b] = 1;
            else score[a][b] = -1;
        }
    }
    const offset = n;
    let dp = Array.from({length: 3}, () => new Array(2 * n + 1).fill(0));
    const b0 = mp[s[0]];
    for (let a = 0; a < 3; a++) dp[a][score[a][b0] + offset] = 1;
    for (let i = 1; i < n; i++) {
        const ndp = Array.from({length: 3}, () => new Array(2 * n + 1).fill(0));
        const b = mp[s[i]];
        for (let last = 0; last < 3; last++) {
            for (let d = 0; d <= 2 * n; d++) {
                if (dp[last][d] === 0) continue;
                for (let a = 0; a < 3; a++) {
                    if (a === last) continue;
                    const nd = d + score[a][b];
                    if (nd < 0 || nd > 2 * n) continue;
                    ndp[a][nd] = (ndp[a][nd] + dp[last][d]) % mod;
                }
            }
        }
        dp = ndp;
    }
    let ans = 0;
    for (let a = 0; a < 3; a++) {
        for (let d = offset + 1; d <= 2 * n; d++) ans = (ans + dp[a][d]) % mod;
    }
    return ans;
};
