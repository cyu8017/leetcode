// LeetCode 1830 - Minimum Number of Operations to Make String Sorted
// https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/

function makeStringSorted(s: string): number {
    const MOD = 1000000007n;
    const n = s.length;
    const fact: bigint[] = Array(n + 1).fill(1n);
    for (let i = 2; i <= n; i++) fact[i] = (fact[i - 1] * BigInt(i)) % MOD;

    const modPow = (base: bigint, exp: bigint): bigint => {
        let result = 1n;
        let b = base % MOD;
        let e = exp;
        while (e > 0n) {
            if (e & 1n) result = (result * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return result;
    };

    const invFact: bigint[] = Array(n + 1).fill(1n);
    invFact[n] = modPow(fact[n], MOD - 2n);
    for (let i = n - 1; i >= 0; i--) invFact[i] = (invFact[i + 1] * BigInt(i + 1)) % MOD;

    const freq: number[] = Array(26).fill(0);
    for (const ch of s) freq[ch.charCodeAt(0) - 97] += 1;

    let ans = 0n;
    for (let i = 0; i < n; i++) {
        const c = s.charCodeAt(i) - 97;
        for (let smaller = 0; smaller < c; smaller++) {
            if (freq[smaller] === 0) continue;
            freq[smaller] -= 1;
            let ways = fact[n - i - 1];
            for (const count of freq) ways = (ways * invFact[count]) % MOD;
            ans = (ans + ways) % MOD;
            freq[smaller] += 1;
        }
        freq[c] -= 1;
    }
    return Number(ans);
}
