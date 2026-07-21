// LeetCode 1897 - Redistribute Characters to Make All Strings Equal
// https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

#include <stdbool.h>
#include <string.h>

bool makeEqual(char** words, int wordsSize) {
    int counts[26] = {0};
    for (int i = 0; i < wordsSize; i++) {
        for (int j = 0; words[i][j]; j++) counts[words[i][j] - 'a']++;
    }
    for (int i = 0; i < 26; i++) {
        if (counts[i] % wordsSize != 0) return false;
    }
    return true;
}
