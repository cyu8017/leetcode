// LeetCode 2937 - Make Three Strings Equal
// https://leetcode.com/problems/make-three-strings-equal/

class Solution {
    public int findMinimumOperations(String s1, String s2, String s3) {
        int n = Math.min(s1.length(), Math.min(s2.length(), s3.length()));
        int i = 0;
        while (i < n && s1.charAt(i) == s2.charAt(i) && s2.charAt(i) == s3.charAt(i)) i++;
        if (i == 0) return -1;
        return s1.length() + s2.length() + s3.length() - 3 * i;
    }
}
