// LeetCode 1528 - Shuffle String
// https://leetcode.com/problems/shuffle-string/

/**
 * @param {string} s
 * @param {number[]} indices
 * @return {string}
 */
var restoreString = function(s, indices) {
    const answer = Array(s.length);
    for (let i = 0; i < s.length; i++) answer[indices[i]] = s[i];
    return answer.join("");
};
