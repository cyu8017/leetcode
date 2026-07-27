// LeetCode 1680 - Concatenation of Consecutive Binary Numbers
// https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

function concatenatedBinary(n: number): number {
    let ans = 0n, bits = 0n;
    const mod = 1000000007n;
    for (let x = 1; x <= n; x++) {
        if ((x & (x - 1)) === 0) bits++;
        ans = ((ans << bits) + BigInt(x)) % mod;
    }
    return Number(ans);
}
