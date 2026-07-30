// LeetCode 1239 - Maximum Length of a Concatenated String with Unique Characters
// https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxLength(string[] arr) {
        var masks = new List<(int used, int length)> { (0, 0) };
        foreach (string word in arr) {
            int mask = 0;
            foreach (char ch in word) mask |= 1 << (ch - 'a');
            if (BitCount(mask) != word.Length) continue;
            var next = new List<(int, int)>(masks);
            foreach (var (used, length) in masks) {
                if ((used & mask) == 0) {
                    next.Add((used | mask, length + word.Length));
                }
            }
            masks = next;
        }
        int best = 0;
        foreach (var (_, length) in masks) best = Math.Max(best, length);
        return best;
    }

    private static int BitCount(int x) {
        int c = 0;
        while (x != 0) {
            c += x & 1;
            x >>= 1;
        }
        return c;
    }
}
