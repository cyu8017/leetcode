// LeetCode 2283 - Check if Number Has Equal Digit Count and Digit Value
// https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

class Solution {
    public boolean digitCount(String num) {
        int[] cnt = new int[10];
        for (char c : num.toCharArray()) cnt[c - '0']++;
        for (int i = 0; i < num.length(); i++)
            if (cnt[i] != num.charAt(i) - '0') return false;
        return true;
    }
}
