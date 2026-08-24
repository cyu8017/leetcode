// LeetCode 3375 - Minimum Operations to Make Array Values Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/

export function minOperations(nums: any, k: any): any {
    const seen = new Set();
    for (const x of nums) {
        if (x < k) return -1;
        if (x > k) seen.add(x);
    }
    return seen.size;
}
