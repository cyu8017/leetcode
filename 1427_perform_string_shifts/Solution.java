// LeetCode 1427 - Perform String Shifts
// https://leetcode.com/problems/perform-String-shifts/

class Solution {
    public String stringShift(String s, int[][] shift) {
        int offset = 0;
        for (var sh : shift) offset += sh[0] == 1 ? sh[1] : -sh[1];
        offset %= s.length;
        if (offset < 0) offset += s.length;
        return offset == 0 ? s : s.SubString(s.length - offset) + s.SubString(0, s.length - offset);
    }
}
