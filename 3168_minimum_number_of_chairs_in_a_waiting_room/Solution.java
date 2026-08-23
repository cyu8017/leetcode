// LeetCode 3168 - Minimum Number of Chairs in a Waiting Room
// https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/

class Solution {
    public int minimumChairs(String s) {
        int cnt = 0, left = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'E') {
                if (left > 0) left--;
                else cnt++;
            } else left++;
        }
        return cnt;
    }
}
