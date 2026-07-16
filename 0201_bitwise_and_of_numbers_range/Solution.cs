// LeetCode 0201 - Bitwise AND of Numbers Range\n// https://leetcode.com/problems/\n\npublic class Solution {
    public int RangeBitwiseAnd(int left, int right) {
        var shift = 0;
        while (left < right) { left >>= 1; right >>= 1; shift++; }
        return left << shift;
    }
}
