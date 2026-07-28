// LeetCode 1079 - Letter Tile Possibilities
// https://leetcode.com/problems/letter-tile-possibilities/

using System.Collections.Generic;

public class Solution {
    public int NumTilePossibilities(string tiles) {
        var count = new Dictionary<char, int>();
        foreach (char ch in tiles) {
            count[ch] = count.GetValueOrDefault(ch) + 1;
        }

        int Dfs() {
            int total = 0;
            var keys = new List<char>(count.Keys);
            foreach (char ch in keys) {
                if (count[ch] == 0) {
                    continue;
                }
                count[ch]--;
                total += 1 + Dfs();
                count[ch]++;
            }
            return total;
        }

        return Dfs();
    }
}
