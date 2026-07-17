// LeetCode 1790 - Check if One String Swap Can Make Strings Equal
// https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        int first = -1;
        int second = -1;
        int count = 0;
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                count++;
                if (count == 1) {
                    first = i;
                } else if (count == 2) {
                    second = i;
                } else {
                    return false;
                }
            }
        }
        if (count == 0) return true;
        return count == 2
            && s1.charAt(first) == s2.charAt(second)
            && s1.charAt(second) == s2.charAt(first);
    }
}
