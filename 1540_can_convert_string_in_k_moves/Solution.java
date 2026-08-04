// LeetCode 1540 - Can Convert String in K Moves
// https://leetcode.com/problems/can-convert-string-in-k-moves/

class Solution {
    public boolean canConvertString(String s, String t, int k) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] used = new int[26];
        for (int i = 0; i < s.length(); i++) {
            int shift = (t.charAt(i) - s.charAt(i) + 26) % 26;
            if (shift == 0) {
                continue;
            }
            used[shift]++;
            if (shift + 26L * (used[shift] - 1) > k) {
                return false;
            }
        }
        return true;
    }
}
