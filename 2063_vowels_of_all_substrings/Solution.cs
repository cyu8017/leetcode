// LeetCode 2063 - Vowels of All Substrings
// https://leetcode.com/problems/vowels-of-all-substrings/

public class Solution {
    public long CountVowels(string word) {
        bool IsVowel(char c) => c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        int n = word.Length;
        long ans = 0;
        for (int i = 0; i < n; i++)
            if (IsVowel(word[i])) ans += (long)(i + 1) * (n - i);
        return ans;
    }
}
