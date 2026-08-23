// LeetCode 2586 - Count the Number of Vowel Strings in Range
// https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

public class Solution {
    public int VowelStrings(string[] words, int left, int right) {
        bool IsV(char c) => c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        int ans = 0;
        for (int i = left; i <= right; ++i) {
            string w = words[i];
            if (IsV(w[0]) && IsV(w[w.Length - 1])) ans++;
        }
        return ans;
    }
}
