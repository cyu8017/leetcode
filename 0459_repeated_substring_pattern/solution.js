// LeetCode 0459 - Repeated Substring Pattern
// https://leetcode.com/problems/repeated-substring-pattern/

class Solution {
    repeatedSubstringPattern(s) {
        const doubled = s + s;
        return doubled.slice(1, -1).includes(s);
    }
}

module.exports = { Solution };
