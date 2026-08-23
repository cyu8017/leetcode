// LeetCode 0683 - K Empty Slots
// https://leetcode.com/problems/k-empty-slots/

using System;

public class Solution {
    public int KEmptySlots(int[] bulbs, int k) {
        int n = bulbs.Length;
        int[] days = new int[n];
        for (int day = 1; day <= n; day++) days[bulbs[day - 1] - 1] = day;
        int ans = int.MaxValue;
        int i = 0;
        while (i < n - k - 1) {
            int left = i, right = i + k + 1, j = left + 1;
            while (j < right && days[j] > days[left] && days[j] > days[right]) j++;
            if (j == right) {
                ans = Math.Min(ans, Math.Max(days[left], days[right]));
                i++;
            } else i = j;
        }
        return ans == int.MaxValue ? -1 : ans;
    }
}
