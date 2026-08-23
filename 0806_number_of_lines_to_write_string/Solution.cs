// LeetCode 0806 - Number of Lines To Write String
// https://leetcode.com/problems/number-of-lines-to-write-string/

public class Solution {
    public int[] NumberOfLines(int[] widths, string s) {
        int lines = 1, width = 0;
        foreach (char ch in s) {
            int w = widths[ch - 'a'];
            if (width + w > 100) { lines++; width = w; }
            else width += w;
        }
        return new int[] { lines, width };
    }
}
