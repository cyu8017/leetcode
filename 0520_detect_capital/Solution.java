// LeetCode 0520 - Detect Capital
// https://leetcode.com/problems/detect-capital/

class Solution {
    public boolean detectCapitalUse(String word) {
        return word.equals(word.toUpperCase())
            || word.equals(word.toLowerCase())
            || word.equals(word.substring(0, 1).toUpperCase() + word.substring(1).toLowerCase());
    }
}
