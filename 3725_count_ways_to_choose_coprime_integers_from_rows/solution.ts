// LeetCode 3725 - Count Ways To Choose Coprime Integers From Rows
// https://leetcode.com/problems/count_ways_to_choose_coprime_integers_from_rows/

export function countCoprime(mat: any): any {
    const MOD = 1000000007;
    const m = mat.length;
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    let dp = new Map();
    for (const v of mat[0]) dp.set(v, (dp.get(v) || 0) + 1);
    for (let i = 1; i < m; i++) {
        const ndp = new Map();
        for (const v of mat[i]) {
            for (const [key, val] of dp) {
                const ng = gcd(key, v);
                ndp.set(ng, ((ndp.get(ng) || 0) + val) % MOD);
            }
        }
        dp = ndp;
    }
    return dp.get(1) || 0;
}
