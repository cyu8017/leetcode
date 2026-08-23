// LeetCode 0434 - Number of Segments in a String
// https://leetcode.com/problems/number-of-segments-in-a-string/

class Solution {
    public int countSegments(String s) {
        int count = 0;
        boolean inSegment = false;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != ' ') {
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
