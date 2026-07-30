// LeetCode 1307 - Verbal Arithmetic Puzzle
// https://leetcode.com/problems/verbal-arithmetic-puzzle/

using System.Collections.Generic;

public class Solution {
    public bool IsSolvable(string[] words, string result) {
        int maxWord = 0;
        foreach (var w in words) maxWord = System.Math.Max(maxWord, w.Length);
        if (maxWord > result.Length) return false;
        var letters = new HashSet<char>();
        foreach (var w in words) foreach (char c in w) letters.Add(c);
        foreach (char c in result) letters.Add(c);
        if (letters.Count > 10) return false;
        var leading = new HashSet<char>();
        foreach (var w in words) if (w.Length > 1) leading.Add(w[0]);
        if (result.Length > 1) leading.Add(result[0]);
        var value = new Dictionary<char, int>();
        var used = new bool[10];
        int width = result.Length;

        bool Solve(int column, int row, int total) {
            if (column == width) return total == 0;
            if (row < words.Length) {
                if (column >= words[row].Length) return Solve(column, row + 1, total);
                char ch = words[row][words[row].Length - 1 - column];
                if (value.ContainsKey(ch)) return Solve(column, row + 1, total + value[ch]);
                for (int digit = 0; digit < 10; digit++) {
                    if (!used[digit] && (digit != 0 || !leading.Contains(ch))) {
                        value[ch] = digit; used[digit] = true;
                        if (Solve(column, row + 1, total + digit)) return true;
                        used[digit] = false; value.Remove(ch);
                    }
                }
                return false;
            }
            char chR = result[result.Length - 1 - column];
            int digitR = total % 10, carry = total / 10;
            if (value.ContainsKey(chR))
                return value[chR] == digitR && Solve(column + 1, 0, carry);
            if (used[digitR] || (digitR == 0 && leading.Contains(chR))) return false;
            value[chR] = digitR; used[digitR] = true;
            bool ok = Solve(column + 1, 0, carry);
            used[digitR] = false; value.Remove(chR);
            return ok;
        }
        return Solve(0, 0, 0);
    }
}
