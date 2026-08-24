// LeetCode 3407 - Substring Matching Pattern
// https://leetcode.com/problems/substring-matching-pattern/

var hasMatch = function(s, p) {
    const i = p.indexOf('*');
    const left = p.substring(0, i);
    const right = p.substring(i + 1);
    const li = s.indexOf(left);
    if (li < 0) return false;
    return s.indexOf(right, li + left.length) >= 0;
};
