// LeetCode 3109 - Find the Index of Permutation
// https://leetcode.com/problems/find-the-index-of-permutation/

export class BIT {
    constructor(n: any) {
    this.n = n;
    this.c = new Array(n + 1).fill(0);
}
    update(x: any, delta: any): any {
    for (; x <= this.n; x += x & -x) this.c[x] += delta;
}
    query(x: any): any {
    let s = 0;
    for (; x > 0; x -= x & -x) s += this.c[x];
    return s;
}
}

export function getPermutationIndex(perm: number[]): number {
    const MOD = 1000000007;
    const n = perm.length;
    const tree = new BIT(n + 1);
    const f = new Array(n);
    f[0] = 1;
    for (let i = 1; i < n; i++) f[i] = f[i - 1] * i % MOD;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const x = perm[i];
        const cnt = x - 1 - tree.query(x);
        ans = (ans + cnt * f[n - 1 - i]) % MOD;
        tree.update(x, 1);
    }
    return ans;
}
