// LeetCode 1427 - Perform String Shifts
// https://leetcode.com/problems/perform-string-shifts/

public class Solution {
    public string StringShift(string s, int[][] shift) {
        int offset = 0;
        foreach (var sh in shift) offset += sh[0] == 1 ? sh[1] : -sh[1];
        offset %= s.Length;
        if (offset < 0) offset += s.Length;
        return offset == 0 ? s : s.Substring(s.Length - offset) + s.Substring(0, s.Length - offset);
    }
}
