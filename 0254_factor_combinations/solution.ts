// LeetCode 0254 - Factor Combinations
// https://leetcode.com/problems/factor-combinations/

export function getFactors(n: number): number[][] {
    const result: number[][] = [];

    function backtrack(remain: number, path: number[], start: number): void {
        if (start > remain) {
            if (path.length > 1) {
                result.push([...path]);
            }
            return;
        }

        let factor = start;
        while (factor * factor <= remain) {
            if (remain % factor === 0) {
                path.push(factor);
                backtrack(Math.floor(remain / factor), path, factor);
                path.pop();
            }
            factor += 1;
        }

        if (path.length > 0) {
            path.push(remain);
            if (path.length > 1) {
                result.push([...path]);
            }
            path.pop();
        }
    }

    backtrack(n, [], 2);
    return result;
}
