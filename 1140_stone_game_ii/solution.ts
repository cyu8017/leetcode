// LeetCode 1140 - Stone Game II
// https://leetcode.com/problems/stone-game-ii/

function stoneGameII(piles: number[]): number {
    const n = piles.length;
    const suffix = Array(n + 1).fill(0);
    for (let i = n - 1; i >= 0; i--) suffix[i] = suffix[i + 1] + piles[i];
    const memo = new Map();
    const dfs = (i, m) => {
        const key = `${i},${m}`;
        if (memo.has(key)) return memo.get(key);
        if (i >= n) return 0;
        if (i + m >= n) return suffix[i];
        let minOpp = Infinity;
        for (let x = 1; x <= Math.min(2 * m, n - i); x++) {
            minOpp = Math.min(minOpp, dfs(i + x, Math.max(x, m)));
        }
        const ans = suffix[i] - minOpp;
        memo.set(key, ans);
        return ans;
    };
    return dfs(0, 1);
}
