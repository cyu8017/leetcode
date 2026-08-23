// LeetCode 0710 - Random Pick with Blacklist
// https://leetcode.com/problems/random-pick-with-blacklist/

using System;
using System.Collections.Generic;

public class Solution {
    private readonly int size;
    private readonly Dictionary<int, int> mapping = new Dictionary<int, int>();
    private readonly Random rand = new Random();

    public Solution(int n, int[] blacklist) {
        size = n - blacklist.Length;
        var black = new HashSet<int>(blacklist);
        int white = size;
        foreach (int b in blacklist) {
            if (b < size) {
                while (black.Contains(white)) white++;
                mapping[b] = white++;
            }
        }
    }

    public int Pick() {
        int index = rand.Next(size);
        return mapping.TryGetValue(index, out int mapped) ? mapped : index;
    }
}
