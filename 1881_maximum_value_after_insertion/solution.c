// LeetCode 1881 - Maximum Value after Insertion
// https://leetcode.com/problems/maximum-value-after-insertion/

#include <stdlib.h>
#include <string.h>

char* maxValue(char* n, int x) {
    int len = (int)strlen(n);
    char* result = (char*)malloc((size_t)len + 2);
    int neg = n[0] == '-';
    int start = neg ? 1 : 0;
    int insertAt = len;
    for (int i = start; i < len; i++) {
        int d = n[i] - '0';
        if (neg) {
            if (d > x) {
                insertAt = i;
                break;
            }
        } else if (d < x) {
            insertAt = i;
            break;
        }
    }
    memcpy(result, n, (size_t)insertAt);
    result[insertAt] = (char)('0' + x);
    memcpy(result + insertAt + 1, n + insertAt, (size_t)(len - insertAt));
    result[len + 1] = '\0';
    return result;
}
