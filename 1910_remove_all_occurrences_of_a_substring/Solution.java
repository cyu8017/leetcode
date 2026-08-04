// LeetCode 1910 - Remove All Occurrences of a Substring
// https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

class Solution {
    public String removeOccurrences(String s, String part) {
        StringBuilder stack = new StringBuilder();
        int m = part.length();
        for (int i = 0; i < s.length(); i++) {
            stack.append(s.charAt(i));
            if (stack.length() >= m && stack.substring(stack.length() - m).equals(part)) {
                stack.setLength(stack.length() - m);
            }
        }
        return stack.toString();
    }
}
