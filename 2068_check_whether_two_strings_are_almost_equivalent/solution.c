// LeetCode 2068 - Check Whether Two Strings Are Almost Equivalent
// https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

#include <stdbool.h>
#include <string.h>

bool checkAlmostEquivalent(char* word1, char* word2) {
    int freq[26] = {0};
    for (int i = 0; word1[i]; i++) {
        freq[word1[i] - 'a']++;
        freq[word2[i] - 'a']--;
    }
    for (int i = 0; i < 26; i++) if (freq[i] > 3 || freq[i] < -3) return false;
    return true;
}
