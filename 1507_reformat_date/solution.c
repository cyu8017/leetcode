// LeetCode 1507 - Reformat Date
// https://leetcode.com/problems/reformat-date/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char* reformatDate(char* date) {
    static const char* months[] = {
        "Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"
    };
    char day[8], month[8], year[8];
    sscanf(date, "%s %s %s", day, month, year);
    int d = atoi(day);
    int m = 0;
    for (int i = 0; i < 12; i++) {
        if (strcmp(month, months[i]) == 0) { m = i + 1; break; }
    }
    char* out = (char*)malloc(11);
    sprintf(out, "%s-%02d-%02d", year, m, d);
    return out;
}
