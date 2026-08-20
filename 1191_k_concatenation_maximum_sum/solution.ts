// LeetCode 1191 - K-Concatenation Maximum Sum
// https://leetcode.com/problems/k-concatenation-maximum-sum/

function kConcatenationMaxSum(arr: number[], k: number): number {
    const MOD = 1e9 + 7;
    const kadane = (nums) => {
        let best = 0, cur = 0;
        for (const x of nums) {
            cur = Math.max(0, cur + x);
            best = Math.max(best, cur);
        }
        return best;
    };
    const one = kadane(arr);
    if (k === 1) return one % MOD;
    const two = kadane(arr.concat(arr));
    const total = arr.reduce((a, b) => a + b, 0);
    if (total > 0) return Math.max(one, two + total * (k - 2)) % MOD;
    return Math.max(one, two) % MOD;
}
