// LeetCode 1221 - Split a String in Balanced Strings
// https://leetcode.com/problems/split-a-string-in-balanced-strings/

public class Solution {
    public int BalancedStringSplit(string s) {
        int balance = 0, answer = 0;
        foreach (char ch in s) {
            balance += ch == 'L' ? 1 : -1;
            if (balance == 0) answer++;
        }
        return answer;
    }
}
