// LeetCode 2903 - Find Indices With Index and Value Difference I
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/

export function findIndices(nums: number[], indexDifference: number, valueDifference: number): number[] {
    const n = nums.length;
    for (let i = 0; i < n; i++)
        for (let j = i; j < n; j++) {
            if (Math.abs(j - i) >= indexDifference && Math.abs(nums[i] - nums[j]) >= valueDifference)
                return [i, j];
        }
    return [-1, -1];
}
