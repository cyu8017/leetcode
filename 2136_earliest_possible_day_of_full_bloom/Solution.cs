// LeetCode 2136 - Earliest Possible Day of Full Bloom
// https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

public class Solution {
    public int EarliestFullBloom(int[] plantTime, int[] growTime) {
        int n = plantTime.Length;
        int[] idx = new int[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Array.Sort(idx, (a, b) => growTime[b].CompareTo(growTime[a]));
        int day = 0, ans = 0;
        foreach (int i in idx) {
            day += plantTime[i];
            ans = Math.Max(ans, day + growTime[i]);
        }
        return ans;
    }
}
