// LeetCode 3986 - Number of Elapsed Seconds Between Two Times
// https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/

static int toSeconds3986(char* s) {
    int h = (s[0] - '0') * 10 + (s[1] - '0');
    int m = (s[3] - '0') * 10 + (s[4] - '0');
    int sec = (s[6] - '0') * 10 + (s[7] - '0');
    return h * 3600 + m * 60 + sec;
}

int secondsBetweenTimes(char* startTime, char* endTime) {
    return toSeconds3986(endTime) - toSeconds3986(startTime);
}
