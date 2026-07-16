// LeetCode 0216 - Combination Sum III
// https://leetcode.com/problems/combination-sum-iii/

export function combinationSum3(k: number, n: number): number[][] {
    const result: number[][] = [];

    function backtrack(start: number, remaining: number, path: number[]): void {
        if (path.length === k) {
            if (remaining === 0) {
                result.push(path.slice());
            }
            return;
        }
        if (remaining <= 0 || path.length >= k) {
            return;
        }

        for (let num = start; num <= 9; num++) {
            if (num > remaining) {
                break;
            }
            path.push(num);
            backtrack(num + 1, remaining - num, path);
            path.pop();
        }
    }

    backtrack(1, n, []);
    return result;
}
