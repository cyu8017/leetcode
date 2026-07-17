// LeetCode 1784 - Check if Binary String Has at Most One Segment of Ones
// https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

class Solution {
    public boolean checkOnesSegment(String s) {
        int start = 0;
        int end = s.length();
        while (start < end && s.charAt(start) == '0') start++;
        while (end > start && s.charAt(end - 1) == '0') end--;
        return !s.substring(start, end).contains("01");
    }
}
