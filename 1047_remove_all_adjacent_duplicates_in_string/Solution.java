// LeetCode 1047 - Remove All Adjacent Duplicates In String
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution {
    public String removeDuplicates(String s) {
        StringBuilder stack = new StringBuilder();
        for (char ch : s.toCharArray()) {
            int n = stack.length();
            if (n > 0 && stack.charAt(n - 1) == ch) stack.setLength(n - 1);
            else stack.append(ch);
        }
        return stack.toString();
    }
}
