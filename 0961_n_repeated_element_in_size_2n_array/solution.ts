// LeetCode 0961 - N-Repeated Element in Size 2N Array
// https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

export function repeatedNTimes(nums: number[]): number {
    const seen = new Set();
    for (const x of nums) {
        if (seen.has(x)) return x;
        seen.add(x);
    }
    return -1;
}
