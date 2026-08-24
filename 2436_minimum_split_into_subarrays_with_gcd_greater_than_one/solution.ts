// LeetCode 2436 - Minimum Split Into Subarrays With GCD Greater Than One
// https://leetcode.com/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/

export function minimumSplits(nums: number[]): number {
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    let ans = 1, g = nums[0];
    for (let i = 1; i < nums.length; i++) {
        const ng = gcd(g, nums[i]);
        if (ng === 1) {
            ans++;
            g = nums[i];
        } else g = ng;
    }
    return ans;
}
