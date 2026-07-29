// LeetCode 1154 - Day of the Year
// https://leetcode.com/problems/day-of-the-year/

#include <stdio.h>

int dayOfYear(char* date) {
    int year, month, day;
    sscanf(date, "%d-%d-%d", &year, &month, &day);
    int leap = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    int days[] = {31, leap ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int ans = day;
    for (int i = 0; i < month - 1; i++) ans += days[i];
    return ans;
}
