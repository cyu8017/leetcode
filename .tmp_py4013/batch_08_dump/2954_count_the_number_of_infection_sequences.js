// LeetCode 2954 - Count the Number of Infection Sequences
// https://leetcode.com/problems/count-the-number-of-infection-sequences/

const MOD = 1000000007;
function modPow(a, b) {
    let res = 1n;
    a = BigInt(a); b = BigInt(b);
    const M = BigInt(MOD);
    while (b > 0n) {
        if (b & 1n) res = res * a % M;
        a = a * a % M;
        b >>= 1n;
    }
    return Number(res);
}
var numberOfSequence = function(n, sick) {
    const fact = new Array(n + 1), invFact = new Array(n + 1);
    fact[0] = 1;
    for (let i = 1; i <= n; i++) fact[i] = Number(BigInt(fact[i - 1]) * BigInt(i) % BigInt(MOD));
    invFact[n] = modPow(fact[n], MOD - 2);
    for (let i = n; i > 0; i--) invFact[i - 1] = Number(BigInt(invFact[i]) * BigInt(i) % BigInt(MOD));
    const m = sick.length;
    const totalEmpty = n - m;
    let ans = BigInt(fact[totalEmpty]);
    let prev = -1;
    for (const s of sick) {
        const gap = s - prev - 1;
        if (prev === -1) ans = ans * BigInt(invFact[gap]) % BigInt(MOD);
        else if (gap > 0) ans = ans * BigInt(invFact[gap]) % BigInt(MOD) * BigInt(modPow(2, gap - 1)) % BigInt(MOD);
        prev = s;
    }
    const gap2 = n - prev - 1;
    ans = ans * BigInt(invFact[gap2]) % BigInt(MOD);
    return Number(ans);
};
