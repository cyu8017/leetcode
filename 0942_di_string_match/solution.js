// LeetCode 0942 - DI String Match
// https://leetcode.com/problems/di-string-match/

/**
 * @param {string} s
 * @return {number[]}
 */
var diStringMatch = function(s) {
    let lo = 0, hi = s.length;
    const ans = new Array(s.length + 1);
    let k = 0;
    for (const ch of s) {
        if (ch === "I") ans[k++] = lo++;
        else ans[k++] = hi--;
    }
    ans[k] = lo;
    return ans;
};
