// LeetCode 0039 - Combination Sum
// https://leetcode.com/problems/combination-sum/

export function combinationSum(candidates: number[], target: number): number[][] {
    const result: number[][] = [];

    function backtrack(start: number, remaining: number, path: number[]): void {
        if (remaining === 0) {
            result.push(path.slice());
            return;
        }
        if (remaining < 0) {
            return;
        }

        for (let i = start; i < candidates.length; i++) {
            path.push(candidates[i]);
            backtrack(i, remaining - candidates[i], path);
            path.pop();
        }
    }

    backtrack(0, target, []);
    return result;
}
