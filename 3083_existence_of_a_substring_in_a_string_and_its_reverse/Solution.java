// LeetCode 3083 - Existence of a Substring in a String and Its Reverse
// https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/

class Solution {
    public boolean isSubstringPresent(String s) {
        boolean[][] st = new boolean[26][26];
        for (int i = 0; i + 1 < s.length(); i++)
            st[s.charAt(i + 1) - 'a'][s.charAt(i) - 'a'] = true;
        for (int i = 0; i + 1 < s.length(); i++)
            if (st[s.charAt(i) - 'a'][s.charAt(i + 1) - 'a']) return true;
        return false;
    }
}
