// LeetCode 0306 - Additive Number
// https://leetcode.com/problems/additive-number/

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static bool hasLeadingZero(const char* text, int length) {
    return length > 1 && text[0] == '0';
}

static long long parseNumber(const char* text, int length) {
    char buffer[32];
    strncpy(buffer, text, (size_t)length);
    buffer[length] = '\0';
    return strtoll(buffer, NULL, 10);
}

static void numberToString(long long value, char* buffer, size_t size) {
    snprintf(buffer, size, "%lld", value);
}

static bool valid(const char* num, const char* first, int firstLength, const char* second, int secondLength, int start) {
    if (hasLeadingZero(first, firstLength) || hasLeadingZero(second, secondLength)) {
        return false;
    }
    char firstBuffer[32];
    char secondBuffer[32];
    strncpy(firstBuffer, first, (size_t)firstLength);
    firstBuffer[firstLength] = '\0';
    strncpy(secondBuffer, second, (size_t)secondLength);
    secondBuffer[secondLength] = '\0';

    while (num[start] != '\0') {
        long long total = parseNumber(firstBuffer, (int)strlen(firstBuffer))
            + parseNumber(secondBuffer, (int)strlen(secondBuffer));
        char totalText[32];
        numberToString(total, totalText, sizeof(totalText));
        if (strncmp(num + start, totalText, strlen(totalText)) != 0) {
            return false;
        }
        strcpy(firstBuffer, secondBuffer);
        strcpy(secondBuffer, totalText);
        start += (int)strlen(totalText);
    }
    return true;
}

bool isAdditiveNumber(char* num) {
    int length = (int)strlen(num);
    for (int firstEnd = 1; firstEnd < length; firstEnd++) {
        for (int secondEnd = firstEnd + 1; secondEnd < length; secondEnd++) {
            if (valid(num, num, firstEnd, num + firstEnd, secondEnd - firstEnd, secondEnd)) {
                return true;
            }
        }
    }
    return false;
}
