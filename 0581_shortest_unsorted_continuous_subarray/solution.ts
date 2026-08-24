// LeetCode 0581 - Shortest Unsorted Continuous Subarray
// https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

export function findUnsortedSubarray(nums: number[]): number {
    const n = nums.length;
    let left = -1, right = -2;
    let maxSeen = nums[0], minSeen = nums[n - 1];
    for (let i = 0; i < n; ++i) {
        maxSeen = Math.max(maxSeen, nums[i]);
        if (nums[i] < maxSeen) right = i;
        const j = n - 1 - i;
        minSeen = Math.min(minSeen, nums[j]);
        if (nums[j] > minSeen) left = j;
    }
    return right - left + 1;
}
