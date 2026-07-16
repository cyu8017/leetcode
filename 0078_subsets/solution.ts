// LeetCode 0078 - Subsets
// https://leetcode.com/problems/subsets/

export function subsets(nums: number[]): number[][] {
    const result: number[][] = [[]];

    for (const num of nums) {
        const size = result.length;
        for (let i = 0; i < size; i++) {
            result.push([...result[i], num]);
        }
    }

    return result;
}
