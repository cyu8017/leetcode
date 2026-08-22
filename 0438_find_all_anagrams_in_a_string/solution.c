// LeetCode 0438 - Find All Anagrams in a String
// https://leetcode.com/problems/find-all-anagrams-in-a-string/

#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findAnagrams(char* s, char* p, int* returnSize) {
    int sLen = (int)strlen(s);
    int pLen = (int)strlen(p);
    if (sLen < pLen) {
        *returnSize = 0;
        return (int*)malloc(sizeof(int));
    }

    int need[26] = {0};
    int window[26] = {0};
    for (int i = 0; i < pLen; i++) {
        need[p[i] - 'a']++;
        window[s[i] - 'a']++;
    }

    int* result = (int*)malloc((size_t)(sLen - pLen + 1) * sizeof(int));
    int count = 0;
    int matches = 0;
    for (int i = 0; i < 26; i++) {
        if (need[i] == window[i]) {
            matches++;
        }
    }
    if (matches == 26) {
        result[count++] = 0;
    }

    for (int right = pLen; right < sLen; right++) {
        int add = s[right] - 'a';
        int remove = s[right - pLen] - 'a';

        if (window[add] == need[add]) {
            matches--;
        }
        window[add]++;
        if (window[add] == need[add]) {
            matches++;
        }

        if (window[remove] == need[remove]) {
            matches--;
        }
        window[remove]--;
        if (window[remove] == need[remove]) {
            matches++;
        }

        if (matches == 26) {
            result[count++] = right - pLen + 1;
        }
    }

    *returnSize = count;
    return result;
}
