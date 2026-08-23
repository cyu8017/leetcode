// LeetCode 0784 - Letter Case Permutation
// https://leetcode.com/problems/letter-case-permutation/

using System.Collections.Generic;

public class Solution {
    public IList<string> LetterCasePermutation(string s) {
        var result = new List<string> { "" };
        foreach (char ch in s) {
            var next = new List<string>();
            if (char.IsLetter(ch)) {
                char lower = char.ToLower(ch);
                char upper = char.ToUpper(ch);
                foreach (string prefix in result) {
                    next.Add(prefix + lower);
                    next.Add(prefix + upper);
                }
            } else {
                foreach (string prefix in result) next.Add(prefix + ch);
            }
            result = next;
        }
        return result;
    }
}
