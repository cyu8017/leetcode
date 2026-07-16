// LeetCode 0520 - Detect Capital
// https://leetcode.com/problems/detect-capital/

class Solution {
    detectCapitalUse(word) {
        return word === word.toUpperCase() || word === word.toLowerCase() || word === word[0].toUpperCase() + word.slice(1).toLowerCase();
    }
}

module.exports = { Solution };
