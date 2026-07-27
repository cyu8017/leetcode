// LeetCode 1621 - Number of Sets of K Non-Overlapping Line Segments
// https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/

function numberOfSets(n: number, k: number): number {
    const MOD = 1000000007;
    const comb = (N: number, R: number): number => {
        if (R < 0 || R > N) return 0;
        R = Math.min(R, N - R);
        let num = 1n, den = 1n;
        for (let i = 0; i < R; i++) {
            num *= BigInt(N - i);
            den *= BigInt(i + 1);
        }
        return Number(num / den % BigInt(MOD));
    };
    return comb(n + k - 1, 2 * k);
}
