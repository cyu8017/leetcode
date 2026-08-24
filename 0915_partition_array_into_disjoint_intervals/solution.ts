// LeetCode 0915 - Partition Array into Disjoint Intervals
// https://leetcode.com/problems/partition-array-into-disjoint-intervals/

export function partitionDisjoint(nums: number[]): number {
    const n = nums.length;
    const minRight = new Array(n);
    minRight[n - 1] = nums[n - 1];
    for (let i = n - 2; i >= 0; i--) minRight[i] = Math.min(nums[i], minRight[i + 1]);
    let maxLeft = nums[0];
    for (let i = 1; i < n; i++) {
        if (maxLeft <= minRight[i]) return i;
        maxLeft = Math.max(maxLeft, nums[i]);
    }
    return n - 1;
}
