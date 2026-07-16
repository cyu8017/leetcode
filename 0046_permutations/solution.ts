// LeetCode 0046 - Permutations
// https://leetcode.com/problems/permutations/

export function permute(nums: number[]): number[][] {
    const result: number[][] = [];
    const path: number[] = [];
    const used = new Array(nums.length).fill(false);

    function backtrack(): void {
        if (path.length === nums.length) {
            result.push(path.slice());
            return;
        }
        for (let i = 0; i < nums.length; i++) {
            if (used[i]) {
                continue;
            }
            used[i] = true;
            path.push(nums[i]);
            backtrack();
            path.pop();
            used[i] = false;
        }
    }

    backtrack();
    return result;
}
