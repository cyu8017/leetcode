// LeetCode 1662 - Check If Two String Arrays are Equivalent
// https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

public class Solution {
    public bool ArrayStringsAreEqual(string[] word1, string[] word2) {
        return string.Concat(word1) == string.Concat(word2);
    }
}
