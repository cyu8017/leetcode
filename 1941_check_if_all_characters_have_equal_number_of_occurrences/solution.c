// LeetCode 1941 - Check if All Characters Have Equal Number of Occurrences
// https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

#include <stdbool.h>

bool areOccurrencesEqual(char* s) {
    int freq[26] = {0};
    for (char* p = s; *p; p++) freq[*p - 'a']++;
    int target = 0;
    for (int i = 0; i < 26; i++) {
        if (freq[i] == 0) continue;
        if (target == 0) target = freq[i];
        else if (freq[i] != target) return false;
    }
    return true;
}
