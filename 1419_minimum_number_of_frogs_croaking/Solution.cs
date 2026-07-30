// LeetCode 1419 - Minimum Number Of Frogs Croaking
// https://leetcode.com/problems/minimum-number-of-frogs-croaking/

public class Solution {
    public int MinNumberOfFrogs(string croakOfFrogs) {
        string order = "croak";
        var counts = new int[5];
        int active = 0, answer = 0;
        foreach (char ch in croakOfFrogs) {
            int i = order.IndexOf(ch);
            if (i < 0 || (i > 0 && counts[i - 1] == 0)) return -1;
            if (i > 0) counts[i - 1]--;
            counts[i]++;
            if (i == 0) { active++; answer = System.Math.Max(answer, active); }
            else if (i == 4) { counts[4]--; active--; }
        }
        return active == 0 ? answer : -1;
    }
}
