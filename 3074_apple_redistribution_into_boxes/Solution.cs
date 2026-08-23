// LeetCode 3074 - Apple Redistribution into Boxes
// https://leetcode.com/problems/apple-redistribution-into-boxes/

using System;

public class Solution {
    public int MinimumBoxes(int[] apple, int[] capacity) {
        Array.Sort(capacity);
        int s = 0;
        foreach (int x in apple) s += x;
        for (int i = 1; ; i++) {
            s -= capacity[capacity.Length - i];
            if (s <= 0) return i;
        }
    }
}
