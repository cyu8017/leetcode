// LeetCode 2654 - Minimum Number of Operations to Make All Array Elements Equal to 1
// https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

export function minOperations(nums: any): any {
    const gcd = (a, b) => { while (b) { const t = a % b; a = b; b = t; } return a; };
    const n = nums.length;
    let ones = 0;
    for (const x of nums) if (x === 1) ones++;
    if (ones > 0) return n - ones;
    let best = n + 1;
    for (let i = 0; i < n; i++) {
        let g = 0;
        for (let j = i; j < n; j++) {
            g = gcd(g, nums[j]);
            if (g === 1) { best = Math.min(best, j - i); break; }
        }
    }
    if (best === n + 1) return -1;
    return best + n - 1;
}
