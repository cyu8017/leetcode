// LeetCode 3881 - Direction Assignments With Exactly K Visible People
// https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/

const N3881 = 100001;
const MOD3881 = 1000000007;
let fact3881, invFact3881, ready3881 = false;
function qmi3881(a: any, k: any, p: any): any {
    let res = 1n;
    let A = BigInt(a), K = BigInt(k), P = BigInt(p);
    while (K !== 0n) {
        if ((K & 1n) !== 0n) res = res * A % P;
        K >>= 1n;
        A = A * A % P;
    }
    return Number(res);
}function init3881(): any {
    if (ready3881) return;
    fact3881 = new Array(N3881);
    invFact3881 = new Array(N3881);
    fact3881[0] = invFact3881[0] = 1;
    for (let i = 1; i < N3881; i++) {
        fact3881[i] = Number(BigInt(fact3881[i - 1]) * BigInt(i) % BigInt(MOD3881));
        invFact3881[i] = qmi3881(fact3881[i], MOD3881 - 2, MOD3881);
    }
    ready3881 = true;
}function comb3881(n: any, k: any): any {
    return Number(BigInt(fact3881[n]) * BigInt(invFact3881[k]) % BigInt(MOD3881) * BigInt(invFact3881[n - k]) % BigInt(MOD3881));
}export function countVisiblePeople(n: any, pos: any, k: any): any {
    init3881();
    const l = pos, r = n - pos - 1;
    let ans = 0;
    for (let a = 0; a <= Math.min(k, l); a++) {
        const b = k - a;
        if (b <= r) {
            ans = (ans + 2 * comb3881(l, a) % MOD3881 * comb3881(r, b) % MOD3881) % MOD3881;
        }
    }
    return ans;
}
