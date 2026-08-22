// LeetCode 3894 - Traffic Signal Color
// https://leetcode.com/problems/traffic-signal-color/

#include <stdlib.h>
#include <string.h>

char* trafficSignal(int timer) {
    const char* s;
    if (timer == 0) s = "Green";
    else if (timer == 30) s = "Orange";
    else if (timer > 30 && timer <= 90) s = "Red";
    else s = "Invalid";
    char* out = malloc(strlen(s) + 1);
    strcpy(out, s);
    return out;
}
