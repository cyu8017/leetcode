// LeetCode 1794 - Count Pairs of Equal Substrings With Minimum Difference
// https://leetcode.com/problems/count-pairs-of-equal-substrings-with-minimum-difference/

#include <limits.h>
#include <string.h>

long long countQuadruples(char* firstString, char* secondString) {
    int first[26], lastF[26], lastS[26];
    for (int c = 0; c < 26; c++) {
        first[c] = -1;
        lastF[c] = -1;
        lastS[c] = -1;
    }
    int n1 = strlen(firstString);
    int n2 = strlen(secondString);
    for (int i = 0; i < n1; i++) {
        int c = firstString[i] - 'a';
        if (first[c] == -1) first[c] = i;
        lastF[c] = i;
    }
    for (int i = 0; i < n2; i++) {
        lastS[secondString[i] - 'a'] = i;
    }
    long long best = LLONG_MAX;
    for (int c = 0; c < 26; c++) {
        if (first[c] != -1 && lastS[c] != -1) {
            long long diff = (long long)lastF[c] - lastS[c];
            if (diff < best) best = diff;
        }
    }
    if (best == LLONG_MAX) return 0;
    long long ans = 0;
    for (int c = 0; c < 26; c++) {
        if (first[c] == -1 || lastS[c] == -1 || lastF[c] - lastS[c] != best) continue;
        long long iCount = 0;
        for (int k = first[c]; k <= lastF[c]; k++) {
            if (firstString[k] - 'a' == c) iCount++;
        }
        long long aCount = 0;
        for (int k = 0; k <= lastS[c]; k++) {
            if (secondString[k] - 'a' == c) aCount++;
        }
        ans += iCount * aCount;
    }
    return ans;
}
