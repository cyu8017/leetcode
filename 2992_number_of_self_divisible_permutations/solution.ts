// LeetCode 2992 - Number of Self-Divisible Permutations
// https://leetcode.com/problems/number-of-self-divisible-permutations/

function gcd(a: any, b: any): any {
    while (b !== 0) { const t = a % b; a = b; b = t; }
    return a;
}export function selfDivisiblePermutationCount(n: any): any {
    let ans = 0;
    const used = new Array(n + 1).fill(false);
    function dfs(pos: any): any {
        if (pos > n) { ans++; return; }
        for (let v = 1; v <= n; v++) {
            if (used[v]) continue;
            if (gcd(v, pos) !== 1) continue;
            used[v] = true;
            dfs(pos + 1);
            used[v] = false;
        }
    }    dfs(1);
    return ans;
}
