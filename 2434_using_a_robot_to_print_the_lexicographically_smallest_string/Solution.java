// LeetCode 2434 - Using a Robot to Print the Lexicographically Smallest String
// https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

class Solution {
    public String robotWithString(String s) {
        int n = s.length();
        char[] minSuf = new char[n + 1];
        minSuf[n] = (char)('z' + 1);
        for (int i = n - 1; i >= 0; i--)
            minSuf[i] = s.charAt(i) < minSuf[i + 1] ? s.charAt(i) : minSuf[i + 1];
        var stack = new StringBuilder();
        var ans = new StringBuilder();
        for (int i = 0; i < n; i++) {
            stack.append(s.charAt(i));
            while (stack.length > 0 && stack[stack.length - 1] <= minSuf[i + 1]) {
                ans.append(stack[stack.length - 1]);
                stack.length--;
            }
        }
        while (stack.length > 0) {
            ans.append(stack[stack.length - 1]);
            stack.length--;
        }
        return ans.toString();
    }
}
