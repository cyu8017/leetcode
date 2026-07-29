// LeetCode 0681 - Next Closest Time
// https://leetcode.com/problems/next-closest-time/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* nextClosestTime(char* time) {
    int digits[4] = {time[0]-'0', time[1]-'0', time[3]-'0', time[4]-'0'};
    int start = digits[0]*600 + digits[1]*60 + digits[2]*10 + digits[3];
    char* result = (char*)malloc(6);
    for (int elapsed = 1; elapsed <= 24*60; elapsed++) {
        int cur = (start + elapsed) % (24*60);
        int hh = cur / 60, mm = cur % 60;
        int cand[4] = {hh/10, hh%10, mm/10, mm%10};
        int ok = 1;
        for (int i = 0; i < 4 && ok; i++) {
            int found = 0;
            for (int j = 0; j < 4; j++) if (cand[i] == digits[j]) found = 1;
            if (!found) ok = 0;
        }
        if (ok) {
            snprintf(result, 6, "%02d:%02d", hh, mm);
            return result;
        }
    }
    strcpy(result, time);
    return result;
}
