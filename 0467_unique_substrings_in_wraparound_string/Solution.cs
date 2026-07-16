// LeetCode 0467 - Unique Substrings in Wraparound String
// https://leetcode.com/problems/unique-substrings-in-wraparound-string/

using System.Linq;

public class Solution {
    public int FindSubstringInWraproundString(string s) {
        int[] counts = new int[26];
        int length = 0;
        for (int index = 0; index < s.Length; index++) {
            if (index > 0 && (s[index] - s[index - 1] + 26) % 26 == 1) {
                length++;
            } else {
                length = 1;
            }
            int position = s[index] - 'a';
            counts[position] = Math.Max(counts[position], length);
        }
        return counts.Sum();
    }
}
