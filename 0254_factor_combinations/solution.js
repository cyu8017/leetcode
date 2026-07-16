// LeetCode 0254 - Factor Combinations
// https://leetcode.com/problems/factor-combinations/

/**
 * @param {number} n
 * @return {number[][]}
 */
var getFactors = function(n) {
    const result = [];

    function backtrack(remain, path, start) {
        if (start > remain) {
            if (path.length > 1) {
                result.push(path.slice());
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
                result.push(path.slice());
            }
            path.pop();
        }
    }

    backtrack(n, [], 2);
    return result;
};
