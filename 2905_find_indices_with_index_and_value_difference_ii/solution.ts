// LeetCode 2905 - Find Indices With Index and Value Difference II
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/

export function findIndices(nums: number[], indexDifference: number, valueDifference: number): number[] {
    const n = nums.length;
    let minIdx = 0, maxIdx = 0;
    for (let j = indexDifference; j < n; j++) {
        const i = j - indexDifference;
        if (nums[i] < nums[minIdx]) minIdx = i;
        if (nums[i] > nums[maxIdx]) maxIdx = i;
        if (nums[j] - nums[minIdx] >= valueDifference) return [minIdx, j];
        if (nums[maxIdx] - nums[j] >= valueDifference) return [maxIdx, j];
    }
    return [-1, -1];
}
