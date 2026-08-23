// LeetCode 2409 - Count Days Spent Together
// https://leetcode.com/problems/count-days-spent-together/

using System;

public class Solution {
    public int CountDaysTogether(string arriveAlice, string leaveAlice, string arriveBob, string leaveBob) {
        int[] days = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
        int ToDay(string s) {
            int m = (s[0] - '0') * 10 + (s[1] - '0');
            int d = (s[3] - '0') * 10 + (s[4] - '0');
            int res = d;
            for (int i = 0; i < m - 1; i++) res += days[i];
            return res;
        }
        int a1 = ToDay(arriveAlice), a2 = ToDay(leaveAlice);
        int b1 = ToDay(arriveBob), b2 = ToDay(leaveBob);
        int start = Math.Max(a1, b1);
        int end = Math.Min(a2, b2);
        if (end < start) return 0;
        return end - start + 1;
    }
}
