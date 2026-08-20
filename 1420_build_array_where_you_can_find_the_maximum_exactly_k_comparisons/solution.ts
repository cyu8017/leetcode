// LeetCode 1420: Build Array Where You Can Find The Maximum Exactly K Comparisons

function numOfArrays(n: any, m: any, k: any): any {
    const mod = 1000000007;
    let dp = Array.from({ length: m + 1 }, (: any): any => Array(k + 1).fill(0));
    for (let max = 1; max <= m; max++) dp[max][1] = 1;
    for (let length = 2; length <= n; length++) {
        const next = Array.from({ length: m + 1 }, (: any): any => Array(k + 1).fill(0));
        for (let max = 1; max <= m; max++) for (let cost = 1; cost <= k; cost++) {
            next[max][cost] = (next[max][cost] + dp[max][cost] * max) % mod;
            for (let previous = 1; previous < max; previous++) next[max][cost] = (next[max][cost] + dp[previous][cost - 1]) % mod;
        }
        dp = next;
    }
    return dp.reduce((sum, row: any): any => (sum + row[k]) % mod, 0);
}
