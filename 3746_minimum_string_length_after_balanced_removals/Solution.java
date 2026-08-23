// LeetCode 3746 - Minimum String Length After Balanced Removals
// https://leetcode.com/problems/minimum-string-length-after-balanced-removals/

class Solution {
    public int minLengthAfterRemovals(String s) {
        int a = 0;
        for (char c : s.toCharArray()) if (c == 'a') a++;
        int b = s.length() - a;
        return Math.abs(a - b);
    }
}
