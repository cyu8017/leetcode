// LeetCode 1977 - Number of Ways to Separate Numbers
// https://leetcode.com/problems/number-of-ways-to-separate-numbers/

function numberOfCombinations(num: string): number {
    const MOD = 1000000007;
    const n = num.length;
    if (num[0] === "0") return 0;
    const lcp = Array.from({ length: n + 1 }, () => new Array(n + 1).fill(0));
    for (let i = n - 1; i >= 0; i--) {
        for (let j = n - 1; j >= 0; j--) {
            if (num[i] === num[j]) lcp[i][j] = lcp[i + 1][j + 1] + 1;
        }
    }
    const le = (a: any, b: any, length: any) => {
        const common = lcp[a][b];
        if (common >= length) return true;
        return num[a + common] < num[b + common];
    };
    const dp = Array.from({ length: n + 1 }, () => new Array(n + 1).fill(0));
    const pref = Array.from({ length: n + 1 }, () => new Array(n + 1).fill(0));
    for (let i = 1; i <= n; i++) {
        for (let l = 1; l <= i; l++) {
            const start = i - l;
            if (num[start] === "0") dp[i][l] = 0;
            else if (start === 0) dp[i][l] = 1;
            else {
                let ways = l > 1 ? pref[start][Math.min(l - 1, start)] : 0;
                if (start >= l && le(start - l, start, l)) ways = (ways + dp[start][l]) % MOD;
                dp[i][l] = ways;
            }
        }
        for (let l = 1; l <= n; l++) {
            pref[i][l] = (pref[i][l - 1] + (l <= i ? dp[i][l] : 0)) % MOD;
        }
    }
    return pref[n][n];
}
