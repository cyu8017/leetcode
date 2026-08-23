// LeetCode 3084 - Count Substrings Starting and Ending with Given Character
// https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/

public class Solution {
    public long CountSubstrings(string s, char c) {
        long cnt = 0;
        foreach (char ch in s) if (ch == c) cnt++;
        return cnt * (cnt + 1) / 2;
    }
}
