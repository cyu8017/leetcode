// LeetCode 1131 - Maximum of Absolute Value Expression
// https://leetcode.com/problems/maximum-of-absolute-value-expression/

/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number}
 */
var maxAbsValExpr = function(arr1, arr2) {
    const n = arr1.length;
    let ans = 0;
    for (const [p, q] of [[1, 1], [1, -1], [-1, 1], [-1, -1]]) {
        let best = p * arr1[0] + q * arr2[0];
        for (let i = 1; i < n; i++) {
            const cur = p * arr1[i] + q * arr2[i] + i;
            ans = Math.max(ans, cur - best);
            best = Math.min(best, cur);
        }
    }
    return ans;
};
