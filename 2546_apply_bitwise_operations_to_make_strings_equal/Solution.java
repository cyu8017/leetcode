// LeetCode 2546 - Apply Bitwise Operations to Make Strings Equal
// https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/

class Solution {
    public boolean makeStringsEqual(String s, String target) {
        boolean has1s = false, has1t = false;
        for (int i = 0; i < s.length(); ++i) {
            if (s.charAt(i) == '1') has1s = true;
            if (target.charAt(i) == '1') has1t = true;
        }
        return has1s == has1t;
    }
}
