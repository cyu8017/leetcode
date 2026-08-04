// LeetCode 1358 - Number Of Substrings Containing All Three Characters
// https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

/**
 * @param {string} s
 * @return {number}
 */
var numberOfSubstrings = function(s) {
    const last = [-1, -1, -1];
    let ans = 0;
    for (let i = 0; i < s.length; i++) {
        last[s.charCodeAt(i) - 97] = i;
        ans += Math.min(...last) + 1;
    }
    return ans;
};
