// LeetCode 0564 - Find the Closest Palindrome
// https://leetcode.com/problems/find-the-closest-palindrome/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static long long makePalindrome(long long half, int length) {
    char text[32];
    sprintf(text, "%lld", half);
    char pal[64];
    int halfLen = (int)strlen(text);
    strcpy(pal, text);
    if (length % 2 == 0) {
        for (int i = halfLen - 1; i >= 0; i--) {
            int pos = (int)strlen(pal);
            pal[pos] = text[i];
            pal[pos + 1] = '\0';
        }
    } else {
        for (int i = halfLen - 2; i >= 0; i--) {
            int pos = (int)strlen(pal);
            pal[pos] = text[i];
            pal[pos + 1] = '\0';
        }
    }
    return atoll(pal);
}

static long long pow10ll(int exp) {
    long long value = 1;
    for (int i = 0; i < exp; i++) {
        value *= 10;
    }
    return value;
}

char* nearestPalindromic(char* n) {
    int length = (int)strlen(n);
    long long number = atoll(n);
    long long candidates[5];
    int count = 0;
    candidates[count++] = pow10ll(length - 1) - 1;
    candidates[count++] = pow10ll(length) + 1;

    char prefixText[32];
    int prefixLen = (length + 1) / 2;
    strncpy(prefixText, n, (size_t)prefixLen);
    prefixText[prefixLen] = '\0';
    long long prefix = atoll(prefixText);
    for (long long half = prefix - 1; half <= prefix + 1; half++) {
        candidates[count++] = makePalindrome(half, length);
    }

    long long best = -1;
    long long bestDiff = 0;
    for (int i = 0; i < count; i++) {
        if (candidates[i] == number) {
            continue;
        }
        long long diff = candidates[i] - number;
        if (diff < 0) {
            diff = -diff;
        }
        if (best == -1 || diff < bestDiff || (diff == bestDiff && candidates[i] < best)) {
            best = candidates[i];
            bestDiff = diff;
        }
    }

    char* result = (char*)malloc(32);
    sprintf(result, "%lld", best);
    return result;
}
