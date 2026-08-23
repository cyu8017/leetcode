// LeetCode 0691 - Stickers to Spell Word
// https://leetcode.com/problems/stickers-to-spell-word/

using System;
using System.Collections.Generic;

public class Solution {
    private List<char> chars = new List<char>();
    private List<int[]> sticks = new List<int[]>();
    private Dictionary<string, int> memo = new Dictionary<string, int>();

    private string Key(int[] state) => string.Join(",", state);

    private int Dfs(int[] state) {
        string key = Key(state);
        if (memo.ContainsKey(key)) return memo[key];
        int i = 0;
        while (i < state.Length && state[i] == 0) i++;
        if (i == state.Length) return memo[key] = 0;
        char first = chars[i];
        int best = int.MaxValue / 4;
        foreach (var stick in sticks) {
            if (stick[first - 'a'] == 0) continue;
            int[] nxt = (int[])state.Clone();
            for (int j = 0; j < chars.Count; j++) {
                nxt[j] = Math.Max(0, nxt[j] - stick[chars[j] - 'a']);
            }
            best = Math.Min(best, 1 + Dfs(nxt));
        }
        return memo[key] = best;
    }

    public int MinStickers(string[] stickers, string target) {
        int[] need = new int[26];
        foreach (char ch in target) need[ch - 'a']++;
        chars.Clear();
        for (int i = 0; i < 26; i++) if (need[i] > 0) chars.Add((char)('a' + i));
        sticks.Clear();
        foreach (string sticker in stickers) {
            int[] counts = new int[26];
            foreach (char ch in sticker) counts[ch - 'a']++;
            bool useful = false;
            foreach (char ch in chars) if (counts[ch - 'a'] > 0) { useful = true; break; }
            if (useful) sticks.Add(counts);
        }
        memo.Clear();
        int[] state = new int[chars.Count];
        for (int i = 0; i < chars.Count; i++) state[i] = need[chars[i] - 'a'];
        int result = Dfs(state);
        return result >= int.MaxValue / 4 ? -1 : result;
    }
}
