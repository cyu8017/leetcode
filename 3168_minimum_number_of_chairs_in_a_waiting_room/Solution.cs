// LeetCode 3168 - Minimum Number of Chairs in a Waiting Room
// https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/

public class Solution {
    public int MinimumChairs(string s) {
        int cnt = 0, left = 0;
        foreach (char c in s) {
            if (c == 'E') {
                if (left > 0) left--;
                else cnt++;
            } else left++;
        }
        return cnt;
    }
}
