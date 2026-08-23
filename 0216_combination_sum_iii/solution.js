// LeetCode 0216 - Combination Sum III
// https://leetcode.com/problems/combination-sum-iii/

/**
 * @param {number} k
 * @param {number} n
 * @return {number[][]}
 */
var combinationSum3 = function(k, n) {
    const result = [];

    function backtrack(start, remaining, path) {
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
};
