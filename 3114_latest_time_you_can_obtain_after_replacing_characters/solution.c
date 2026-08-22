// LeetCode 3114 - Latest Time You Can Obtain After Replacing Characters
// https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* findLatestTime(char* s) {
    char* out = (char*)malloc(6);
    for (int h = 11; h >= 0; h--) {
        for (int m = 59; m >= 0; m--) {
            char t[6];
            sprintf(t, "%02d:%02d", h, m);
            int ok = 1;
            for (int i = 0; i < 5; i++) {
                if (s[i] != '?' && s[i] != t[i]) { ok = 0; break; }
            }
            if (ok) {
                strcpy(out, t);
                return out;
            }
        }
    }
    strcpy(out, "00:00");
    return out;
}
