// LeetCode 1221 - Split a String in Balanced Strings
// https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution {
    public int balancedStringSplit(String s) {
        int balance = 0, answer = 0;
        for (int i = 0; i < s.length(); i++) {
            balance += s.charAt(i) == 'L' ? 1 : -1;
            if (balance == 0) answer++;
        }
        return answer;
    }
}

