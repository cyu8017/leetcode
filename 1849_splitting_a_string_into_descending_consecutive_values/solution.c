// LeetCode 1849 - Splitting a String Into Descending Consecutive Values
// https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

#include <stdbool.h>
#include <string.h>

static bool parseUll(const char* s, int l, int r, unsigned long long* out) {
    if (l >= r) return false;
    unsigned long long value = 0;
    for (int i = l; i < r; i++) {
        unsigned long long digit = (unsigned long long)(s[i] - '0');
        if (value > (18446744073709551615ULL - digit) / 10ULL) return false;
        value = value * 10ULL + digit;
    }
    *out = value;
    return true;
}

static bool dfsSplit(const char* s, int n, int index, unsigned long long previous, int hasPrev, int parts) {
    if (index == n) return parts >= 2;
    for (int end = index + 1; end <= n; end++) {
        unsigned long long value;
        if (!parseUll(s, index, end, &value)) break;
        if (!hasPrev) {
            if (dfsSplit(s, n, end, value, 1, parts + 1)) return true;
        } else if (previous > 0 && value == previous - 1) {
            if (dfsSplit(s, n, end, value, 1, parts + 1)) return true;
        } else if (previous == 0 || value > previous - 1) {
            break;
        }
    }
    return false;
}

bool splitString(char* s) {
    int n = (int)strlen(s);
    return dfsSplit(s, n, 0, 0, 0, 0);
}
