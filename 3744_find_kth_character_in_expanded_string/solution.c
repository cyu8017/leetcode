// LeetCode 3744 - Find Kth Character in Expanded String
// https://leetcode.com/problems/find-kth-character-in-expanded-string/

#include <string.h>
#include <stdlib.h>

char kthCharacter(char* s, long long k) {
    int n = (int)strlen(s);
    int start = 0;
    while (start < n) {
        while (start < n && s[start] == ' ') start++;
        if (start >= n) break;
        int end = start;
        while (end < n && s[end] != ' ') end++;
        int len = end - start;
        long long m = (1 + (long long)len) * len / 2;
        if (k == m) return ' ';
        if (k > m) {
            k -= m + 1;
        } else {
            long long cur = 0;
            for (int i = 0; ; i++) {
                cur += i + 1;
                if (k < cur) return s[start + i];
            }
        }
        start = end;
    }
    return ' ';
}
