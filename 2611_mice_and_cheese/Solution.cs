// LeetCode 2611 - Mice and Cheese
// https://leetcode.com/problems/mice-and-cheese/

using System;

public class Solution {
    public int MiceAndCheese(int[] reward1, int[] reward2, int k) {
        int n = reward1.Length;
        int[] diff = new int[n];
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans += reward2[i];
            diff[i] = reward1[i] - reward2[i];
        }
        Array.Sort(diff, (a, b) => b.CompareTo(a));
        for (int i = 0; i < k; ++i) ans += diff[i];
        return ans;
    }
}
