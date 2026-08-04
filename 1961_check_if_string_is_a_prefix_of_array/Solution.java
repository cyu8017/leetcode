// LeetCode 1961 - Check If String Is a Prefix of Array
// https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

class Solution {
    public boolean isPrefixString(String s, String[] words) {
        StringBuilder built = new StringBuilder();
        for (String w : words) {
            built.append(w);
            String cur = built.toString();
            if (cur.equals(s)) return true;
            if (cur.length() > s.length() || !s.startsWith(cur)) return false;
        }
        return false;
    }
}
