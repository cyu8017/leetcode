// LeetCode 3169 - Count Days Without Meetings
// https://leetcode.com/problems/count-days-without-meetings/

using System;

public class Solution {
    public int CountDays(int days, int[][] meetings) {
        Array.Sort(meetings, (a, b) => a[0].CompareTo(b[0]));
        int last = 0, ans = 0;
        foreach (var e in meetings) {
            int st = e[0], ed = e[1];
            if (last < st) ans += st - last - 1;
            last = Math.Max(last, ed);
        }
        ans += days - last;
        return ans;
    }
}
