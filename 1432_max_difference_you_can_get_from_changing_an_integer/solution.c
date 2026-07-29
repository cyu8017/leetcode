// LeetCode 1432 - Max Difference You Can Get From Changing an Integer
// https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

static void replace_char(char* s, char from, char to) {
    for (int i = 0; s[i]; i++) if (s[i] == from) s[i] = to;
}

int maxDiff(int num) {
    char s[16], high[16], low[16];
    sprintf(s, "%d", num);
    strcpy(high, s); strcpy(low, s);
    for (int i = 0; high[i]; i++) if (high[i] != '9') { replace_char(high, high[i], '9'); break; }
    if (low[0] != '1') replace_char(low, low[0], '1');
    else {
        for (int i = 1; low[i]; i++)
            if (low[i] != '0' && low[i] != '1') { replace_char(low, low[i], '0'); break; }
    }
    return atoi(high) - atoi(low);
}
