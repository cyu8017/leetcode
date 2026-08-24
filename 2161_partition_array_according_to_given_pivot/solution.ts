// LeetCode 2161 - Partition Array According to Given Pivot
// https://leetcode.com/problems/partition-array-according-to-given-pivot/

export function pivotArray(nums: number[], pivot: number): number[] {
    const ans = new Array(nums.length);
    let i = 0;
    for (const x of nums) if (x < pivot) ans[i++] = x;
    for (const x of nums) if (x === pivot) ans[i++] = x;
    for (const x of nums) if (x > pivot) ans[i++] = x;
    return ans;
}
