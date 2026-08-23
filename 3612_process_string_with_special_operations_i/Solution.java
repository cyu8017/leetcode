// LeetCode 3612 - Process String with Special Operations I
// https://leetcode.com/problems/process-string-with-special-operations-i/

class Solution {
    public String processStr(String s) {
        StringBuilder result = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) result.append(c);
            else if (c == '*') {
                if (result.length() > 0) result.setLength(result.length() - 1);
            } else if (c == '#') result.append(result);
            else if (c == '%') result.reverse();
        }
        return result.toString();
    }
}
