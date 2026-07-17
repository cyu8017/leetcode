// LeetCode 1864 - Minimum Number of Swaps to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

class Solution {
    public int minSwaps(String s) {
        int zeros = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '0') {
                zeros++;
            }
        }
        int ones = s.length() - zeros;
        if (Math.abs(zeros - ones) > 1) {
            return -1;
        }

        if (zeros == ones) {
            return Math.min(mismatches(s, "01"), mismatches(s, "10"));
        }
        if (zeros > ones) {
            return mismatches(s, "01");
        }
        return mismatches(s, "10");
    }

    private int mismatches(String s, String pattern) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != pattern.charAt(i % 2)) {
                count++;
            }
        }
        return count / 2;
    }
}
