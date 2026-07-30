// LeetCode 1967 - Number of Strings That Appear as Substrings in Word
// https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

using System.Linq;

public class Solution {
    public int NumOfStrings(string[] patterns, string word) {
        return patterns.Count(p => word.Contains(p));
    }
}