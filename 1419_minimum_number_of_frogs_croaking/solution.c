// LeetCode 1419 - Minimum Number of Frogs Croaking
// https://leetcode.com/problems/minimum-number-of-frogs-croaking/

#include <string.h>

int minNumberOfFrogs(char* croakOfFrogs) {
    const char* order = "croak";
    int counts[5] = {0};
    int active = 0, answer = 0;
    for (int i = 0; croakOfFrogs[i]; i++) {
        const char* p = strchr(order, croakOfFrogs[i]);
        if (!p) return -1;
        int idx = (int)(p - order);
        if (idx && counts[idx - 1] == 0) return -1;
        if (idx) counts[idx - 1]--;
        counts[idx]++;
        if (idx == 0) {
            active++;
            if (active > answer) answer = active;
        } else if (idx == 4) {
            counts[4]--;
            active--;
        }
    }
    return active == 0 ? answer : -1;
}
