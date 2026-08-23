// LeetCode 0748 - Shortest Completing Word
// https://leetcode.com/problems/shortest-completing-word/

public class Solution {
    public string ShortestCompletingWord(string licensePlate, string[] words) {
        int[] need = new int[26];
        foreach (char ch in licensePlate) {
            if (char.IsLetter(ch)) need[char.ToLower(ch) - 'a']++;
        }
        string best = "";
        foreach (string word in words) {
            int[] counts = new int[26];
            foreach (char ch in word) counts[ch - 'a']++;
            bool ok = true;
            for (int i = 0; i < 26; i++) if (counts[i] < need[i]) { ok = false; break; }
            if (ok && (best.Length == 0 || word.Length < best.Length)) best = word;
        }
        return best;
    }
}
