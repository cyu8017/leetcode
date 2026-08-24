// CONFIG class=Solution method=secondsBetweenTimes types=None
// LeetCode 3986 - Number of Elapsed Seconds Between Two Times
// https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/

class Solution {
    static int toSeconds(String s) {
        int h = (s.charAt(0) - '0') * 10 + (s.charAt(1) - '0');
        int m = (s.charAt(3) - '0') * 10 + (s.charAt(4) - '0');
        int sec = (s.charAt(6) - '0') * 10 + (s.charAt(7) - '0');
        return h * 3600 + m * 60 + sec;
    }

    public int secondsBetweenTimes(String startTime, String endTime) {
        return toSeconds(endTime) - toSeconds(startTime);
    }
}
