// LeetCode 0161 - One Edit Distance
#include <stdbool.h>
#include <string.h>
bool isOneEditDistance(char* s, char* t) {
    int m = strlen(s), n = strlen(t);
    if (m > n) return isOneEditDistance(t, s);
    if (n - m > 1 || !strcmp(s, t)) return false;
    int i = 0;
    while (i < m && s[i] == t[i]) ++i;
    return m == n ? !strcmp(s + i + 1, t + i + 1) : !strcmp(s + i, t + i + 1);
}