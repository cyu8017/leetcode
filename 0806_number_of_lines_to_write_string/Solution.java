// LeetCode 0806 - Number of Lines To Write String
// https://leetcode.com/problems/number-of-lines-to-write-string/

class Solution {
    public int[] numberOfLines(int[] widths, String s) {
        int lines = 1, width = 0;
        for (char ch : s.toCharArray()) {
            int w = widths[ch - 'a'];
            if (width + w > 100) {
                lines++;
                width = w;
            } else {
                width += w;
            }
        }
        return new int[] {lines, width};
    }
}
