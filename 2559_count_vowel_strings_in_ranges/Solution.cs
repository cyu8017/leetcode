// LeetCode 2559 - Count Vowel Strings in Ranges
// https://leetcode.com/problems/count-vowel-strings-in-ranges/

public class Solution {
    public int[] VowelStrings(string[] words, int[][] queries) {
        bool IsV(char c) => c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        int n = words.Length;
        int[] pref = new int[n + 1];
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i];
            string w = words[i];
            if (w.Length > 0 && IsV(w[0]) && IsV(w[w.Length - 1])) pref[i + 1]++;
        }
        int[] ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; ++i) {
            ans[i] = pref[queries[i][1] + 1] - pref[queries[i][0]];
        }
        return ans;
    }
}
