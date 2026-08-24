// LeetCode 3655 - XOR After Range Multiplication Queries II
// https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/

export function xorAfterQueries(nums: any, queries: any): any {
    const MOD = 1000000007n;
    const n = nums.length;
    const byK = new Map();
    for (const q of queries) {
        if (!byK.has(q[2])) byK.set(q[2], []);
        byK.get(q[2]).push(q);
    }
    const res = nums.slice();
    for (const [, list] of byK) {
        const fac = new Array(n).fill(1n);
        for (const u of list)
            for (let i = u[0]; i <= u[1]; i += u[2])
                fac[i] = fac[i] * BigInt(u[3]) % MOD;
        for (let i = 0; i < n; i++)
            res[i] = Number(BigInt(res[i]) * fac[i] % MOD);
    }
    let ans = 0;
    for (const v of res) ans ^= v;
    return ans;
}
