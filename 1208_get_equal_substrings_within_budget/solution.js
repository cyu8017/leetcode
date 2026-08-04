// LeetCode 1208 - Get Equal Substrings Within Budget
// https://leetcode.com/problems/get-equal-substrings-within-budget/

/**
 * @param {string} s
 * @param {string} t
 * @param {number} maxCost
 * @return {number}
 */
var equalSubstring = function(s, t, maxCost) {
    let left = 0, cost = 0, answer = 0;
    for (let right = 0; right < s.length; right++) {
        cost += Math.abs(s.charCodeAt(right) - t.charCodeAt(right));
        while (cost > maxCost) {
            cost -= Math.abs(s.charCodeAt(left) - t.charCodeAt(left));
            left++;
        }
        answer = Math.max(answer, right - left + 1);
    }
    return answer;
};
