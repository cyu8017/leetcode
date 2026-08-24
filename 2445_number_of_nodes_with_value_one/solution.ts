// LeetCode 2445 - Number of Nodes With Value One
// https://leetcode.com/problems/number-of-nodes-with-value-one/

export function numberOfNodes(n: number, queries: number[]): number {
    const flip = Array(n + 1).fill(0);
    const val = Array(n + 1).fill(0);
    for (const q of queries) flip[q] ^= 1;
    let ans = 0;
    for (let i = 1; i <= n; i++) {
        val[i] = flip[i];
        if (i > 1) val[i] ^= val[Math.floor(i / 2)];
        ans += val[i];
    }
    return ans;
}
