// LeetCode 2834 - Find the Minimum Possible Sum of a Beautiful Array
// https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/

export function minimumPossibleSum(n: number, target: number): number {
    const MOD = 1000000007;
    const m = Math.floor(target / 2);
    if (n <= m) return Number((BigInt(n) * BigInt(n + 1) / 2n) % BigInt(MOD));
    let sum = BigInt(m) * BigInt(m + 1) / 2n;
    const remain = n - m;
    sum += BigInt(remain) * BigInt(target) + BigInt(remain) * BigInt(remain - 1) / 2n;
    return Number(sum % BigInt(MOD));
}
