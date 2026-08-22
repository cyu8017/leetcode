// LeetCode 1736 - Latest Time by Replacing Hidden Digits
// https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/

#include <string.h>

char* maximumTime(char* time) {
    if (time[0] == '?') {
        time[0] = (time[1] == '?' || strchr("0123", time[1]) != NULL) ? '2' : '1';
    }
    if (time[1] == '?') {
        time[1] = time[0] == '2' ? '3' : '9';
    }
    if (time[3] == '?') {
        time[3] = '5';
    }
    if (time[4] == '?') {
        time[4] = '9';
    }
    return time;
}
