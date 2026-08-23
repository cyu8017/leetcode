// LeetCode 2384 - Largest Palindromic Number
// https://leetcode.com/problems/largest-palindromic-number/

class Solution {
    public String largestPalindromic(String num) {
        int[] freq = new int[10];
        for (int i = 0; i < num.length(); i++) freq[num.charAt(i) - '0']++;
        StringBuilder left = new StringBuilder();
        for (int d = 9; d >= 0; d--) {
            int pairs = freq[d] / 2;
            for (int i = 0; i < pairs; i++) left.append((char) ('0' + d));
            freq[d] %= 2;
        }
        char mid = 0;
        for (int d = 9; d >= 0; d--) {
            if (freq[d] > 0) {
                mid = (char) ('0' + d);
                break;
            }
        }
        if (left.length() == 0) {
            return mid == 0 ? "0" : String.valueOf(mid);
        }
        if (left.charAt(0) == '0') {
            return mid == 0 ? "0" : String.valueOf(mid);
        }
        StringBuilder ans = new StringBuilder(left);
        if (mid != 0) ans.append(mid);
        ans.append(left.reverse());
        return ans.toString();
    }
}
