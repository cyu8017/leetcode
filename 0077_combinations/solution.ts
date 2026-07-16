// LeetCode 0077 - Combinations
// https://leetcode.com/problems/combinations/

export function combine(n: number, k: number): number[][] {
    const result: number[][] = [];
    const path: number[] = [];

    function backtrack(start: number): void {
        if (path.length === k) {
            result.push(path.slice());
            return;
        }

        const remaining = k - path.length;
        for (let i = start; i <= n - remaining + 1; i++) {
            path.push(i);
            backtrack(i + 1);
            path.pop();
        }
    }

    backtrack(1);
    return result;
}
