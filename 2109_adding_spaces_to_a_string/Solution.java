// LeetCode 2109 - Adding Spaces to a String
// https://leetcode.com/problems/adding-spaces-to-a-string/

class Solution {
    public String addSpaces(String s, int[] spaces) {
        StringBuilder b = new StringBuilder(s.length() + spaces.length);
        int j = 0;
        for (int i = 0; i < s.length(); i++) {
            if (j < spaces.length && spaces[j] == i) { b.append(' '); j++; }
            b.append(s.charAt(i));
        }
        return b.toString();
    }
}
