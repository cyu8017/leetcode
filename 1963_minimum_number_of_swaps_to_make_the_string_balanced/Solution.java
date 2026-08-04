// LeetCode 1963 - Minimum Number of Swaps to Make the String Balanced
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

class Solution {
    public int minSwaps(String s) {
        int bal = 0, mx = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '[') bal++;
            else bal--;
            mx = Math.min(mx, bal);
        }
        return (-mx + 1) / 2;
    }
}
