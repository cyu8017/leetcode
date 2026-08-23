// LeetCode 2696 - Minimum String Length After Removing Substrings
// https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

class Solution {
    public int minLength(String s) {
        StringBuilder st = new StringBuilder();
        for (char c : s.toCharArray()) {
            int len = st.length();
            if (len > 0 && ((st.charAt(len - 1) == 'A' && c == 'B') || (st.charAt(len - 1) == 'C' && c == 'D')))
                st.setLength(len - 1);
            else st.append(c);
        }
        return st.length();
    }
}
