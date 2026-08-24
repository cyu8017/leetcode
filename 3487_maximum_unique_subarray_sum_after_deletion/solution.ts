// LeetCode 3487 - Maximum Unique Subarray Sum After Deletion
// https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

export function maxSum(nums: any): any {
    const seen = new Set();
    let sum = 0;
    let hasPos = false;
    let maxNeg = -1e9;
    for (const x of nums) {
        if (x < 0) {
            if (x > maxNeg) maxNeg = x;
            continue;
        }
        hasPos = true;
        if (!seen.has(x)) {
            seen.add(x);
            sum += x;
        }
    }
    return hasPos ? sum : maxNeg;
}
