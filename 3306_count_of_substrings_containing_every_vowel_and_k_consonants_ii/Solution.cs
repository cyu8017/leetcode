// LeetCode 3306 - Count of Substrings Containing Every Vowel and K Consonants II
// https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/

using System.Collections.Generic;

public class Solution {
    bool IsVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    long AtLeast(string word, int k) {
        var cnt = new Dictionary<char, int>();
        int cons = 0, l = 0;
        long ans = 0;
        for (int r = 0; r < word.Length; r++) {
            char c = word[r];
            if (IsVowel(c)) {
                if (!cnt.ContainsKey(c)) cnt[c] = 0;
                cnt[c]++;
            } else cons++;
            while (cnt.Count == 5 && cons >= k) {
                ans += word.Length - r;
                char c2 = word[l];
                if (IsVowel(c2)) {
                    if (--cnt[c2] == 0) cnt.Remove(c2);
                } else cons--;
                l++;
            }
        }
        return ans;
    }

    public long CountOfSubstrings(string word, int k) {
        return AtLeast(word, k) - AtLeast(word, k + 1);
    }
}
