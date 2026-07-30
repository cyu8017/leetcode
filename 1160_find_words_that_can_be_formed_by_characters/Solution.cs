// LeetCode 1160 - Find Words That Can Be Formed by Characters
// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

public class Solution {
    public int CountCharacters(string[] words, string chars) {
        int[] avail = new int[26];
        foreach (char ch in chars) avail[ch - 'a']++;
        int ans = 0;
        foreach (string word in words) {
            int[] need = new int[26];
            bool ok = true;
            foreach (char ch in word) {
                if (++need[ch - 'a'] > avail[ch - 'a']) { ok = false; break; }
            }
            if (ok) ans += word.Length;
        }
        return ans;
    }
}
