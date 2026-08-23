// LeetCode 2124 - Check if All A's Appears Before All B's
// https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

class Solution {
    public boolean checkString(String s) {
        boolean seenB = false;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'b') seenB = true;
            else if (seenB) return false;
        }
        return true;
    }
}
