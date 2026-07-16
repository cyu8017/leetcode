// LeetCode 0040 - Combination Sum II
// https://leetcode.com/problems/combination-sum-ii/

export function combinationSum2(candidates: number[], target: number): number[][] {
    candidates.sort((a, b) => a - b);
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
            if (i > start && candidates[i] === candidates[i - 1]) {
                continue;
            }
            path.push(candidates[i]);
            backtrack(i + 1, remaining - candidates[i], path);
            path.pop();
        }
    }

    backtrack(0, target, []);
    return result;
}
