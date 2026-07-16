// LeetCode 0090 - Subsets II
// https://leetcode.com/problems/subsets-ii/

export function subsetsWithDup(nums: number[]): number[][] {
    nums.sort((a, b) => a - b);
    const result: number[][] = [];

    function backtrack(start: number, path: number[]): void {
        result.push(path.slice());
        for (let i = start; i < nums.length; i++) {
            if (i > start && nums[i] === nums[i - 1]) {
                continue;
            }
            path.push(nums[i]);
            backtrack(i + 1, path);
            path.pop();
        }
    }

    backtrack(0, []);
    return result;
}
