// LeetCode 3842 - Toggle Light Bulbs
// https://leetcode.com/problems/toggle-light-bulbs/

using System.Collections.Generic;

public class Solution {
    public int[] ToggleLightBulbs(int[] bulbs) {
        var st = new int[101];
        foreach (int x in bulbs) st[x] ^= 1;
        var ans = new List<int>();
        for (int i = 0; i < 101; i++) if (st[i] == 1) ans.Add(i);
        return ans.ToArray();
    }
}
