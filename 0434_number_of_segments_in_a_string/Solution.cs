// LeetCode 0434 - Number of Segments in a String
// https://leetcode.com/problems/number-of-segments-in-a-string/

public class Solution {
    public int CountSegments(string s) {
        int count = 0;
        bool inSegment = false;
        foreach (char ch in s) {
            if (ch != ' ') {
                if (!inSegment) {
                    count++;
                    inSegment = true;
                }
            } else {
                inSegment = false;
            }
        }
        return count;
    }
}
