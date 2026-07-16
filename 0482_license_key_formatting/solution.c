// LeetCode 0482 - License Key Formatting
// https://leetcode.com/problems/license-key-formatting/

#include <ctype.h>
#include <stdlib.h>
#include <string.h>

char* licenseKeyFormatting(char* s, int k) {
    int rawLength = 0;
    for (int index = 0; s[index] != '\0'; index++) {
        if (s[index] != '-') {
            rawLength++;
        }
    }
    if (rawLength == 0) {
        char* empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }
    int firstLen = rawLength % k;
    if (firstLen == 0) {
        firstLen = k;
    }
    int dashCount = (rawLength - firstLen) / k;
    int resultLength = rawLength + dashCount;
    char* result = (char*)malloc((size_t)resultLength + 1);
    int writeIndex = 0;
    int seen = 0;
    for (int index = 0; s[index] != '\0'; index++) {
        if (s[index] == '-') {
            continue;
        }
        if (seen > 0 && (seen == firstLen || (seen - firstLen) % k == 0)) {
            result[writeIndex++] = '-';
        }
        result[writeIndex++] = (char)toupper((unsigned char)s[index]);
        seen++;
    }
    result[writeIndex] = '\0';
    return result;
}
