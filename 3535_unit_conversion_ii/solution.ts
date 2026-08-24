// LeetCode 3535 - Unit Conversion II
// https://leetcode.com/problems/unit-conversion-ii/

const MOD3535 = 1000000007;
function qpow3535(x: any, n: any): any {
    let res = 1n;
    let bx = BigInt(x), bn = BigInt(n), mod = BigInt(MOD3535);
    while (bn > 0n) {
        if (bn & 1n) res = res * bx % mod;
        bx = bx * bx % mod;
        bn >>= 1n;
    }
    return Number(res);
}export function queryConversions(conversions: any, queries: any): any {
    const n = conversions.length + 1;
    const g = Array.from({length: n}, () => []);
    for (const e of conversions) g[e[0]].push([e[1], e[2]]);
    const res = new Array(n).fill(0);
    function dfs(s: any, mul: any): any {
        res[s] = mul;
        for (const e of g[s]) dfs(e[0], Number(BigInt(mul) * BigInt(e[1]) % BigInt(MOD3535)));
    }    dfs(0, 1);
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; i++)
        ans[i] = Number(BigInt(res[queries[i][1]]) * BigInt(qpow3535(res[queries[i][0]], MOD3535 - 2)) % BigInt(MOD3535));
    return ans;
}
