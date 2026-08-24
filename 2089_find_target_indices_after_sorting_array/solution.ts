// LeetCode 2089 - Find Target Indices After Sorting Array
// https://leetcode.com/problems/find-target-indices-after-sorting-array/

export function targetIndices(nums: number[], target: number): number[] {
    let less = 0, eq = 0;
    for (const x of nums) {
        if (x < target) less++;
        else if (x === target) eq++;
    }
    const ans = [];
    for (let i = 0; i < eq; i++) ans.push(less + i);
    return ans;
}
