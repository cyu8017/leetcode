// LeetCode 0423 - Reconstruct Original Digits from English
// https://leetcode.com/problems/reconstruct-original-digits-from-english/

#include <stdlib.h>
#include <string.h>

char* originalDigits(char* s) {
    int counts[26] = {0};
    for (int i = 0; s[i]; i++) {
        counts[s[i] - 'a']++;
    }

    int digitCounts[10] = {0};
    digitCounts[0] = counts['z' - 'a'];
    digitCounts[2] = counts['w' - 'a'];
    digitCounts[4] = counts['u' - 'a'];
    digitCounts[6] = counts['x' - 'a'];
    digitCounts[8] = counts['g' - 'a'];
    digitCounts[1] = counts['o' - 'a'] - digitCounts[0] - digitCounts[2] - digitCounts[4];
    digitCounts[3] = counts['h' - 'a'] - digitCounts[8];
    digitCounts[5] = counts['f' - 'a'] - digitCounts[4];
    digitCounts[7] = counts['s' - 'a'] - digitCounts[6];
    digitCounts[9] = counts['i' - 'a'] - digitCounts[5] - digitCounts[6] - digitCounts[8];

    int total = 0;
    for (int d = 0; d < 10; d++) {
        total += digitCounts[d];
    }

    char* result = (char*)malloc((size_t)total + 1);
    int pos = 0;
    for (int d = 0; d < 10; d++) {
        for (int i = 0; i < digitCounts[d]; i++) {
            result[pos++] = (char)('0' + d);
        }
    }
    result[pos] = '\0';
    return result;
}
