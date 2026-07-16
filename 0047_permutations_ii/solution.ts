// LeetCode 0047 - Permutations II
// https://leetcode.com/problems/permutations-ii/

export function permuteUnique(nums: number[]): number[][] {
    nums.sort((a, b) => a - b);
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
            if (i > 0 && nums[i] === nums[i - 1] && !used[i - 1]) {
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
