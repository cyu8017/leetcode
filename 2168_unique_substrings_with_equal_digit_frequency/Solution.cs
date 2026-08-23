// LeetCode 2168 - Unique Substrings With Equal Digit Frequency
// https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/

public class Solution {
    public int EqualDigitFrequency(string s) {
        int n = s.Length;
        var seen = new HashSet<string>();
        for (int i = 0; i < n; i++) {
            int[] freq = new int[10];
            int maxf = 0, kinds = 0;
            for (int j = i; j < n; j++) {
                int d = s[j] - '0';
                if (freq[d] == 0) kinds++;
                freq[d]++;
                maxf = Math.Max(maxf, freq[d]);
                if (maxf * kinds == j - i + 1) seen.Add(s.Substring(i, j - i + 1));
            }
        }
        return seen.Count;
    }
}
