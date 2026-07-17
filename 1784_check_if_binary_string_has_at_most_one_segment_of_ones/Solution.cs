// LeetCode 1784 - Check if Binary String Has at Most One Segment of Ones
// https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

public class Solution {
    public bool CheckOnesSegment(string s) {
        string trimmed = s.Trim('0');
        return !trimmed.Contains("01");
    }
}
