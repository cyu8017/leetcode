// LeetCode 1957 - Delete Characters to Make Fancy String
// https://leetcode.com/problems/delete-characters-to-make-fancy-string/

class Solution {
    public String makeFancyString(String s) {
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int n = ans.length();
            if (n >= 2 && ans.charAt(n - 1) == c && ans.charAt(n - 2) == c) continue;
            ans.append(c);
        }
        return ans.toString();
    }
}
