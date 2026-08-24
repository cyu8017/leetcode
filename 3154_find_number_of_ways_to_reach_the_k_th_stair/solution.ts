// LeetCode 3154 - Find Number of Ways to Reach the K-th Stair
// https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/

export function waysToReachStair(k: number): number {
    const f = new Map();
    const dfs = (i, j, jump) => {
        if (i > k + 1) return 0;
        const key = (BigInt(i) << 32n) | (BigInt(jump) << 1n) | BigInt(j);
        const keyS = key.toString();
        if (f.has(keyS)) return f.get(keyS);
        let ans = 0;
        if (i === k) ans++;
        if (i > 0 && j === 0) ans += dfs(i - 1, 1, jump);
        ans += dfs(i + (2 ** jump), 0, jump + 1);
        f.set(keyS, ans);
        return ans;
    };
    return dfs(1, 0, 0);
}
