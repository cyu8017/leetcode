// LeetCode 3003 - Maximize the Number of Partitions After Operations
// https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/

function popcount(x: any): any {
    let c = 0;
    while (x !== 0) { c += x & 1; x >>= 1; }
    return c;
}export function maxPartitionsAfterOperations(s: any, k: any): any {
    const n = s.length;
    const memo = new Map();
    function key(i: any, cur: any, t: any): any {
        return (BigInt(i) << 32n) | (BigInt(cur) << 1n) | BigInt(t);
    }    function dfs(i: any, cur: any, t: any): any {
        if (i >= n) return 1;
        const kkey = key(i, cur, t).toString();
        if (memo.has(kkey)) return memo.get(kkey);
        const v = 1 << (s.charCodeAt(i) - 97);
        let nxt = cur | v;
        let ans;
        if (popcount(nxt) > k) ans = dfs(i + 1, v, t) + 1;
        else ans = dfs(i + 1, nxt, t);
        if (t > 0) {
            for (let j = 0; j < 26; j++) {
                nxt = cur | (1 << j);
                if (popcount(nxt) > k)
                    ans = Math.max(ans, dfs(i + 1, 1 << j, 0) + 1);
                else
                    ans = Math.max(ans, dfs(i + 1, nxt, 0));
            }
        }
        memo.set(kkey, ans);
        return ans;
    }    return dfs(0, 0, 1);
}
