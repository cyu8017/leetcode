// LeetCode 1349 - Maximum Students Taking Exam
// https://leetcode.com/problems/maximum-students-taking-exam/

using System.Collections.Generic;
public class Solution {
    public int MaxStudents(char[][] seats) {
        int rows = seats.Length, cols = seats[0].Length;
        var validRows = new List<int>[rows];
        for (int r = 0; r < rows; r++) {
            int available = 0;
            for (int c = 0; c < cols; c++) if (seats[r][c] == '.') available |= 1 << c;
            validRows[r] = new List<int>();
            for (int mask = 0; mask < (1 << cols); mask++)
                if ((mask & ~available) == 0 && (mask & (mask << 1)) == 0)
                    validRows[r].Add(mask);
        }
        var dp = new Dictionary<int, int> { [0] = 0 };
        foreach (var masks in validRows) {
            var nxt = new Dictionary<int, int>();
            foreach (int mask in masks) {
                foreach (var kv in dp) {
                    int previous = kv.Key, count = kv.Value;
                    if ((mask & (previous << 1)) == 0 && (mask & (previous >> 1)) == 0) {
                        int bits = System.Numerics.BitOperations.PopCount((uint)mask);
                        int val = count + bits;
                        if (!nxt.ContainsKey(mask) || val > nxt[mask]) nxt[mask] = val;
                    }
                }
            }
            dp = nxt;
        }
        int ans = 0;
        foreach (int v in dp.Values) ans = System.Math.Max(ans, v);
        return ans;
    }
}
