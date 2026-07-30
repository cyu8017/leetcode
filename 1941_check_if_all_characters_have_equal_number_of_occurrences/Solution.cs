// LeetCode 1941 - Check if All Characters Have Equal Number of Occurrences
// https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public bool AreOccurrencesEqual(string s) {
        var freq = new Dictionary<char, int>();
        foreach (char c in s) freq[c] = freq.GetValueOrDefault(c) + 1;
        return freq.Values.Distinct().Count() == 1;
    }
}