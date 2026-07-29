// LeetCode 0686 - Repeated String Match
// https://leetcode.com/problems/repeated-string-match/

#include <stdlib.h>
#include <string.h>

int repeatedStringMatch(char* a, char* b) {
    int la = (int)strlen(a), lb = (int)strlen(b);
    int times = (lb + la - 1) / la;
    int cap = (times + 2) * la + 1;
    char* buf = (char*)malloc((size_t)cap);
    buf[0] = '\0';
    for (int i = 0; i < times; i++) strcat(buf, a);
    if (strstr(buf, b)) { free(buf); return times; }
    strcat(buf, a);
    if (strstr(buf, b)) { free(buf); return times + 1; }
    strcat(buf, a);
    if (strstr(buf, b)) { free(buf); return times + 2; }
    free(buf);
    return -1;
}
