// LeetCode 3528 - Unit Conversion I
// https://leetcode.com/problems/unit-conversion-i/

var baseUnitConversions = function(conversions) {
    const mod = 1000000007;
    const n = conversions.length + 1;
    const g = Array.from({length: n}, () => []);
    for (const e of conversions) g[e[0]].push([e[1], e[2]]);
    const ans = new Array(n).fill(0);
    function dfs(s, mul) {
        ans[s] = mul;
        for (const e of g[s]) dfs(e[0], Number(BigInt(mul) * BigInt(e[1]) % BigInt(mod)));
    }
    dfs(0, 1);
    return ans;
};
