// LeetCode 2390 - Removing Stars From a String
// https://leetcode.com/problems/removing-stars-from-a-string/

class Solution {
    public String removeStars(String s) {
        var stack = new StringBuilder();
        for (char c : s) {
            if (c == '*') stack.length--;
            else stack.append(c);
        }
        return stack.toString();
    }
}
