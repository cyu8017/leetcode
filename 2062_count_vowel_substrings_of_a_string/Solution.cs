// LeetCode 2062 - Count Vowel Substrings of a String
// https://leetcode.com/problems/count-vowel-substrings-of-a-string/

using System.Collections.Generic;

public class Solution {
    public int CountVowelSubstrings(string word) {
        bool IsVowel(char c) => c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        int ans = 0, n = word.Length;
        for (int i = 0; i < n; i++) {
            var seen = new HashSet<char>();
            for (int j = i; j < n && IsVowel(word[j]); j++) {
                seen.Add(word[j]);
                if (seen.Count == 5) ans++;
            }
        }
        return ans;
    }
}
